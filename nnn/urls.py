from django.conf.urls import url
from nnn import views

urlpatterns = [

	# url(r'^acd/',views.functionname,name='functionname'),
	url(r'^signup/', views.signup,name='signup'),
	url(r'^function/', views.function,name='function'),
	url(r'^show/', views.show,name='show'),
	# url(r'^number/(\d+)/',views.hello, name = 'hello'),

]