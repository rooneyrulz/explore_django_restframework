from rest_framework import routers
from .views import PostViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/posts', PostViewset, 'posts')

urlpatterns = router.urls
