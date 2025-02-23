from rest_framework.routers import SimpleRouter

from user import views

router = SimpleRouter(trailing_slash=True)

router.register("users", views.UserViewSet, basename="users")

urlpatterns = router.urls
