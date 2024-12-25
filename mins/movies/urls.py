from django.urls import path
from .api.urls import urlpatterns as api_urls #getting api endpoints urls


urlpatterns = [
    #for the front-end
]

urlpatterns += api_urls #adding api endpoints to urls