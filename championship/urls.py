from django.urls import path, include
from rest_framework import routers
from championship import views

router = routers.DefaultRouter()
router.register(r'editions', views.EditionViewSet, 'editions')
router.register(r'phases', views.PhaseViewSet, 'phases')
router.register(r'groups', views.GroupViewSet, 'groups')
router.register(r'teams', views.TeamViewSet, 'teams')

urlpatterns = [
    path('api/', include(router.urls)),
]
