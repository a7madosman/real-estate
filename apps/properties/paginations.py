from rest_framework.pagination import PageNumberPagination


class  PropertPagination(PageNumberPagination):
    page_size = 3
