from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        
        # authenticate user 
        user = authenticate(request, username=username, password=password)
        
        print(user)
        if user is None:
            context={
                'error':'Invalid Username or Password'
            }
            return render(request, 'accounts/login.html',context=context)
        
        login(request,user)
        return redirect('/')
    return render(request, 'accounts/login.html',{})

# Create your views here.
def logou_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
        
    return render(request, 'accounts/logout.html')

# Create your views here.
def register_view(request):

    return render(request, 'accounts/login.html')