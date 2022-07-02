from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainersViewSet, AbonementsViewSet, ClubsViewSet, PartnersViewSet, EquipmentsViewSet, grouptrainingViewSet, GetTrainersView
from authentication.views import AuthenticationViewSet


router = DefaultRouter()
router.register('trainers', TrainersViewSet, )
router.register('abonements', AbonementsViewSet)
router.register('clubs', ClubsViewSet)
router.register('partners', PartnersViewSet)
router.register('eqipments', EquipmentsViewSet)
router.register('grouptraining', grouptrainingViewSet)
router.register('user', AuthenticationViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/trainers/filtering', GetTrainersView.as_view()),
]
