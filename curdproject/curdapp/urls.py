
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.emp_form,name='emp_insert'),
    path('<int:id>/' , views.emp_form , name='emp_update'),
    path('delete/<int:id>/' , views.emp_delete , name='emp_delete') ,
    path('list/',views.emp_list,name='emp_list')]
