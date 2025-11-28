from django.urls import path
from core import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Airport
    path('airport/create/', views.airport_create, name='airport_create'),
    path('airport/list/', views.airport_list, name='airport_list'),
    path('airport/update/<int:pk>/', views.airport_update, name='airport_update'),

    # Route
    path('route/create/', views.route_create, name='route_create'),
    path('route/list/', views.route_list, name='route_list'),
    path('route/update/<int:pk>/', views.route_update, name='route_update'),

    # Find Nth Node
    path('find-nth-node/', views.find_nth_node, name='find_nth_node'),
    
    # Longest Node
    path('longest/node/', views.longest_route_view, name='longest_node'),

    # Shortest Node
    path('shortest/node/', views.shortest_route_view, name='shortest_node'),



]
