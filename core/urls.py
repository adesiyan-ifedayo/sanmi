from core import views
from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static



app_name='core'

urlpatterns = [
	path('', views.home, name='home'),
	path('blog/', views.blog, name='blog'),
	path('gallery/', views.gallery, name='gallery'),
	path('contact/', views.contact, name='contact'),
	path('about_me/', views.about_me, name='about-me'),
	path('blog/<str:slug>/', views.post_detail_view, name='post-detail'),

	#path('<id>/comment-delete/', views.comment_delete_view, name='comment-delete'),
	
	]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	