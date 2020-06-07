from django.shortcuts import render
from news.handlers.news_handler import collect_news_from_source
# Create your views here.


from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

@api_view(['GET'])
def get_news_for_location(request):
    location = request.GET.get('locationName')
    news = collect_news_from_source(location)

    if news:
        return Response(data={'data':news,'success':True,'message':'success'},status=status.HTTP_200_OK)
    else:
        return Response(data={'data':[],'success':False,'message':'Uable to get news for this location'},status=status.HTTP_204_NO_CONTENT)

