# from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse

# Create your views here.
# def homepage(request: HttpRequest):
#     response = {"message": "Hello World"}
#     return JsonResponse(data=response)


from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

# posts=[
#     {
#         "id":1,
#         "title": "Python",
#         "content": "It is a very simple programming language"
#     },
#     {
#         "id":2,
#         "title": "JavaScript",
#         "content": "It is another simple programming language"
#     },
#     {
#         "id":3,
#         "title": "JAVA",
#         "content": "It is yet another simple programming language"
#     }
# ]

@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data
        response = {"message": "Hello Morld", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {"message": "Hello Mojjam"}
    return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=["GET","POST"])
# def list_posts(request:Request):
#     posts = Post.objects.all()

#     if request.method == "POST":
#         data = request.data

#         serializer = PostSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()

#             response = {"message": "Post Created", "data": serializer.data}

#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     serializer = PostSerializer(instance=posts, many=True)

#     response = {
#         "message":"posts",
#         "data": serializer.data
#     }

#     return Response(data=response, status=status.HTTP_200_OK)

# ## Class-based API view

class PostListCreateView(APIView):

    """
        A view for creating and listing post
    """
    serializer_class = PostSerializer

    def get(self, request:Request, *args, **kwargs):
        posts = Post.objects.all()

        serializer = PostSerializer(instance=posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request:Request, *args, **kwargs):
        data=request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Post created",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)

    serializer = PostSerializer(instance=post)

    response = {"message": "post", "data": serializer.data}

    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def get_post_by_id(request:Request, post_id:int):
    pass

@api_view(http_method_names=["PUT"])
def update_post(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)

    data = request.data

    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "message": "Post updated successfully",
            "data": serializer.data,
        }

        return Response(data=response, status=status.HTTP_200_OK)
    
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["DELETE"])
def delete_post(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)