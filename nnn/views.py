from django.shortcuts import render, render_to_response,HttpResponse 
from nnn.models import Details

# def functionname(request):
# 	return render(request,'signup.html')


def signup(request):
	return render(request,'registration.html')


def function(request):

	obj=Details(
		name=request.POST.get('uname'),
		surname=request.POST.get('sname'),
		address=request.POST.get('add'),
		phoneno=request.POST.get('number'),
		emailid=request.POST.get('email')
		)
	obj.save()
	return render(request,'signup.html')
	# obj=Details(
	# 	name = request.POST.get('uname'),
	# 	surname = request.POST.get('sname'),
	# 	address = request.POST.get('add'),
	# 	phoneno = request.POST.get('number'),
	# 	emailid = request.POST.get('email'))
	# obj.save()
	# return render(request,'signup.html')


def show(request):
	obj = Details.objects.all()
	return render(request, 'show.html', {'obj':obj})
# def function(request):
# 	username=request.POST.get('uname')
# 	surname=request.POST.get('sname')
# 	address=request.POST.get('add')
# 	phone=request.POST.get('number')
# 	email=request.POST.get('email')
# 	obj=Details(
# 		name = username,
# 		surname = surname,
# 		address= address,
# 		phoneno= phone,
# 		emailid= email)
# 	obj.save()
# 	# return render(request,'signup.html')
# 	return HttpResponse("anil")

def hello(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)



