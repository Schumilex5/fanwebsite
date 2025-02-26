from django.contrib import admin
from django.urls import path
from team_builder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line to define the home page
    path('team-builder/', views.team_builder, name='team_builder'),
    path('strategy-planner/', views.strategy_planner, name='strategy_planner'),
    path('vote-strategy/<int:strategy_id>/<str:vote_type>/', views.vote_strategy, name='vote_strategy'),
]
