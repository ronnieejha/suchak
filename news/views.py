from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.handlers.news_handler import collect_news_from_source


# Create your views here.


@api_view(['GET'])
def get_news_for_location(request):
    location = request.GET.get('locationName')
    news = collect_news_from_source(location)

    if news:
        return Response(data={'data': news, 'success': True, 'message': 'success'}, status=status.HTTP_200_OK)
    else:
        return Response(data={'data': [], 'success': False, 'message': 'Uable to get news for this location'},
                        status=status.HTTP_204_NO_CONTENT)


def render_news(request):
    location = request.GET.get('locationName')
    news = collect_news_from_source(location)
    return render(request, 'news.html', {'news_data': news})
