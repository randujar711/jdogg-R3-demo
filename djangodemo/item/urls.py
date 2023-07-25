from django.urls import path
from . import views
# When you create a urls file manually like so make sure you import it into the main urls file
app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    # we expect an integer pk which is recieved from the views/item
    ##views.detail specifies which def from detail you want to use
    path('<int:pk>/', views.detail, name='detail'), 
    path('<int:pk>/delete', views.delete, name='delete'), 
    path('<int:pk>/edit', views.edit, name='edit')
]