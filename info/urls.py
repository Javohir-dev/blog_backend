from django.urls import path

from rest_framework.routers import DefaultRouter

from info import views

router = DefaultRouter()
# router.register("", views.MyInfoModelViewSet)

app_name = "info"
urlpatterns = router.urls
urlpatterns += [
    path("info/", views.MyInfoView.as_view(), name="info"),
    path("info/lc/", views.MyInfoListCreateView.as_view(), name="info_list_create"),
    path("cv/", views.CVAPIView.as_view(), name="cv"),
    path("cv/lc/", views.CVListCreateView.as_view(), name="cv_list_create"),
]
