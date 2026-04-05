"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ##Va a responder la app bases url
    path('', include(('bases.urls', 'bases'), namespace='bases')),
    ##Cuando se ponga inv en el nav automaticamente va a redirigir al archivo url de inv que esta en la app inv, dentro de ese archivo dependiendo de 
    ##las rutas que pondremos ahi podremos aaccder a esas rutas ejemplo: inv/categorias/
    path('inv/', include(('inv.urls', 'inv'), namespace='inv')),
    path('admin/', admin.site.urls),
]
