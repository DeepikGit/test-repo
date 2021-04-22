from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')

def result(request):
    userinput=request.POST.get('text')
    opt=request.POST.get('opt')
    cap=request.POST.get('cap')
    small=request.POST.get('small')
    punc=request.POST.get('punc')
    space=request.POST.get('space')

    if opt=='1':
        userout=userinput.upper()
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    elif opt=='2':
        userout=userinput.lower()
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    elif opt=='3':
        punclist=string.punctuation
        userout = ''
        for char in userinput:
            if char not in punclist:
                userout = userout + char
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    elif opt=='4':
        userout=''
        userout="".join(userinput.split())
        return render(request,'result.html',{'userinput':userinput,'userout':userout})
    elif opt=='5':
        userout=''
        userout=userinput[::-1]
        return render(request, 'result.html', {'userinput': userinput, 'userout': userout})
    else:
        return render(request,'error.html')



