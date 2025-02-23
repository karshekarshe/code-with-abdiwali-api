from rest_framework.routers import SimpleRouter

from blog import views

router = SimpleRouter(trailing_slash=True)

router.register("categories", views.CategoryViewSet, basename="categories")
router.register("articles", views.ArticleViewSet, basename="articles")
router.register("tags", views.TagViewSet, basename="tags")

urlpatterns = router.urls
