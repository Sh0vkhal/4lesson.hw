from django.db import models

# Create your models here.
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


from rest_framework.parsers import JSONParser


from .models import Category,Moview, Comment

class MoviewSerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     movie = models.CharField(max_length=50)
     year = models.IntegerField()
     category_id = serializers.IntegerField()


     def create(self, validated_data):
        return Moview.objects.create(**validated_data)

     def update(self, instance, validated_data):
        instance.movie = validated_data.get("movie", instance.movie)
        instance.year = validated_data.get("year",  instance.year)
        instance.category = validated_data.get("category_id", instance.category_id)
        instance.save()
        return instance
     


class CommentSerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)     
     user = serializers.CharField(max_length=70)
     comment = serializers.CharField(max_length=200)
     category_id_2 = serializers.IntegerField()


     def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    
     def update(self,instance,validated_data):
         instance.user = validated_data.get("user", instance.user)
         instance.comment = validated_data.get("comment",  instance.comment)
         instance.category_2 = validated_data.get("category_id_2", instance.category_id_2)
         instance.save()
         return instance
     