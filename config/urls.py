from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jogos.views import JogoViewSet

# (Lacuna 10): Cria o "roteador", que é a ferramenta do DRF que gera as URLs automaticamente.
router = DefaultRouter()

# (Lacuna 11): Registamos a nossa view no roteador com o prefixo 'jogos'.
router.register('jogos', JogoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # (Lacuna 12): Incluímos todas as rotas geradas pelo router debaixo do caminho base 'api/'.
    path('api/', include(router.urls)),
]