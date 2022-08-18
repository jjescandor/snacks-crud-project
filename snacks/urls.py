from django.urls import path
from .views import SnackListView, SnackCreateView, SnackDeleteView, SnackDetailView, SnackUpdateView

urlpatterns = [
    path('', SnackListView.as_view(), name='list_snack'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail_snack'),
    path('create/', SnackCreateView.as_view(), name='create_snack'),
    path('<int:pk>/update', SnackUpdateView.as_view(), name='update_snack'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='delete_snack'),
]