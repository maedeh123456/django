from rest_framework import generics , filters
from blog.models import Blog
from django.core.exceptions import PermissionDenied
from .permission import OwnerCanmangeorReadonly
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,  # request.user.is_stuff == True
    IsAuthenticatedOrReadOnly
)
from .serializers import (
postlistserializer ,
postdetailserializer,
postdeleteserializer,
postupdateserializer,
postcreateserializer,
postdetailupdateserializer,
postdetaildestroyserializer,
postupdatedestroyserializer
)
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend 



class postlistAPIView(generics.ListAPIView):
    serializer_class = postlistserializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
    filterset_fields = ('title','content','owner')
    search_fields = ['title','content','owner__username']
    order_fields = ['title']
    #search_fields = ['username', 'email']

    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser:
            queryset = Blog.objects.all()
        elif not self.request.user.is_anonymous:
            queryset = Blog.objects.filter(owner = self.request.user)
        else :
            return None
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
            Q(title__contains=query)|
            Q(content__contains=query)).distinct().order_by('title')
        return queryset
    

class postdetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = postdetailserializer
    lookup_field = 'id'

class postDestroyAPIView(generics.DestroyAPIView):
    queryset  = Blog.objects.all()
    serilalizer_class = postdeleteserializer
    lookup_field = 'id'
    def perform_destroy(self,serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()

class postUpdateAPIView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = postupdateserializer
    lookup_field = 'id'
    permission_classes =  [OwnerCanmangeorReadonly,]
    def perform_update(self,serializer):
        serializer.save(owner = self.request.user)

class postcreateAPIView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = postcreateserializer
    permission_classes = [IsAuthenticated,]
    def perform_create(self,serializer):
        serializer.save(owner = self.request.user)

class postdetailupdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = postdetailupdateserializer
    lookup_field = 'id'
    permission_classes = [OwnerCanmangeorReadonly,]
    def perform_update(self,serializer):
        serializer.save(owner = self.request.user)

class postRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = postdetaildestroyserializer
    lookup_field = 'id'
    permission_classes = [OwnerCanmangeorReadonly,]
    def perform_destroy(self,serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()

class postRUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = postupdatedestroyserializer
    lookup_field = 'id'
    permission_classes = [OwnerCanmangeorReadonly,]