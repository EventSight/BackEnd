from django.contrib.auth.models import AbstractUser
from django.db import models


# username, email, password, first_name, last_name
# would be handled by parent class
class Student(AbstractUser):
    pass


class Club(models.Model):

    # club will have an admin, and if we delete admin then it would do nothing
    name = models.CharField(max_length=128, primary_key=True)
    admin = models.ForeignKey(
        Student, on_delete=models.DO_NOTHING, default=None)
    description = models.CharField(max_length=2048)
    followers = models.ManyToManyField(
        Student, blank=True, related_name="follow_list")
    members = models.ManyToManyField(
        Student, blank=True, related_name="member_list")
    image_url = models.URLField()

    def __str__(self):
        return f"{self.name}, administered by: {self.admin}"


class member_request(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, default=None)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)
    date_time = models.DateTimeField(auto_created=True)


class Event(models.Model):

    # if organizers are deleted, then Event would also be deleted
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    details = models.CharField(max_length=2048)
    date_time = models.DateTimeField()
    organizers = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="event_organizers")
    interested = models.ManyToManyField(
        Student, blank=True, related_name="interested_events")
    participants = models.ManyToManyField(
        Student, blank=True, related_name="participated_events")
    open_to_all = models.BooleanField()
    image_url = models.URLField()


class Comment(models.Model):

    comment_text = models.CharField(max_length=2048)
    date_time = models.DateTimeField(auto_created=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, default=None)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)