from django.urls import path
from django.urls.resolvers import URLPattern
from app.views import todo_list, todo_detail_change_and_delete
urlpatterns = [
    path('', todo_list),
    path('<int:pk>/', todo_detail_change_and_delete),
]
