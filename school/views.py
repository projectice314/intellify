# Hi there

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages

from teacher.models import teacher_profile

from .models import School, subjects, Classroom
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.

# School Dashboard (Wasif)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def schoolHome(request):
    school_name = request.user
  
    context = {'school_name': school_name, }
    return render(request, 'school/index.html', context)

# School Registration (Wasif)
@unauthenticated_user
def schoolRegister(request):
    if request.method == "POST":
        # Get the post parameters
        fname = request.POST["school_name"]
        email = request.POST["school_email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        username = email

        # Check for errorneous inputs
        if pass1 != pass2:
            messages.error(request, 'Passwords did not match!')
            return redirect("school_register")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()

        Group.objects.get(name='school').user_set.add(myuser)
        School.objects.create(user=myuser, name=myuser.username)

        messages.success(request, "Account created, Now you can log in to your account!")
        return redirect("school_login")
    return render(request, "school/register.html")

# School Login (Wasif)
@unauthenticated_user
def schoolLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)

            return redirect("school_home")
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect("school_login")

    return render(request, "school/login.html")

# School Logout (Wasif)
def schoolLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("school_login")

# Edit/Add School Profile (Wasif)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def schoolProfileAdd(request):
    if request.method == "POST":
        # Get the post parameters
        school_head = request.POST["school_head"]
        phone_no = request.POST["phone_no"]
        students_no = request.POST["students_no"]
        email = request.POST["email"]
        school_name = request.POST["school_name"]
  

        profile = request.user.schooluserprofile.id
        s_profile = School.objects.filter(id=profile).update(hod_name=school_head, students_no=students_no, phone=phone_no, email=email, name=school_name)
        return redirect("school_profile")

    s_profile = request.user.schooluserprofile

    context = {'s_profile': s_profile, 'school_id' : request.user.schooluserprofile.id}
    return render(request, 'school/school_profile_add.html', context)

# School Profile Page (Wasif)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def schoolProfile(request):
    s_profile = request.user.schooluserprofile
    print(s_profile)
    context = {'s_profile': s_profile,}
    return render(request, 'school/school_profile.html', context)


# subject add (Ayon)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def add_subject(request):

        if request.method == "POST":
            try:
                # Get the post parameters
                subject_name = request.POST["subject_name"]
                subject_stream = request.POST["subject_stream"]

                new_subject = subjects.objects.create(
                    name = subject_name,
                    stream = subject_stream
                )

                subject_id = subject_name[0:3].upper()
                if subjects.objects.filter(subject_id= subject_id).exists():
                    subject_id = subject_name[0:3].upper() + str(new_subject.id)
                new_subject.subject_id = subject_id
                new_subject.save()
                messages.success(request, "Subject Added")
                return redirect('/school/add-subject/')
            except:
                messages.error(request, "Something went wrong")
                return redirect('/school/add-subject/')

        context = {'s_profile': School.objects.get(user=request.user),}
        return render(request, 'school/add-subject.html', context)


# subject list (Ayon)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def list_subject(request):
    context = {
        's_profile': School.objects.get(user=request.user),
        'subjects' : subjects.objects.all()
    }
    return render(request, 'school/subject-list.html', context)

@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def add_classroom(request):

        if request.method == "POST":
            try:
                # Get the post parameters
                standard = request.POST["standard"]
                section = request.POST["section"]
                school_id = request.user.schooluserprofile

                new_classroom = Classroom.objects.create(
                    standard = standard,
                    section = section,
                    school_id = school_id,
                )

                subject = request.POST.getlist('subject')
                for i in subject:
                    new_classroom.subject_list.add(subjects.objects.get(id=i))
                new_classroom.save()

                classroom_id = standard +'_'+section+str(new_classroom.id)
                new_classroom.classroom_id = classroom_id
                new_classroom.save()
                messages.success(request, "Classroom Added")
                return redirect('/school/add-class/')
            except:
                messages.error(request, "Something went wrong")
                return redirect('/school/add-class/')

        context = {'subjects': subjects.objects.all(),}
        return render(request, 'school/add-class.html', context)

@login_required(login_url='/')
def list_classroom(request):

    if request.user.groups.filter(name='school').exists():
        school = School.objects.get(user=request.user)
        schoolNavHeader = True
        classrooms = Classroom.objects.filter(school_id=school)
    else:
        school = request.user.teacherprofile.school
        teacher = teacher_profile.objects.get(user = request.user)
        classrooms = teacher.classroom.all()
        schoolNavHeader = False

    context = {
        'classroom' : classrooms,
        'schoolNavHeader' : schoolNavHeader,
    }
    return render(request, 'school/class_list.html', context)



@login_required(login_url='/')
def classroom_profile(request):
    if request.user.groups.filter(name='school').exists():
        school = School.objects.get(user=request.user)
        schoolNavHeader  = True
        isStudent = False
    elif request.user.groups.filter(name='Teachers').exists():
        school = request.user.teacherprofile.school
        schoolNavHeader = isStudent = False
    else:
        schoolNavHeader = False
        isStudent = True
        school = request.user.studentprofile.school

    if 'room_id' in request.GET and Classroom.objects.filter(classroom_id=request.GET['room_id'], school_id=school).exists():


        context = {
            'classroom' : Classroom.objects.get(classroom_id=request.GET['room_id'], school_id=school),
            'schoolNavHeader' : schoolNavHeader,
            'isStudent' : isStudent,
        }
        return render(request, 'school/classroom-profile.html', context)
    else:
        return redirect('/school/classrooms/')    