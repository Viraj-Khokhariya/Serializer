from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Snippet
from app.serializers import SnippetSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def snippet_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def snippet_post(request,format=None):
    if request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def snippet_delete(request,pk):
    snippets = Snippet.objects.get(id=pk)
    snippets.delete()
    return Response("Record Deleted Successfully!!!")
    
       

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((permissions.AllowAny,))
# def snippet_detail(request, pk , format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class UserList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    

# class Item(generics.RetrieveAPIView):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


# @api_view(['GET'])
# def index(request,format=None):
#     queryset = Snippet.objects.all()
#     serializer = SnippetSerializer(queryset, many=True)
#     return Response(serializer.data)




