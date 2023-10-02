from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import student, hostel_record, patient_record
from .serializers import studentCRSerializer, hostelCRSerializer, patientCRSerializer, StudentSerializer
from rest_framework import generics, mixins
# Create your views here.

class studentCRView(LoginRequiredMixin, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = student.objects.all()
    serializer_class = studentCRSerializer

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        


class patientCU(LoginRequiredMixin,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               generics.GenericAPIView):
    queryset = patient_record.objects.all()
    serializer_class = patientCRSerializer
    lookup_field ='pk'

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class hostelCU(LoginRequiredMixin,
               mixins.ListModelMixin,
                mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               generics.GenericAPIView):
    queryset = hostel_record.objects.all()
    serializer_class = hostelCRSerializer
    lookup_field = 'pk' 
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class studentListView(generics.ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentCRSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentList(APIView):
    def get(self, request):
        students = student.objects.all()
        serializer = StudentSerializer(students, many=True, context={'request': request})
        return Response(serializer.data)

class StudentDetail(APIView):
    def get(self, request, pk):
        student = student.objects.get(pk=pk)
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)

class HostelRecordCreate(generics.UpdateAPIView):
    queryset = hostel_record.objects.all()  # Specify the queryset for hostel records
    serializer_class = hostelCRSerializer

    def get_queryset(self):
        # Filter the queryset to retrieve records for the specific student
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(student_id=pk)
    
    def post(self, request, pk):
        student = student.objects.get(pk=pk)
        serializer = hostelCRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientRecordCreate(generics.RetrieveUpdateAPIView):
    queryset = patient_record.objects.all()  # Specify the queryset for patient records
    serializer_class = patientCRSerializer

    def get_queryset(self):
        # Filter the queryset to retrieve records for the specific student
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(student_id=pk)
    
    def post(self, request, pk):
        student = student.objects.get(pk=pk)
        serializer = patientCRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
