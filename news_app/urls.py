from django.urls import path
from .views import news_detail, news_list, ContactPageView, HomePageView, \
     MahalliyNews, XorijNews, TexnologiyaNews, SportNews #homepageView, 

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home_page'),
    path('mahalliy/', MahalliyNews.as_view(), name = 'mahalliy_page'),
    path('xorij/', XorijNews.as_view(), name = 'xorij_page'),
    path('texnologiya/', TexnologiyaNews.as_view(), name = 'texnologiya_page'),
    path('sport/', SportNews.as_view(), name = 'sport_page'),
    path('contact/', ContactPageView.as_view(), name = 'contact_page'),
    path('news/', news_list, name='news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail')
]