from django.contrib.auth import authenticate,login
from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        
        # authenticate user 
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            context={
                'error':'Invalid Username or Password'
            }
            print(context)
            render(request, 'accounts/login.html',context={'error':'hehh'})
        
    return render(request, 'accounts/login.html')

# Create your views here.
def logou_view(request):
    
    return render(request, 'accounts/login.html')

# Create your views here.
def register_view(request):

    return render(request, 'accounts/login.html')