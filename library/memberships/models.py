import uuid
from django.db import models

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    socialmedia = models.JSONField()  # To store a JSON object with various social media profiles

    def __str__(self):
        return self.name


class Process(models.Model):
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    first_contact = models.JSONField(default=dict)  # This will store method of contact and date
    response_by_secretary = models.FileField(upload_to='responses/', null=True, blank=True)  # PDF storage
    submitted_application = models.BooleanField(default=False)
    documents_received = models.JSONField(default=dict, blank=True)  # Flexible field to note which documents were received
    mentor_assigned = models.CharField(max_length=255, null=True, blank=True)
    first_vote = models.BooleanField(default=False)
    interview_date = models.DateField(null=True, blank=True)
    commission_findings = models.JSONField(default=dict, blank=True)  # Flexible field for the report
    final_vote = models.BooleanField(null=True, blank=True)
    date_of_initiation = models.DateField(null=True, blank=True)
    extra_info = models.JSONField(default=dict, blank=True)  # Field to store any additional flexible information

    def __str__(self):
        return f"Process for {self.member.name}"
