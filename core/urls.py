
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.registration,name='register'),
    path('addData',views.addData,name='addData'),
    path('updateData/<int:id>',views.updateData,name='updateData'),
    path('deleteData/<int:id>',views.deleteData,name='deleteData'),


]