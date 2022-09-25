from tkinter import E
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from school.models import *
from teacher.models import *
from student.models import *
import random
from django.contrib.auth.decorators import login_required

from .forms import QuestionsForm, AnswerForm
# Create your views here.

@login_required(login_url='/school/school-login')
def add_quiz(request):
    # check if the school/teacher is logged in or not
    if request.user.groups.filter(name='school').exists() or request.user.groups.filter(name='Teachers').exists():
        if request.user.groups.filter(name='school').exists():
            school = request.user.schooluserprofile
            schoolNavHeader = True
            classrooms = Classroom.objects.filter(school_id=school)
        else:
            school = request.user.teacherprofile.school
            teacher = request.user.teacherprofile
            schoolNavHeader = False
            classrooms = teacher.classroom.all()

        if True:
            if request.method == 'POST':
                print('tt')
                classroom = request.POST['classroom']
                subject = request.POST['subject']
                teacher = request.POST['teacher']
                quiz_schedule = request.POST['quiz_schedule']
                title = request.POST['title']
                time_limit = request.POST['time_limit']

                hasError = False
                if not Classroom.objects.filter(id=int(classroom)).exists():
                    hasError = True
                if not subjects.objects.filter(id=int(subject)).exists():
                    hasError = True
                if not teacher_profile.objects.filter(id=int(teacher)).exists():
                    hasError = True
                if int(teacher)<1 :
                    hasError = True           

                if hasError != False:
                    return redirect('/quiz/add?msg=form-invalid') 
                else:
                    new_quiz = quiz.objects.create(
                        classroom = Classroom.objects.get(id=int(classroom)),
                        subject = subjects.objects.get(id=int(subject)),
                        teacher = teacher_profile.objects.get(id=int(teacher)),
                        quiz_schedule = quiz_schedule,
                        title = title,
                        time_limit = time_limit,
                    )
                    new_quiz.save()
                    quiz_id = new_quiz.quiz_id
                    return redirect(f"/quiz/search-ques/?quiz_id={quiz_id}&msg=Quiz-added")
            context = {
                'classrooms' : classrooms,
                'teachers' : teacher_profile.objects.filter(school=school),
                'schoolNavHeader' : schoolNavHeader,
                'subjects' : subjects.objects.all() if schoolNavHeader else teacher.subject
            }       
            return render(request, 'quiz/add-quiz.html', context)
        else:#
            return redirect('/quiz/add')     
    return redirect('/')    

def valid_quiz_uid(quiz_id):
    if quiz.objects.filter(quiz_id=quiz_id).exists():
        return True
    else:
        return False    

# normal search ques page
@login_required(login_url='/school/school-login')
def search_ques(request):
    if request.user.groups.filter(name='school').exists() or request.user.groups.filter(name='Teachers').exists():
        if request.user.groups.filter(name='school').exists():
            school = request.user.schooluserprofile
            schoolNavHeader = True
        else:
            school = request.user.teacherprofile.school
            schoolNavHeader = False

        if not 'quiz_id' in request.GET:
            return redirect('/quiz/add/?msg=no-uid')   

        if not valid_quiz_uid(str(request.GET['quiz_id'])):
            return redirect('/quiz/add/?msg=uid-not-found')       

        quiz_id = str(request.GET['quiz_id'])

        new_quiz = quiz.objects.get(quiz_id=quiz_id)

        context = {
            'quiz' : new_quiz,
            'quiz_id' : quiz_id,
            'schoolNavHeader' : schoolNavHeader,
            'questions' : Question.objects.all(),
        }       
        return render(request, 'quiz/search-ques.html', context)
    return redirect('/')   
    


def select_question_api(request):
    try:
        question_objs = list(Question.objects.all())
        if 'qs' in request.GET:
            question_objs = list(Question.objects.filter(question__icontains = request.GET['qs']))
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "category" : question_obj.level.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers(),
                'question_id' : question_obj.uid,
            })
        
        payload = {'status' : True, 'data' : data}
        
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong.")

@login_required(login_url='/')
def quiz_list(request):

    if request.user.groups.filter(name='school').exists():
            
        school = School.objects.get(user=request.user)
        schoolNavHeader =  True
        isStudent = False
        quizs  = quiz.objects.filter(classroom__school_id= school)  
    elif request.user.groups.filter(name='Teachers').exists():
        school = request.user.teacherprofile.school
        schoolNavHeader = isStudent = False
        quizs  = quiz.objects.filter(classroom__school_id= school)  
    else:
        schoolNavHeader = False
        isStudent = True
        quizs  = quiz.objects.filter(classroom= request.user.studentprofile.classroom)  

    

    context = {
        'quizs' : quizs,
        'schoolNavHeader' : schoolNavHeader,
        'isStudent' : isStudent
    }       
    return render(request, 'quiz/quiz-list.html', context)  



