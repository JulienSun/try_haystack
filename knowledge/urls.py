from django.urls import path, include
from haystack.generic_views import SearchView

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", views.ArticleSearchView, basename="search1111")

urlpatterns = [
    path("search/v1/", include(router.urls)),
    path("search/", views.MySearchView.as_view(), name="search_view"),
    # path("search/", include("haystack.urls")),
]
