from django.shortcuts import render,HttpResponseRedirect
from .forms import formsdata
from .models import modeldata
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=formsdata(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pd=fm.cleaned_data['password']
            var=modeldata(name=nm,email=em,password=pd)
            var.save()
    else:
        fm=formsdata()
    stud=modeldata.objects.all()
    return render(request,'testapp/add&show.html',{'form':fm,'stu':stud})

def delete_show(request,id):
    if request.method=='POST':
        pi=modeldata.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_show(request,id):
    if request.method=='POST':
        pi=modeldata.objects.get(pk=id)
        fm=formsdata(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=modeldata.objects.get(pk=id)
        fm=formsdata(instance=pi)
    
    return render(request,'testapp/update.html',{'form':fm})