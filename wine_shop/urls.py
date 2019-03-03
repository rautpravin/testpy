from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register(r'country',CountryViewSet)
router.register(r'state', StateViewSet)
router.register(r'city', CityViewSet)

urlpatterns = router.urls
