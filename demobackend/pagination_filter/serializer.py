from rest_framework import serializers
from pagination_filter.models import Student

class StudentSerializer(serializers.ModelSerializer):
    ''' Student Serializer '''
    class Meta:
        ''' Meta Class '''
        model = Student
        fields = '__all__'