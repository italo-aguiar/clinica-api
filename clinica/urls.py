# urls.py principal
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pacientes.views import PacienteViewSet
from agendamentos.views import AgendamentoViewSet
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'agendamentos', AgendamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

