"""roslinyapka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apkaroslnyprototyp.views import *
from roslinyapka import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',BaseView.as_view()),
    path('offers/', TradeListView.as_view()),
    path('trade/', TradeView.as_view(), name='Trade'),
    path('trade/<int:id>', ShowTrade.as_view()),
    path('accounts/', include('accounts.urls')),
    path('guide/<int:id>/', ShowGuide.as_view()),
    path('guide/', GuideView.as_view()),
    path('guides/', GuideListView.as_view()),
    path('profile/<int:id>', UserProfile.as_view()),
    path('searchuser/',SearchUser.as_view() ),
    path('test/', test.as_view()),
    path('api/tradepost/', csrf_exempt(TradeVote.as_view())),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
