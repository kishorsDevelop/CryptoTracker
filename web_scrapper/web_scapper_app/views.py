from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cryptocurrency
import json

@csrf_exempt
def update_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for item in data:
            cryptocurrency, created = Cryptocurrency.objects.get_or_create(
                name=item['name'],
                defaults={
                    'price': item['price'],
                    'change_1h': item['change_1h'],
                    'change_24h': item['change_24h'],
                    'change_7d': item['change_7d'],
                    'market_cap': item['market_cap'],
                    'volume_24h': item['volume_24h'],
                    'circulating_supply': item['circulating_supply']
                }
            )
            if not created:
                cryptocurrency.price = item['price']
                cryptocurrency.change_1h = item['change_1h']
                cryptocurrency.change_24h = item['change_24h']
                cryptocurrency.change_7d = item['change_7d']
                cryptocurrency.market_cap = item['market_cap']
                cryptocurrency.volume_24h = item['volume_24h']
                cryptocurrency.circulating_supply = item['circulating_supply']
                cryptocurrency.save()
        return JsonResponse({'message': 'Data updated successfully'})
    return JsonResponse({'error': 'Invalid request method'})


def get_latest_data(request):
    data = Cryptocurrency.objects.all().values()
    return JsonResponse(list(data), safe=False)
