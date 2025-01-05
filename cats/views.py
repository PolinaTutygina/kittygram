# Нужен для view-функции
#from rest_framework.decorators import api_view

# Нужены для view-класса (низкоуровнего)
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status

# Высокоуровневый view-класс (дженерики).
#from rest_framework import generics


# Нужно для вьюсетов.
from rest_framework import viewsets 

from .models import Cat
from .serializers import CatSerializer

# Вьюсет, обработает все шесть типичных действий.
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

# Высокоуровневые view-классы (дженерики).
#class CatList(generics.ListCreateAPIView):
#    queryset = Cat.objects.all()
#    serializer_class = CatSerializer
#
#
#class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Cat.objects.all()
#    serializer_class = CatSerializer 


# Низкоуровневый view-класс.
#class APICat(APIView):
#    def get(self, request):
#        cats = Cat.objects.all()
#        serializer = CatSerializer(cats, many=True)
#        return Response(serializer.data)
#
#    def post(self, request):
#        serializer = CatSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED) 
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# View-функция.
#@api_view(['GET', 'POST'])  # Разрешены только POST- и GET-запросы
#def cat_list(request):
#    # В случае POST-запроса добавим список записей в БД
#    if request.method == 'POST':
#        serializer = CatSerializer(data=request.data, many=True)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    # В случае GET-запроса возвращаем список всех котиков
#    cats = Cat.objects.all()
#    serializer = CatSerializer(cats, many=True)
#    return Response(serializer.data)
