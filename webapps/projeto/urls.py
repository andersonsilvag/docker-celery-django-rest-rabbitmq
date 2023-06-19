from django.contrib import admin  # Importa o módulo 'admin' do Django para a área de administração
from django.urls import path, include  # Importa as funções 'path' e 'include' do módulo 'urls' do Django
from django.conf.urls.static import static  # Importa a função 'static' do módulo 'urls' do Django para servir arquivos estáticos
from django.conf import settings  # Importa as configurações do projeto Django
from django.views.generic import TemplateView  # Importa a classe 'TemplateView' do módulo 'views' do Django

urlpatterns = [
    path('admin/', admin.site.urls),  # Define a URL '/admin/' para a área de administração do Django
    path('api/', include('apps.api.urls', namespace='api')),  # Define a URL '/api/' para incluir as URLs da aplicação 'api' com o namespace 'api'
    path('emprestimo/', include('apps.emprestimo.urls', namespace='emprestimo')),  # Define a URL '/emprestimo/' para incluir as URLs da aplicação 'emprestimo' com o namespace 'emprestimo'
    path('', TemplateView.as_view(template_name='enviar_proposta.html'), name='enviar_proposta'),  # Define a URL raiz ('/') para exibir o template 'enviar_proposta.html' usando a classe 'TemplateView' e com o nome 'enviar_proposta'
]

# Serve arquivos de mídia a partir do MEDIA_ROOT. Isso só funcionará quando DEBUG=True estiver configurado.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adiciona as URLs para servir arquivos de mídia quando DEBUG=True, utilizando as configurações do Django

if settings.DEBUG:  # Use local only
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]