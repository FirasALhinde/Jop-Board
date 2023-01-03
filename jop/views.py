from django.shortcuts import render,get_object_or_404
from .models import Jop
from django.core.paginator import Paginator
# Create your views here.
def jop_list(request):
    all_obj = Jop.objects.all()
    paginator = Paginator(all_obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'all_obj':page_obj}
    return render(request,'jop/jop_list.html',context)

def jop_detail(request,id):
    obj = get_object_or_404(Jop,id=id)
    return render(request,'jop/jop_detail.html',{'obj':obj})