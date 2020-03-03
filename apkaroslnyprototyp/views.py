from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from apkaroslnyprototyp.models import TradePost, TradeComment
class BaseView(View):
    def get(self, request):
        return render(request,'landing.html')

class TradeListView(View):
    def get(self, request):
        trades = TradePost.objects.filter(is_active=True)
        if request.GET.get('name') is not None:
            filtername = request.GET.get('name')
            trades = trades.filter(title__contains=filtername)
        if request.GET.get('specie') is not None:
            filterspecies = request.GET.get('specie')
            trades =trades.filter(plant_name__contains=filterspecies)
        return render(request,'tradelist.html', {'trades':trades})


class TradeView(View):
    def get(self, request, id):
        trade = TradePost.objects.get(pk=id)
        return render(request, 'trade.html', {'trade':trade})