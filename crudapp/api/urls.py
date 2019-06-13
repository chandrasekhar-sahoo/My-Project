from django.conf.urls import url,include
from crudapp.api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api',views.EmployeeApiView)

urlpatterns = [
      url('',include(router.urls))
]
