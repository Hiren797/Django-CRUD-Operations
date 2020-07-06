from django.shortcuts import render , redirect
from .forms import empform
from .models import employee


def emp_list(request):
    context = {'emp_list': employee.objects.all()}
    return render(request , "curdapp/emp_list.html" , context)


def emp_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form=empform()
        else:
            employe=employee.objects.get(pk=id)
            form=empform(instance=employe)
        return render(request , "curdapp/emp_form.html" , {'form': form})
    else:
        if id == 0:
            form = empform(request.POST)
        else:
            employe = employee.objects.get(pk=id)
            form = empform(request.POST , instance=employe)
        if form.is_valid():
            form.save()
        return redirect('/emp/list')



def emp_delete(request,id):
    employe= employee.objects.get(pk=id)
    employe.delete()
    return redirect('/emp/list')

