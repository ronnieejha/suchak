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
    if not location:
        return Response(data={'data':[],'success':False,'message':'Invalid params, Using locationName as param to pass location\'s name'}, status=status.HTTP_400_BAD_REQUEST)
    if request.user.is_authenticated and request.user.is_staff and request.user.is_active:
        if news:
            return Response(data={'data': news, 'success': True, 'message': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'data': [], 'success': False, 'message': 'Uable to get news for this location'},
                            status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_401_UNAUTHORIZED,data={'success':False,'message':'Not Authorized to access','data':[]})


def render_news(request):
    location = request.GET.get('locationName')
    news = collect_news_from_source(location)
    return render(request, 'news.html', {'news_data': news})
