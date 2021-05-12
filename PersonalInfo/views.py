from django.shortcuts import render ,get_object_or_404
from .models import Jobs

def home(request):
    job=Jobs.objects
    return render(request,'Personalinfo/home.html',{'Jobs':job})


def detail(request,Jobs_id):
    Jobs_detail=get_object_or_404(Jobs,pk=Jobs_id)

    return render(request,'Personalinfo/detail.html',{'Jobs':Jobs_detail})
