from django import forms
from .models import Member, Process

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'dob', 'email']

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['member', 'first_contact', 'response_by_secretary', 'submitted_application', 'documents_received', 'mentor_assigned', 'first_vote', 'interview_date', 'commission_findings', 'final_vote', 'date_of_initiation', 'extra_info']
