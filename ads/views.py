import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from homework27 import settings
from users.models import User
from .models import Category, Ad
from .serializers import AdSerializer
from rest_framework.generics import ListAPIView


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})



class CategoryView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        response = []
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")  # сортировка по алфавиту
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


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
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Category.objects.create(
            name=category_data.get("name")
        )

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data["name"]
        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        },
            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted"}, status=200)


######################################################################


class AdView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        categories = request.GET.getlist('category', None)  # поиск по категориям (можно по нескольким:))
        cat_q = None
        for cat in categories:
            if cat_q is None:
                cat_q = Q(category_id__in=cat)
            else:
                cat_q |= Q(category_id__in=cat)

        if cat_q:
            self.queryset = self.queryset.filter(cat_q)

        search_text = request.GET.get('text', None)  # поиск по слову
        if search_text:
            self.queryset = self.queryset.filter(
                name__icontains=search_text
            )

        location = request.GET.get('location', None)  # поиск по локации
        if location:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=location
            )

        price_from = request.GET.get('price_from', None)  # поиск по цене
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(request, *args, **kwargs)

@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = Ad
    fields = ["name", "price", "description", "is_published", "image", "author", "category"]

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "author": ad.author.username,
            "category": ad.category.name
        },
            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["name", "price", "description", "is_published", "author", "category"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        author = get_object_or_404(User, id=ad_data['author'])
        category = get_object_or_404(Category, id=ad_data['category'])

        ad = Ad.objects.create(
            name=ad_data["name"],
            price=ad_data["price"],
            description=ad_data["description"],
            is_published=ad_data["is_published"],
            author=author,
            category=category
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "author": ad.author.username,
            "category": ad.category.name
        },
            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdImageUpdateView(UpdateView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.username,
            "image": self.object.image.url if self.object.image else None
        },
            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name", "price", "description", "author", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)
        self.object.name = ad_data["name"]
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        # self.object.author = ad_data["author"]
        # self.object.category = ad_data["category"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            # "author": self.object.author,
            # "author_id": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            # "category_id": self.object.category_id,
            # "image": self.object.image.url
        },
            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted"}, status=200)