def select_quiz_profile_api(request):
    if request.user.groups.filter(name='school').exists() or request.user.groups.filter(name='Teachers').exists():
        if request.user.groups.filter(name='school').exists():
            school = request.user.schooluserprofile
            schoolNavHeader = True
        else:
            school = request.user.teacherprofile.school
            schoolNavHeader = False

        if not 'quiz_id' in request.GET:
            return redirect('/quiz/add/?msg=no-uid')   

        if not valid_quiz_uid(str(request.GET['quiz_id'])):
            return redirect('/quiz/add/?msg=uid-not-found')       


        quiz_id = str(request.GET['quiz_id'])
        pro_quiz = quiz.objects.get(quiz_id=quiz_id)

        context = {
            'quiz' : pro_quiz,
            'quiz_id' : quiz_id,
            'schoolNavHeader' : schoolNavHeader,
        }       
        return render(request, 'quiz/quiz-profile.html', context)   


             
        return redirect('/quiz/list?msg=add-success') ###
    return redirect('/')   


@login_required(login_url='/school/school-login')
def add_quiz_question_api(request):
    try:
        question_objs = list(Question.objects.all())
        if 'quiz_uid' in request.GET and 'question_uid' in request.GET:
            if not valid_quiz_uid(str(request.GET['quiz_uid'])):
                return redirect('/quiz/add/')
            if not Question.objects.filter(uid=str(request.GET['question_uid'])):
                return redirect('/quiz/add/')      
        else:
            return redirect('/quiz/add/')   

        add_quiz =  quiz.objects.get(quiz_id=str(request.GET['quiz_uid']))    
        new_question = Question.objects.get(uid=str(request.GET['question_uid']))

        add_quiz.question_list.add(new_question)
        add_quiz.save()

        payload = {'status' : True, 'data' : 'Added'}
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong.")

@login_required(login_url='/school/school-login')
def del_quiz_question_api(request):
    try:

        if 'quiz_uid' in request.GET and 'question_uid' in request.GET:
            if not valid_quiz_uid(str(request.GET['quiz_uid'])):
                return redirect('/quiz/add/')
            if not Question.objects.filter(uid=str(request.GET['question_uid'])):
                return redirect('/quiz/add/')      
        else:
            return redirect('/quiz/add/')   

        del_quiz =  quiz.objects.get(quiz_id=str(request.GET['quiz_uid']))    
        del_question = Question.objects.get(uid=str(request.GET['question_uid']))

        del_quiz.question_list.remove(del_question)

        payload = {'status' : True, 'data' : 'Deleted'}
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong.")


@login_required(login_url='/school/school-login')
def get_quiz_questions_api(request):
    try:
        if 'quiz_uid' in request.GET:
            if not valid_quiz_uid(str(request.GET['quiz_uid'])):
                return redirect('/quiz/add/')  
        else:
            return redirect('/quiz/add/')   

        the_quiz =  quiz.objects.get(quiz_id=str(request.GET['quiz_uid']))

        qi_li = the_quiz.question_list.all()

        data = []
        for question_obj in qi_li:
            data.append({
                "question" : question_obj.question,
                'question_id' : question_obj.uid,
            })
        payload = {'status' : True, 'data' : data}
        return JsonResponse(payload)
    
    except:
        return HttpResponse("Something went wrong.")

def add_ques(request):
    quesForm = QuestionsForm()
    if request.user.groups.filter(name='school').exists():
        schoolNavHeader =  True
    else:
        schoolNavHeader = False
    if request.method == "POST":
        quesForm = QuestionsForm(request.POST)
        if quesForm.is_valid():
            quesForm.save()
    context = {'quesForm': quesForm, 'schoolNavHeader':schoolNavHeader}
    return render(request, 'quiz/add_ques.html', context)


def ques_list(request):
    if request.user.groups.filter(name='school').exists():
        schoolNavHeader =  True
    else:
        schoolNavHeader = isStudent = False
    context = {
        'questions' : Question.objects.all(),
        'schoolNavHeader':schoolNavHeader
    }
    return render(request, 'quiz/ques_list.html', context)

