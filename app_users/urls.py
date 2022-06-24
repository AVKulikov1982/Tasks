from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import UserLoginView, UserLogoutView, UpdateProfileView, register, profile

urlpatterns = [
	path('login', UserLoginView.as_view(), name='login'),
	path('logout', UserLogoutView.as_view(), name='logout'),
	path('registration', register, name='registration'),
	path('profile/<int:user_id>', profile, name='profile'),
	path('profile/update/<int:user_id>', UpdateProfileView.as_view(), name='profile_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)