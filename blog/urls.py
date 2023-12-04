from django.urls import path

from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()
router.register("blog", views.BlogModelViewSet)

app_name = "blog"
urlpatterns = router.urls
urlpatterns += [
    path("blogs/", views.BlogListCreateAPIView.as_view(), name="blogs"),
]
