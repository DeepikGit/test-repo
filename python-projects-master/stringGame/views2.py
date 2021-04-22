from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')

def result(request):
    userinput=request.POST.get('text')
    cap=request.POST.get('cap')
    small=request.POST.get('small')
    punc=request.POST.get('punc')
    space=request.POST.get('space')

    if cap=='on':
        userout=userinput.upper()
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    elif small=='on':
        userout=userinput.lower()
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    elif punc=='on':
        punclist=string.punctuation
        userout = ''
        for char in userinput:
            if char not in punclist:
                userout = userout + char
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    elif space=='on':
        userout=''
        userout="".join(userinput.split())
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    else:
        return HttpResponse("Please select any Option")



