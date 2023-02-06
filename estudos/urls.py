from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', include('accounts.urls')),
    path('index/', include('website.urls')),
    path('topicos/', include('topicos.urls')),
    path('cursos/', include('cursos.urls')),
    path('videos/', include('videos.urls')),
    path('forum/', include('forum.urls')),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="password/password_change_done.html"), name='password_change_done'),
    path('validate/<username>/', views.registerValidate, name='validate'),
    path('email_change/', views.emailChange, name='email_change'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

