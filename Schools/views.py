from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from schools.models import Teacher, School
from schools.serializers import TeacherSerializer, SchoolSerializer


class TeacherFilter(filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            "id": ["exact"],
            "code": ["exact"],
            "first_name": ["exact", "contains"],
            "email": ["exact"],
            "phone_number": ["exact"],
        }


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter

    def get_queryset(self):
        # return self.queryset.filter(school=self.request.school)
        return self.queryset.filter()
    

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
