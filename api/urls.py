from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('survivors/', SurvivorViewList.as_view(), name='survivor-list'),
    path('survivors/<int:pk>/', SurvivorDetail.as_view(), name='survivor-detail'),
    path('monsters/', MonsterViewList.as_view(), name='monster-list'),
    path('monsters/<int:pk>/', MonsterDetail.as_view(), name='monster-detail'),
    path('users/', UserViewList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    # path('search/', SearchView.as_view(), name='search'),
]

# autetication
urlpatterns += [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
