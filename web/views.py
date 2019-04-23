from django.shortcuts import render
from web import  models
# Create your views here.
def moviename(request):
    mov_list=models.Movie.objects.all()
    print(mov_list)
    context={
        'mov_list':mov_list
    }
    return render(request,'index.html',context=context)

def find(request):
    return render(request,'choose.html')



def phone(request):
    phone_list=models.Phoneprice.objects.all()
    print(phone_list)
    context1={
        'phone_list':phone_list
    }
    return render(request,'phone.html',context=context1)