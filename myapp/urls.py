from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [

    path('',views.main),
    path('log',views.log),


    path('admin_home', views.admin_home),
    path('add_camp', views.add_camp),
    path('add_camp_post', views.add_camp_post),
    path('editcamp/<int:id>', views.editcamp),
    path('deletecamp/<int:id>', views.deletecamp),
    path('editcamp_post', views.editcamp_post),
    path('add_coordinator', views.add_coordinator),
    path('add_coordinator_post', views.add_coordinator_post),
    path('verify_volunteer', views.verify_volunteer),
    path('accept/<id>', views.accept),
    path('reject/<id>', views.reject),
    path('verify/<id>', views.verify),
    path('view_camp', views.view_camp),
    path('view_inventry', views.view_inventry),
    path('view_coordinator', views.view_coordinator),

    path('coordinator_home', views.coordinator_home),
    path('add_members', views.add_members),
    path('add_members_post', views.add_members_post),
    path('deletemembers/<int:id>', views.deletemembers),
    path('editmembers/<int:id>', views.editmembers),
    path('editmembers_post', views.editmembers_post),
    path('request_need', views.request_need),
    path('request_need_post', views.request_need_post),
    path('request_psychologist', views.request_psychologist_load),
    path('request_psychologist_post', views.request_psychologist_post),
    path('view_psychologist_request', views.view_psychologist_request),
    path('view_members', views.view_members),
    path('view_needs', views.view_needs),
    path('need_accept/<id>', views.need_accept),
    path('need_reject/<id>', views.need_reject),

]
