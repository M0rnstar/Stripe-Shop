import stripe
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from django.conf import settings
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item_detail.html', {
        'item': item,
        'stripe_publish_key': settings.STRIPE_PUBLISHABLE_KEY
    })

def buy_item(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        raise Http404("Товар не найден")
    
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'unit_amount': int(item.price * 100),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                },
                'quantity': 1,
          }],
          mode='payment',
          success_url=request.build_absolute_uri('/success/'),
          cancel_url=request.build_absolute_uri('/cancel/'),
        )
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'id': session.id})

def payment_success(request):
    return render(request, 'success.html')

def payment_cancel(request):
    return render(request, 'cancel.html')
