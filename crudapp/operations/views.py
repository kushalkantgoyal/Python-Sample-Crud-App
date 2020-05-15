from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Car


def get_cars(request):
    all_cars = list(Car.objects.all())
    all_cars = [{"id": car.id, "name": car.name, "price": car.price}
                for car in all_cars]

    output = {"data": all_cars}
    return JsonResponse(output)


def show_cars(request):
    cars = get_cars(request)
    cars = eval(cars.content.decode())
    context = {
        'cars': cars['data']
    }
    return render(request, 'ShowCar.html', context=context)


@api_view(['POST'])
def post_car(request):
    name = request.data.get('name')
    price = request.data.get('price')
    try:
        car = Car.objects.create(name=name, price=price)
        output = {"id": car.id,
                  "name": car.name,
                  "price": car.price
                  }
    except Exception as err:
        output = {"error": str(err)}
    return JsonResponse(output)


class CarOperations(APIView):

    def get(self, request, pk):
        try:
            car = Car.objects.filter(id=pk).first()
            context = {
                'id': car.id,
                'name': car.name,
                'price': car.price
            }

        except Exception as err:
            context = {
                "error": "Car does not exists"
            }

        return JsonResponse(data=context)

    def put(self, request, pk):
        payload = request.data
        name = payload.get('name')
        price = payload.get('price')

        try:
            Car.objects.filter(id=pk).\
                update(name=name, price=price)

            car = Car.objects.filter(id=pk).first()
            context = {
                'id': car.id,
                'name': car.name,
                'price': car.price
            }

        except Exception as err:
            context = {
                "error": "Car does not exists"
            }

        return JsonResponse(data=context)

    def delete(self, request, pk):
        try:
            Car.objects.get(id=pk).delete()
            context = {"msg": "Car deleted successfully!"}

        except Exception as err:
            context = {
                "error": "Provide a valid key"
            }

        return JsonResponse(data=context)
