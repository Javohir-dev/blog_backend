from django.urls import path

from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register("projects", views.ProjectsModelViewSet)

app_name = "projects"
urlpatterns = router.urls
urlpatterns += [
    path(
        "category/<int:category_id>/", views.PostsByCategory.as_view(), name="category"
    ),
]
