from django.shortcuts import render
from pagination_filter.models import Student
from pagination_filter.serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from django_filters import FilterSet, CharFilter, NumberFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class StudentAPIFilter(FilterSet):
    '''Filtering is managed from here'''
    student_name = CharFilter(lookup_expr='iexact') 
    total_marks = NumberFilter(lookup_expr='gte')

    class Meta:
        model = Student
        fields = ['student_name', 'total_marks']

class StudentListPagination(PageNumberPagination):
    '''Inherting the class and setting query params'''
    page_size_query_param = 'page_size'  
    page_number_query_param = 'page'  

class StudentViews(GenericAPIView,ListModelMixin):
    '''List all students'''
    queryset = Student.objects.all().order_by('student_id') 
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        page_size = request.GET.get('page_size')
        page_number = request.GET.get('page')
        
        student_filter = StudentAPIFilter(request.GET, queryset=self.queryset)
        students = student_filter.qs
        
        paginator = StudentListPagination()
        paginator.page_size = int(page_size) if page_size else 9999999
        paginator.page = int(page_number) if page_number else 1
        page = paginator.paginate_queryset(students, request)
        
        serializer = StudentSerializer(page, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    