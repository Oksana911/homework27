import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from .models import Category, Ads


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        response = []
        categories = Category.objects.all()
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        category_data = json.loads(request.body)
        category = Category()
        category.name = category_data.get("name")
        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name
        },
            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        response = []
        ads = Ads.objects.all()
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ads()
        ad.name = ad_data.get("name")
        ad.author = ad_data.get("author")
        ad.price = ad_data.get("price")
        ad.description = ad_data.get("description")
        ad.address = ad_data.get("address")
        ad.is_published = ad_data.get("is_published")
        
        ad.save()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        },
            json_dumps_params={"ensure_ascii": False})
