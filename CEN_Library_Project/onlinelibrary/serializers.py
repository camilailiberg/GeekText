from rest_framework import serializers
from onlinelibrary.models import ShoppingCartItem, ShoppingCart


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('id', 'user')


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    totalforthisbookandquantity = serializers.FloatField(read_only=True, source='total')
    Bookname = serializers.CharField(max_length=200, read_only=True, source='getbookname')
    Usersname = serializers.CharField(max_length=200, read_only=True, source='getusername')
    NumnberOfThisBookInShoppingCart = serializers.IntegerField(min_value=1, source='quantity')
    Userid = serializers.IntegerField(read_only=True, source='getuserid')
    ShoppingCartItemid = serializers.IntegerField(read_only=True, source='id')

    class Meta:
        model = ShoppingCartItem
        fields = ('ShoppingCartItemid', 'savedforlater', 'addedon', 'ordered', 'purchasedby', 'Bookname',
                  'book', 'NumnberOfThisBookInShoppingCart', 'totalforthisbookandquantity', 'shoppingcart', 'Usersname', 'Userid')
