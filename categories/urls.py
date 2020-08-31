from django.contrib import admin
from django.urls import path
from blog.views import ItemsByCategoryView, CategoryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CategoryListView.as_view() , name='category-list'),
    path('<str:slug>/', ItemsByCategoryView.as_view() , name='items-by-category'),
    ]
