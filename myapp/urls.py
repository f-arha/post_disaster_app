from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [

    path('',views.main),
    path('log',views.log),
    path('add_camp_post',views.add_camp_post),

    path('admin_home',views.admin_home),
    path('add_camp',views.add_camp),
    path('editcamp/<int:id>',views.editcamp),
    path('editcamp_post',views.editcamp_post),
    path('add_coordinator',views.add_coordinator),
    path('verify_volunteer',views.verify_volunteer),
    path('view_camp',views.view_camp),
    path('view_inventry',views.view_inventry),

    path('coordinator_home',views.coordinator_home),
    path('add_members',views.add_members),
    path('request_need',views.request_need),
    path('request_psychologist',views.request_psychologist),
    path('view_members',views.view_members),
    path('view_needs',views.view_needs),

]
