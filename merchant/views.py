from rest_framework.generics import ListAPIView
from .models import Merchant
from .serializers import MerchantSerializer
from rest_framework.pagination import PageNumberPagination


class CustomPaginationStyleOne(PageNumberPagination):
    page_size = 4

class CustomPaginationStyleTwo(PageNumberPagination):
    page_size_query_param = 'limit'

class CustomPaginationStyleThree(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'limit'


# creating view here
class MerchantList(ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    pagination_class = CustomPaginationStyleThree
    
   
