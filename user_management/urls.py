from django.urls import path
from .views import (
    register_view,
    login_view,
    dashboard_view,
    logout_view,
    update_profile,
    submission_evidence_view,
    submission_evidence_file_view,
)

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path(
    'profile/update/',  update_profile, name='update_profile'),
    path(
        'submission-evidence/',
        submission_evidence_view,
        name='submission_evidence'
    ),
    path(
        'submission-evidence/files/<str:filename>/',
        submission_evidence_file_view,
        name='submission_evidence_file'
    ),
   

]