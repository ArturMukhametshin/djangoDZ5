from django.shortcuts import render

# Create your views here
def cart(request):

    return render(request, 'cart.html')

def games(request):
    title_g = 'Игры'
    games = ["Atomic Heart", "Cyberpunk 2077", 'PayDay 2']
    context = {
        'games': games,
        'title_g': title_g
    }
    return render(request, 'games.html', context)

def platform(request):
    title_p = 'Корзина'
    message = 'Извините, ваша корзина пуста'
    context = {
        'title_p': title_p,
        'message': message
    }

    return render(request, 'platform.html', context)

def menu(request):
    general = 'Главная страница'
    shop = 'Магазин'
    products = 'Корзина'
    context = {
        'general': general,
        'shop': shop,
        'products': products
    }
    return render(request, 'menu.html', context)
