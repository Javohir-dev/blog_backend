from django.urls import path

from rest_framework.routers import DefaultRouter

from edu import views

router = DefaultRouter()
router.register("edu", views.EDUModelViewSet)

app_name = "edu"
urlpatterns = router.urls
urlpatterns += [
    # path("edu/", views.MyInfoView.as_view(), name="edu"),
]
