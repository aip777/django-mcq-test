from rest_framework import serializers
from sapp.models import StudentInformation

class StudentsStatus(serializers.ModelSerializer):
    class Meta:
        model = StudentInformation
        fields = [
            'id',
            'id_number',
            'first_name',
            'last_name',
            'email',
            'phone',
            'father_name',
            'mother_name',
            'cgpa',

        ]
        # read_only_fields = ['id_number']
        # def validate_content(self, value):
        #     if len(value) > 10000:
        #         raise serializers.ValidationError("This is wayy too long.")
        #     return value

        def validate(self, data):
            first_name = data.get("first_name", None)
            if first_name == "":
                first_name = None
            last_name = data.get("last_name", None)
            if first_name is None and last_name is None:
                raise serializers.ValidationError("title or image is required.")
            return data
