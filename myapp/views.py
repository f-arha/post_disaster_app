from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q

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

def view_coordinator(request):
    return render(request,'admin/view_coordinator.html')

def add_coordinator(request):
    return render(request,'admin/addcoordinator.html')

def add_coordinator_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    image = request.POST['image']


    ob = camp_co_table()
    ob.name = name
    ob.email = email
    ob.phone = phone
    ob.image = image
    ob.LOGIN_id = login_table.objects.get(id=request.session['id'])
    ob.save()
    return HttpResponse('''<script>alert('Coordinator added Successfully'); window.location='/view_coordinator'</script>''')



def verify_volunteer(request):
    vol = volunteer.objects.all()
    return render(request,'admin/verify_volunteer.html',{'data':vol})

def accept(request,id):
    acc = login_table.objects.get(id=id)
    acc.type = 'volunteer'
    acc.save()
    return HttpResponse('''<script>alert('Accepted'); window.location='/verify_volunteer'</script>''')

def reject(request,id):
    rej = login_table.objects.get(id=id)
    rej.delete()
    return HttpResponse('''<script>alert('Deleted'); window.location='/verify_volunteer'</script>''')

def verify(request,id):
    veri = donate.objects.get(id=id)
    veri.status = 'verified'
    veri.save()
    return HttpResponse('''<script>alert('Verified'); window.location='/view_inventry'</script>''')

def view_camp(request):
    ob=camp_table.objects.all()
    return render(request, 'admin/view_camp.html',{'data':ob})

def deletecamp(request,id):
    cam = camp_table.objects.get(id=id)
    cam.delete()
    return HttpResponse('''<script>alert('Camp Deleted Successfully'); window.location='/view_camp'</script>''')


def view_inventry(request):
    inv = donate.objects.all()
    return render(request, 'admin/view_inventry.html', {'data': inv})

#-----------------------------------------------------------------------------------------------------------------------

def coordinator_home(request):
    return render(request,'camp_coordinator/coordinator_home.html')


def add_members(request):
    return render(request,'camp_coordinator/add_members.html')


def add_members_post(request):
    name=request.POST['textfield']
    image=request.POST['textfield2']
    place=request.POST['textfield3']
    pin=request.POST['textfield4']
    post=request.POST['textfield5']
    phone=request.POST['textfield6']
    gender=request.POST['textfield7']
    age=request.POST['textfield8']

    ob = member_table()
    ob.name=name
    ob.image=image
    ob.place=place
    ob.pin=pin
    ob.post=post
    ob.phone=phone
    ob.gender=gender
    ob.age=age
    ob.save()
    return HttpResponse('''<script>alert('added successfully'); window.location='/view_members'</script>''')

def deletemembers(request,id):
    mem = member_table.objects.get(id=id)
    mem.delete()
    return HttpResponse('''<script>alert('Member Deleted Successfully'); window.location='/view_members'</script>''')


def editmembers(request,id):
    ob=member_table.objects.get(id=id)
    request.session['mid'] = id
    return render(request,'camp_coordinator/editmembers.html',{'data':ob})


def editmembers_post(request):
    ob = member_table.objects.get(id=request.session['mid'])
    ob.name = request.POST['textfield']
    ob.image = request.POST['textfield2']
    ob.place = request.POST['textfield3']
    ob.pin = request.POST['textfield4']
    ob.post = request.POST['textfield5']
    ob.phone = request.POST['textfield6']
    ob.gender = request.POST['textfield7']
    ob.age = request.POST['textfield8']
    ob.save()
    return HttpResponse('''<script>alert('Member Details Edited Successfully'); window.location='/view_members'</script>''')

def request_need(request):
    return render(request,'camp_coordinator/request_need.html')

def request_need_post(request):
    type=request.POST['type']
    needs=request.POST['need']
    quantity=request.POST['quantity']

    ob=need()
    ob.type=type
    ob.needs=needs
    ob.quantity=quantity
    ob.COORDID=camp_co_table.objects.get(LOGIN_id=request.session['lid'])
    import datetime
    ob.date = datetime.datetime.today().date()
    ob.status='pending'
    ob.save()
    return HttpResponse('''<script>alert('Need Requested Successfully'); window.location='/coordinator_home'</script>''')


def request_psychologist_load(request):
    return render(request,'camp_coordinator/request_psychologist.html')


def request_psychologist_post(request):
    description=request.POST['description']

    ob = request_psychologist()
    import datetime
    ob.date = datetime.datetime.today().date()
    ob.COORDID=camp_co_table.objects.get(LOGIN=request.session["lid"])
    ob.status = 'pending'
    ob.description=description
    ob.save()
    return HttpResponse( '''<script>alert('Psychologist Requested Successfully'); window.location='/coordinator_home'</script>''')

def view_psychologist_request(request):
    ob=request_psychologist.objects.filter(COORDID__LOGIN=request.session["lid"])
    return render(request,'camp_coordinator/view_psychologist.html',{'val':ob})


def view_members(request):
    ob=member_table.objects.all()
    return render(request, 'camp_coordinator/view_members.html', {'data':ob})


def view_needs(request):
    ob=donate.objects.filter(~Q(status = 'pending'),NEEDID__COORDID__LOGIN_id=request.session['lid']  )
    return render(request, 'camp_coordinator/view_needs.html', {'val':ob})

def need_accept(request,id):
    request.session['did']=id
    acc = donate.objects.get(id=id)
    acc.status = 'accepted'
    acc.save()
    return HttpResponse('''<script>alert('Accepted'); window.location='/view_needs'</script>''')

def need_reject(request,id):
    request.session['did'] = id
    rej = donate.objects.get(id=id)
    rej.status = 'rejected'
    rej.save()
    return HttpResponse('''<script>alert('Rejected'); window.location='/view_needs'</script>''')
