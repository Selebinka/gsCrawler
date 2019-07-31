from django.contrib import admin
from django.urls import path, include
from main.views import search_result, crawl_run, manager_spider


urlpatterns = [
    path('result/', crawl_run, name='crawl_run'),
    path('results/', search_result, name='search_result'),
    path('', manager_spider, name='manager_spider'),

]
