from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

# from backend.views import

DataRouter = DefaultRouter()

app_name = 'expdata'

# DataRouter.register(r'ds_datasubmittedinfo', DataSubmittedInfoViewSet, base_name='ds_datasubmittedinfo')

# DataRouter.register(r'ds_datasubmittedfileInfo', DataSubmittedFileInfoViewSet, base_name='ds_datasubmittedfileInfo')

# DataRouter.register(r'ds_meteoritefield', MeteoriteFieldViewSet, base_name='ds_meteoritefield')

# DataRouter.register(r'ds_meteoritetype', MeteoriteTypeViewSet, base_name='ds_meteoritetype')


urlpatterns = [
    url(r'^', include(DataRouter.urls)),
]