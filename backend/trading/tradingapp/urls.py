from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^getallrecordbydate/(?P<date>\d{4}-\d{2}-\d{2})$',views.GetAllRecordbyDateApi),

]