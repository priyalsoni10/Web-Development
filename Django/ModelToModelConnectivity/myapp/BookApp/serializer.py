from rest_framework.serializers import ModelSerializer
from .models import BookModel
from AuthorApp.serializer import AuthorSerializer
class BookSerializer(ModelSerializer):
    # author = AuthorSerializer()
    class Meta:
        model = BookModel
        fields = '__all__'

class BookReadSerializer(ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = BookModel
        fields = '__all__'
