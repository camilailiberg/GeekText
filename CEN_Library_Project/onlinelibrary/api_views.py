from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from onlinelibrary.serializers import ShoppingCartItemSerializer
from onlinelibrary.models import ShoppingCartItem


class ShoppingCartItemPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ShoppingCartItemList(ListAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'ordered', 'savedforlater', 'addedon',)
    pagination_class = ShoppingCartItemPagination


class ShoppingCartItemCreate(CreateAPIView):
    serializer_class = ShoppingCartItemSerializer

    def create(self, request, *args, **kwargs):
        try:
            shoppingcart = request.data.get('shoppingcart')
        except ValidationError:
            raise ValidationError({'shoppingcart': 'A valid shopping cart is required'})
        try:
            book = request.data.get('book')
        except ValidationError:
            raise ValidationError({'book': 'A valid book is required'})
        try:
            quantity = request.data.get('quantity')
            if quantity is not None and int(quantity) <= 0:
                raise ValidationError({'quantity': 'Must be above 0'})
        except ValidationError:
            raise ValidationError({'quantity': 'A valid quantity is required'})
        try:
            ordered = request.data.get('ordered')
        except ValidationError:
            raise ValidationError({'ordered': 'A valid boolean is required'})
        try:
            savedforlater = request.data.get('savedforlater')
        except ValidationError:
            raise ValidationError({'savedforlater': 'A valid boolean is required'})
        return super().create(request, *args, **kwargs)


class ShoppingCartItemRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCartItem.objects.all()
    lookup_field = 'id'
    serializer_class = ShoppingCartItemSerializer

    def delete(self, request, *args, **kwargs):
        shoppingcartitemid = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('shoppingcartitemid_data_{}'.format(shoppingcartitemid))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            shoppingcartitem = response.data
            cache.set('shoppingcartitem_data_{}'.format(shoppingcartitem['id']), {
                'shoppingcart': shoppingcartitem['shoppingcart'],
                'book': shoppingcartitem['book'],
                'quantity': shoppingcartitem['quantity'],
                'ordered': shoppingcartitem['ordered'],
                'savedforlater': shoppingcartitem['savedforlater'],
            })
        return response
