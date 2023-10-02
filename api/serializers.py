from rest_framework.serializers import ModelSerializer
from app.models import student, hostel_record, patient_record
from django.contrib.auth.models import User # actually used 
from rest_framework import serializers
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

class studentCRSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')

    # add_patient = serializers.HyperlinkedIdentityField(view_name= 'add_patient', lookup_field ='pk')
    # add_hostel = serializers.HyperlinkedIdentityField(view_name= 'add_hostel', lookup_field ='pk')

    add_hostel = serializers.HyperlinkedRelatedField(
        view_name='add_hostel',
        queryset=hostel_record.objects.all(),
        lookup_field='student_id',
        required=False,
        allow_null=True
    )

    add_patient = serializers.HyperlinkedRelatedField(
        view_name='add_patient',
        queryset=patient_record.objects.all(),
        lookup_field='student_id',
        required=False,
        allow_null=True
    )

    # add_patient = serializers.HyperlinkedRelatedField(
    #     view_name='add_patient',
    #     queryset=patient_record.objects.all(),
    #     required= False
    # )
    class Meta:
        model = student
        fields = ['id', 'user', 'surname', 'first_name',
                   'last_name', 'level', 'gender',
                     'department', 'add_hostel', 'add_patient']
        
    # def get_add_hostel(self, obj):
    #     try:
    #         if obj.hostel_record:
    #             return reverse('add_hostel', args=[obj.hostel_record.pk])
    #     except ObjectDoesNotExist:
    #         pass
    #     return None

    # def get_add_patient(self, obj):
    #     try:
    #         if obj.patient_record:
    #             return reverse('add_patient', args=[obj.patient_record.pk])
    #     except ObjectDoesNotExist:
    #         pass
    #     return None
    
class patientCRSerializer(ModelSerializer):
    class Meta:
        model = patient_record
        fields = '__all__'

class hostelCRSerializer(ModelSerializer):
    class Meta:
        model = hostel_record
        fields = '__all__'


from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    hostel_record_link = serializers.HyperlinkedIdentityField(
        view_name='hostel-record-create',
        lookup_field='pk'
    )
    patient_record_link = serializers.HyperlinkedIdentityField(
        view_name='patient-record-create',
        lookup_field='pk'
    )

    class Meta:
        model = student
        fields = ['id', 'user', 'surname', 'first_name', 'last_name', 'level', 'gender', 'department', 'hostel_record_link', 'patient_record_link']

    
