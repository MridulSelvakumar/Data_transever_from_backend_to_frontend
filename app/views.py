from django.shortcuts import render

# Create your views here.
def data_render(request):
    data="this is the data from backend to frontend"
    d={'dataa':data}
    return render(request,'data.html',context=d)
def login(request):
    data1="mridul"
    m={'user':data1,'age':21}
    return render(request,'login.html',context=m)
