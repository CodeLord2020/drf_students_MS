from django.urls import path, include
from . import views

urlpatterns = [ 

 path('studentCR/', views.studentCRView.as_view(), name = 'studentCR' ),
 path('studentCR/<int:student_id>/patientCU/', views.patientCU.as_view(), name = 'add_patient' ),
 path('studentCR/<int:student_id>/hostelCU/', views.hostelCU.as_view(), name = 'add_hostel' ),

path('students/', views.StudentList.as_view(), name='student-list'),
path('students/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
path('students/<int:pk>/hostel-record/', views.HostelRecordCreate.as_view(), name='hostel-record-create'),
path('students/<int:pk>/patient-record/', views.PatientRecordCreate.as_view(), name='patient-record-create'),





]