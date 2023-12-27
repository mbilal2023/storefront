from rest_framework.pagination import PageNumberPagination

class DefaultPaginaiton(PageNumberPagination):
    page_size = 10