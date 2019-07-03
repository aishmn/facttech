from django.urls import path
from .views import PostListView, PostDetailView
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('<int:id>/', PostDetailView.as_view(), name='detail')
]
