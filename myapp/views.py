from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    return render(request,'login.html')

def log(request):
    username = request.POST['username']
    password = request.POST['password']

    if login_table.objects.filter(username=username,password=password).exists():
        log = login_table.objects.get(username=username,password=password)
        request.session['lid'] = log.id
        if log.type == 'admin':
            return HttpResponse('''<script>alert('Admin Login Success'); window.location='admin_home'</script>''')
        elif log.type == 'coordinator':
            return HttpResponse('''<script>alert('Coordinator Login Success'); window.location='coordinator_home'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid'); window.location='/'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid'); window.location='/'</script>''')


#-----------------------------------------------------------------------------------------------------------------------

def admin_home(request):
    return render(request,'admin/admin_home.html')


def add_camp(request):
    return render(request,'admin/addcamp.html')

def add_camp_post(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    pin=request.POST['textfield3']
    post=request.POST['textfield4']
    district=request.POST['textfield5']
    contactno=request.POST['textfield6']

    ob=camp_table()
    ob.name=name
    ob.place=place
    ob.pin=pin
    ob.post=post
    ob.district=district
    ob.contactno=contactno


    ob.save()
    return HttpResponse('''<script>alert('added successfully'); window.location='/view_camp'</script>''')


def editcamp(request,id):
    ob=camp_table.objects.get(id=id)
    request.session['cid'] = id
    return render(request,'admin/editcamp.html',{'data':ob})

def editcamp_post(request):
    ob = camp_table.objects.get(id=request.session['cid'])
    ob.name = request.POST['textfield']
    ob.place = request.POST['textfield2']
    ob.pin = request.POST['textfield3']
    ob.post = request.POST['textfield4']
    ob.district = request.POST['textfield5']
    ob.contactno = request.POST['textfield6']
    ob.save()
    return HttpResponse('''<script>alert('Camp Edited Successfully'); window.location='/view_camp'</script>''')




def add_coordinator(request):
    return render(request,'admin/addcoordinator.html')


def verify_volunteer(request):
    return render(request,'admin/verify_volunteer.html')


def view_camp(request):
    ob=camp_table.objects.all()
    return render(request, 'admin/view_camp.html',{'data':ob})


def view_inventry(request):
    return render(request,'admin/view_inventry.html')

#-----------------------------------------------------------------------------------------------------------------------

def coordinator_home(request):
    return render(request,'camp_coordinator/coordinator_home.html')


def add_members(request):
    return render(request,'camp_coordinator/add_members.html')


def request_need(request):
    return render(request,'camp_coordinator/request_need.html')


def request_psychologist(request):
    return render(request,'camp_coordinator/request_psychologist.html')


def view_members(request):
    return render(request,'camp_coordinator/view_members.html')


def view_needs(request):
    return render(request,'camp_coordinator/view_needs.html')