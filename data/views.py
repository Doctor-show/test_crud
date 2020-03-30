from rest_framework import generics
from data.serializers import DataDetailSerializer, DataListSerializer
from data.models import Data
from rest_framework.permissions import IsAuthenticated
from data.permissions import IsOwnerOrReadOnly


class DataCreateView(generics.CreateAPIView):
    serializer_class = DataDetailSerializer
    permission_classes = (IsAuthenticated,)


class DataListView(generics.ListAPIView):
    serializer_class = DataListSerializer
    queryset = Data.objects.all()
    permission_classes = (IsAuthenticated,)


class DataDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DataDetailSerializer
    queryset = Data.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
