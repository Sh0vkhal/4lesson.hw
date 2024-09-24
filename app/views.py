from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Moview, Comment
from .serializer import MoviewSerializer, CommentSerializer

class ListAPIMoview(APIView):
    def get(self, request:Request, pk=None):
        if pk:
            try:
                movie = Moview.objects.get(pk=pk)
                return Response(MoviewSerializer(movie).data)
            except:
                return Response({"message":"Invalid id"})
        movie = Moview.objects.all()
        return Response(MoviewSerializer(movie, many=True).data)

    def post(self, request: Request, pk=None):
        if not pk:
            serializer = MoviewSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            movie = serializer.save()
            return Response(MoviewSerializer(movie).data)
        return Response({"message": "Method POST not allowed"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                movie = Moview.objects.get(pk=pk)
                serializer = MoviewSerializer(instance=movie, data=request.data)
                serializer.is_valid(raise_exception=True)
                movie = serializer.save()
                return Response(MoviewSerializer(movie).data)
            except:
                return Response({"message": "Does not exist"})
        return Response({"message": "Method Put not allowed"})

    def delete(self, request: Request, pk=None):
        if pk:
            movie = Moview.objects.get(pk=pk)
            movie.delete()
            return Response({"message": "success"})
        else:
            return Response({"message": "Method DELETE not found "})




class ListAPIComment(APIView):
    def get(self, request:Request, pk=None):
        if pk:
            try:
                cooment = Comment.objects.get(pk=pk)
                return Response(CommentSerializer(cooment).data)
            except:
                return Response({"message":"Invalid id"})
        cooment = Comment.objects.all()
        return Response(CommentSerializer(cooment, many=True).data)

    def post(self, request: Request, pk=None):
        if not pk:
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            comment = serializer.save()
            return Response(CommentSerializer(comment).data)
        return Response({"message": "Method POST not allowed"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                serializer = CommentSerializer(instance=comment, data=request.data)
                serializer.is_valid(raise_exception=True)
                comment = serializer.save()
                return Response(CommentSerializer(comment).data)
            except:
                return Response({"message": "Does not exist"})
        return Response({"message": "Method Put not allowed"})

    def delete(self, request: Request, pk=None):
        if pk:
            movie = Moview.objects.get(pk=pk)
            movie.delete()
            return Response({"message": "success"})
        else:
            return Response({"message": "Method DELETE not found "})
