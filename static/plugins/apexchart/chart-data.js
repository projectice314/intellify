


'use strict';

$(document).ready(function() {

	// chart-student-graph
	if ($('#chart-student-graph').length > 0) {
		var options = {
			chart: {
				height: 350,
				type: "area",
				toolbar: {
					show: true
				},
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: "smooth"
			},
			series: [{
				name: "BEN",
				color: '#D33F49',
				data: [45, 40, 75, 51, 42, 42, ]
			}, 
			{
				name: "ENG.",
				color: '#A69888',
				data: [31, 48, 78, 32, 44, 52, ]
			}, 
			{
				name: "MATH",
				color: '#77BA99',
				data: [33, 44, 70, 39, 50, 51, ]
			}, 
			{
				name: "HIS",
				color: '#EFF0D1',
				data: [31, 80, 40, 54, 34, 54, ]
			}, 
			{
				name: "GEO",
				color: '#334E58',
				data: [31, 60, 57, 42, 60, 85, ]
			}, 
			{
				name: "COMP",
				color: 'violet',
				data: [31, 52, 69, 32, 44, 90, ]
			}],
			xaxis: {
				categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',],
			}
		}
		var chartStudent = new ApexCharts(
			document.querySelector("#chart-student-graph"),
			options
		);
		chartStudent.render();

	}

	if ($('#chart-student-graph-bar').length > 0) {
		var optionsBarStu = {
			chart: {
				type: 'bar',
				height: 350,
				width: '100%',
				stacked: true,
				toolbar: {
					show: false
				},
			},
			dataLabels: {
				enabled: false
			},
			plotOptions: {
				bar: {
					columnWidth: '45%',
				}
			},
			series: [{
				name: "Class Avg.",
				color: '#D7F2BA',
				data: [45, 40, 75, 51, 42, 42, ],
			}, {
				name: "Your Avg.",
				color: '#FFBC53',
				data: [31, 48, 78, 32, 44, 52, ],
			}],
			labels: ['Ben', 'Eng', 'His', 'Mat', 'Geo', 'Com',],
			xaxis: {
				labels: {
					show: true
				},
				axisBorder: {
					show: false
				},
				axisTicks: {
					show: false
				},
			},
			yaxis: {
				axisBorder: {
					show: false
				},
				axisTicks: {
					show: false
				},
				labels: {
					style: {
						colors: '#777'
					}
				}
			},
			title: {
				text: '',
				align: 'left',
				style: {
					fontSize: '18px'
				}
			}
	
		}
		var chartStudentBar = new ApexCharts(document.querySelector("#chart-student-graph-bar"),optionsBarStu);
		chartStudentBar.render();

	}



	// Area chart
	
	if ($('#apexcharts-area').length > 0) {
		var options = {
			chart: {
				height: 350,
				type: "area",
				toolbar: {
					show: false
				},
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: "smooth"
			},
			series: [{
				name: "Teachers",
				data: [45, 60, 75, 51, 42, 42, 30]
			}, {
				name: "Students",
				color: '#FFBC53',
				data: [24, 48, 56, 32, 34, 52, 25]
			}],
			xaxis: {
				categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
			}
		}
		var chart = new ApexCharts(
			document.querySelector("#apexcharts-area"),
			options
		);
		chart.render();
	}

	// Bar chart
	
	if ($('#bar').length > 0) {
	var optionsBar = {
		chart: {
			type: 'bar',
			height: 350,
			width: '100%',
			stacked: true,
			toolbar: {
				show: false
			},
		},
		dataLabels: {
			enabled: false
		},
		plotOptions: {
			bar: {
				columnWidth: '45%',
			}
		},
		series: [{
			name: "Boys",
			color: '#fdbb38',
			data: [420, 532, 516, 575, 519, 517, 454, 392, 262, 383, 446, 551, 563, 421, 563, 254, 452],
		}, {
			name: "Girls",
			color: '#19affb',
			data: [336, 612, 344, 647, 345, 563, 256, 344, 323, 300, 455, 456, 526, 652, 325, 425, 436],
		}],
		labels: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
		xaxis: {
			labels: {
				show: false
			},
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false
			},
		},
		yaxis: {
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false
			},
			labels: {
				style: {
					colors: '#777'
				}
			}
		},
		title: {
			text: '',
			align: 'left',
			style: {
				fontSize: '18px'
			}
		}

	}
  
	var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
	chartBar.render();
	}
  
});