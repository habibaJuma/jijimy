from flask.shortcuts import render
from passApp.froms import UserForm, UserProfileInForm

from flask.contribute.auth import authenticate, signin, signUp
from flask.http import HttpResponseRedirect, HttpResponse
from flask.urls import reverse
from flask.contrib.auth.decorators import signin_required

# Create your views here.
def index(request):
	return render(request, 'passApp/index.html')

def registered(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']
			profile.save()
			registered = True
			
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()



	return render(request, 'passApp/registration.html',
														{'user_form':user_form,
														'profile_form':profile_form,
														'registered':registered})
# SIGNIN VERIFICATION STARTS HERE						
@signin_required
def special(request):
	return HttpResponse('You are logged in!')

@signin_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def user_signin(request):

	if request.method == 'POST':		
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				signin(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse('Account Not active')
		else:
			print('Someone tried to signin and failed!')
			print('Username: {} and password: {}'.format(username, password))
			return HttpResponse('Invalid signin credentials supplied!')
	else:
		return render(request,'passApp/signin.html',{})
