from django.urls import path,include
from rest_framework import routers
from .views import HomeViewset, ChargeViewset

router = routers.SimpleRouter()
router.register(r'',HomeViewset)

urlpatterns = [
    path('api/', include((router.urls, 'video_stream'))),
    path(r'api/<int:size>/<int:length>/<str:type>/',ChargeViewset.as_view())

]
