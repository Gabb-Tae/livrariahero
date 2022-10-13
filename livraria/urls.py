from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editora', EditoraViewSet)
router.register(r'autor', AutorViewSet)
router.register(r'livro', LivroViewSet)



urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
