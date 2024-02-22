from django.urls import path
from . import views
from .views import QarindoshDetail,JinoyatchiDetail
urlpatterns = [
    path('', views.home, name='home'),
    path('hudud/<int:hudud_id>/', views.fuqoro, name='fuqoro'),
    path('detail/<int:fuqoro_id>/', views.detail, name='detail'),
    path('qarindosh/<int:pk>/', QarindoshDetail.as_view(), name='qarindosh_detail'),
    path('jinoyatchi/<int:pk>/', JinoyatchiDetail.as_view(), name='jinoyatchi'),
    path('search/', views.search_fuqoro, name='search_fuqoro'),
    path('check-time/', views.check_time, name='check_time'),
]