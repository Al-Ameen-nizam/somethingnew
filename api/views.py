from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls={
        'List ':'/product-list/',
        'Detail views' :'/product-detail/<int:id>',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>',
        'Delete':'/product-Delete/<int:id>',
    }
    return Response(api_urls)