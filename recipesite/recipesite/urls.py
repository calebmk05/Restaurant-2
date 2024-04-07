from django.urls import path, include
from users import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns= [
    path('register/', user_views.register, name="users-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name="users-logout"),
    path('profile/', user_views.profile, name="users-profile"),
    path('', include('recipe.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)