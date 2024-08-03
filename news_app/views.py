from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request,news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news':news
    }
    return render(request, 'news/news_detail.html', context)

# def homepageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:5]
#     local_one = News.published.filter(category__name = 'Mahalliy').order_by('-publish_time')[:1]
#     local_news = News.published.all().filter(category__name = "Mahalliy").order_by('-publish_time')[1:6]
#     local_two = News.published.all().order_by('-publish_time')[:5]
#     local_sport_one = News.published.filter(category__name = 'Sport').order_by('-publish_time')[:1]
#     local_sport = News.published.all().filter(category__name = "Sport").order_by('-publish_time')[:5]
#     local_texno_one = News.published.filter(category__name= 'Texnologiya').order_by('-publish_time')[:1]
#     local_texno = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[:5]
#     context = {
#         'news_list': news_list,
#         'categories':categories,
#         'local_one': local_one,
#         'local_news': local_news,
#         'local_two': local_two,
#         'local_sport': local_sport,
#         'local_sport_one': local_sport_one,
#         'local_texno_one':local_texno_one,
#         'local_texno': local_texno
#     }
#     return render(request, 'news/home.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'News/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        #context['local_one']= News.published.filter(category__name = 'Mahalliy').order_by('-publish_time')[:1]
        context['mahalliy_xabarlar']=News.published.all().filter(category__name = "Mahalliy").order_by('-publish_time')[:6]
        context['local_two']=News.published.all().order_by('-publish_time')[:5]
        context['sport_xabarlar']=News.published.all().filter(category__name = "Sport").order_by('-publish_time')[:6]
        # context['local_sport_one']=News.published.filter(category__name = 'Sport').order_by('-publish_time')[:1]
        # context['local_texno_one']=News.published.filter(category__name= 'Texnologiya').order_by('-publish_time')[:1]
        context['texno_xabarlar']=News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[:6]
        context['local_foto']=News.published.all().filter(category__name='foto').order_by('-publish_time')[:5]
        # context['local_xorij_one']=News.published.filter(category__name='Xorij').order_by('-publish_time')[:1]
        context['xorij_xabarlar']=News.published.all().filter(category__name='Xorij').order_by('-publish_time')[:6]
        return context

class MahalliyNews(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Mahalliy")
        return news

class XorijNews(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Xorij")
        return news

class TexnologiyaNews(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologiya_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Texnologiya")
        return news

class SportNews(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news
# def contactpageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaniniz ushun rahmat</h2>")
#     context = {
#         'form':form
#     }
#     return render(request, "news/contact.html", context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaniniz ushun rahmat</h2>")
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)