from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'calories_tracker/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'calories_tracker/delete.html')
