from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('header', views.introductionView, name='introduction'),
    path('main_img', views.main_img, name='main_img'),
    path('logo', views.nav, name='nav'),
    path('download_cv', views.download_cv, name='download_cv'),
    path('contact', views.contact_form, name='contact'),
    path('footer', views.footer, name='footer'),

]
    