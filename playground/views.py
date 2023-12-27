from django.shortcuts import render
import logging
import requests
# from django.db.models.aggregates import Count, Max, Min, Avg, Sum
# from store.models import Product

logger = logging.getLogger(__name__) # playground.view

# Create your views here.
def say_hello(request):
    # custom manager creating
    # TaggedItem.objects.get_tags_for(Product, 1)
    try:
        logger.info('Calling httpbin')
        response = requests.get('https://httpbin.org/delay/2')
        logger.info('Received the response')
        data = response.json()
    except requests.ConnectionError:
        logger.critical('httpbin is offline')
    return render(request, 'hello.html', { 'name': 'Bilal' })
