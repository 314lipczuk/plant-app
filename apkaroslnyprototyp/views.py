from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from apkaroslnyprototyp.models import TradePost, TradeComment, Guide, GuideComment, Profile
from apkaroslnyprototyp.forms import TradeForm, GuideForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseView(View):
    def get(self, request):
        return render(request,'landing.html')


class Onlyloggedin(LoginRequiredMixin, View):
    login_url = 'registration/login/'
    redirect_field_name = '/trade/'

class TradeView(LoginRequiredMixin,View):
    redirect_field_name = '/'
    login_url = '/'

    def get(self, request):
        form = TradeForm()
        return render(request, 'add.html' , {'form':form})

    def post(self, request):
        new_trade = TradeForm(request.POST)
        if new_trade.is_valid():
            id = new_trade.cleaned_data['title']
            new_trade.save()
            tp=TradePost.objects.get(title=id)
            p=Profile.objects.get(user_id = request.POST.get('creator'))
            tp.creator = p
            tp.save()
            return HttpResponse("yes")



class ShowTrade(View):
    def get(self, request, id):
        trade = TradePost.objects.get(pk=id)
        return render(request, 'trade.html', {'trade':trade})

class GuideView(LoginRequiredMixin, View):
    redirect_field_name = '/'
    login_url = '/'
    def get(self, request):
        form = GuideForm
        return render(request,'add.html', {'form':form})
    def post(self, request):
        form = GuideForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data['title']
            form.save()
            guid = Guide.objects.get(title=id)
            p = Profile.objects.get(user_id = request.POST.get('creator'))
            guid.creator = p
            guid.save()
            return redirect('/')

class ShowGuide(View):
    def get(self, request, id):
        guide = Guide.objects.get(pk=id)
        guidecom = GuideComment.objects.filter(guide_id=id)
        return render(request, 'guide.html', {'guide':guide, 'comments':guidecom})

class GuideListView(View):
    def get(self, request):
        guides = Guide.objects.order_by('?')
        if request.GET.get('name') is not None:
            filtername = request.GET.get('name')
            guides = guides.filter(title__contains=filtername)
        if request.GET.get('sort') is not None:
            sort=request.GET.get('sort')
            if sort == 'mostpoints':
                guides=guides.order_by('-points')
            elif sort == 'newest':
                guides = guides.order_by('add_date')
        return render(request, 'guidelist.html', {'guides':guides})
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



class UserProfile(View):
    def get(self, request, id):
        profile=Profile.objects.get(pk = id)
        return render(request, 'profile.html', {'profile':profile})

