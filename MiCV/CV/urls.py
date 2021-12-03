from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.mi_cv, name='mi_cv'),
    path('create-cv/', views.cv_create, name='cv_create'),
    path('thanks/', views.thanks, name='thanks'),
    path('cv_v2/', views.mi_cv_v2, name='mi_cv_v2'),
    path('update-cv/<int:pk>', views.cv_update, name='cv_update'),
]