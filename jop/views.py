from django.shortcuts import render,get_object_or_404,redirect
from .models import Jop
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import ApplyForm,JopForm
# Create your views here.
def jop_list(request):
    all_obj = Jop.objects.all()
    paginator = Paginator(all_obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'all_obj':page_obj}
    return render(request,'jop/jop_list.html',context)

def jop_detail(request,slug):
    obj = get_object_or_404(Jop,slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.jop = obj
            myform.save()
    else:
        form = ApplyForm()
    return render(request,'jop/jop_detail.html',{'obj':obj,'form':form})

def add_jop(request):
    if request.method == 'POST':
        form = JopForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jop:jop_list'))
    else:   
        form = JopForm()

    return render(request,'jop/add_jop.html',{'form':form})