from django.shortcuts import render

# Create your views here.
def cart(request):
    general = 'Главная страница'
    shop = 'Магазин'
    products = 'Корзина'
    context = {
        'general': general,
        'shop': shop,
        'products': products
    }
    return render(request, 'third_task/cart.html', context)

def games(request):
    game1 = 'Atomic Heart'
    game2 = 'Cyberpank 2077'
    game3= 'PayDay 2'
    context = {
        'game1': game1,
        'game2': game2,
        'game3': game3
    }
    return render(request, 'third_task/games.html', context)

def platform(request):
    return render(request, 'third_task/platform.html')
