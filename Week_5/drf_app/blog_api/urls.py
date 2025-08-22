# blog_api/urls.py
from django.contrib import admin
from django.urls import path, include
from blog.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Blog API
    path('api/v1/blog/', include('blog.urls')),

    # E-commerce API
    path('api/v1/ecommerce/', include('ecommerce.urls')),
    path('api/v1/auth/register/',RegisterView.as_view(), name='register'),

    # Auth with JWT
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
