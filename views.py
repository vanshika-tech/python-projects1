from django.shortcuts import render
from .models import *
#from django.http import *
from django.db.models import Q
def hi(request):

    return render(request,'DEMOAPP/hi.html')

def add(request):

    desig=request.GET['desig']
    office=request.GET['office']
    fname = request.GET['fname']
    sname=request.GET['sname']


    if desig:
        if office:
            if fname:
                if sname:
                    match = employee.objects.filter(Q(fname__icontains=fname)|
                                                   Q(sname__icontains=sname)|
                                                   Q(desig__icontains=desig)|
                                                   Q(office__icontains=office))
                    if match:
                        return render(request,'DEMOAPP/result.html', {'obj': match})
                    else:
                        return render(request, 'DEMOAPP/result2.html')
                else:
                    match = employee.objects.filter(Q(desig__icontains=desig)|
                                                   Q(office__icontains=office)|
                                                   Q(fname__icontains=fname))
                    if match:
                        return render(request, 'DEMOAPP/result.html', {'obj': match})
                    else:
                        return render(request, 'DEMOAPP/result2.html')
            else:
                match = employee.objects.filter(Q(desig__icontains=desig) |
                                               Q(office__icontains=office))
                if match:
                    return render(request, 'DEMOAPP/result.html', {'obj': match})
                else:
                    return render(request, 'DEMOAPP/result2.html')
        else:
            match= employee.objects.filter(Q(desig__icontains=desig))
            if match:
                return render(request, 'DEMOAPP/result.html', {'obj': match})
            else:
                return render(request, 'DEMOAPP/result2.html')
    else:
        return render(request,'DEMOAPP/hi.html')
    return render(request,'DEMOAPP/hi.html')




