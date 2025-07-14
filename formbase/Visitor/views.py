from http.client import HTTPResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Visitor

from .forms import VisitorForm
# Create your views here.
def visitor_form_view(request):
    if request.method=='POST':
        form=VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor-list') #here
    else:
        form=VisitorForm()
        return render(request,'welcome/form.html',{'form':form})


def visitor_list_view(request):
    visitors=Visitor.objects.all()
    return render(request,'welcome/visitor_list.html',{'visitors':visitors})

def visitor_edit_view(request,id):
    visitor = get_object_or_404(Visitor,id=id)
    if request.method == 'POST':
        form=VisitorForm(request.POST,instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitor-list')
    else:
        form=VisitorForm(instance=visitor)
        return render(request,'welcome/form.html',context={'form':form,'edit':True})


def visitor_delete_view(request,id):
    visitor = get_object_or_404(Visitor,id=id)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitor-list')
    else:
        form=VisitorForm(instance=visitor)
        return render(request,'welcome/visitor_delete.html',context={'form':form,'delete':True})