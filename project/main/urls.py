from django.urls import path

from .views import USDRUBView


urlpatterns = [path("get-current-usd", USDRUBView.as_view())]
