"""
URL configuration for djangodemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import index, contact
from item import urls as item_urls 
from dashboard import urls as dash_urls
from conversation import urls as convo_urls
from user_payment import urls as payment_urls
urlpatterns = [
    #in the line below 'when the path is empty it will loop through all of the paths in core.urls before going to the other pathss
    path('', include('core.urls')),
    path('items/', include(item_urls)),
    path('dashboard/', include(dash_urls)),
    path('inbox/', include(convo_urls)),
    path('payment/', include(payment_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
