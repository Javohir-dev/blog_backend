from django.urls import path

from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register("projects", views.ProjectsModelViewSet)
router.register("category", views.CategoryModelViewSet)

app_name = "projects"
urlpatterns = router.urls
urlpatterns += [
    path(
        "by-category/<int:category_id>/",
        views.PostsByCategory.as_view(),
        name="by_category",
    ),
]
