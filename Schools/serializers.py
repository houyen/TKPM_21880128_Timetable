from rest_framework import serializers

from schools.models import Teacher, School


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        read_only_fields = ("full_name",)
        fields = ("id", "full_name", "code")
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        # read_only_fields = ("name",)
        fields = ("id", "name", "code")
