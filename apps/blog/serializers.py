from rest_framework import serializers
from .models import Post, Category, Heading

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
            "slug",
        ]

class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = [
            "title",
            "slug",
            "lavel",
            "order",
        ]

class PostSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    headings = HeadingSerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "description",
            "thumbnail",
            "slug",
            "category",
        ]

