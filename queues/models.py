from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class ServiceCategory(models.Model):
    name = models.CharField(max_length=50) # Teller, CS
    prefix = models.CharField(max_length=1) # A, B
    icon = models.CharField(max_length=50, default='heroicons/user')
    color = models.CharField(max_length=20, default='blue')

    def __str__(self):
        return self.name

class Counter(models.Model):
    name = models.CharField(max_length=50) # Loket 1, CS 1
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    current_petugas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class QueueItem(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('calling', 'Calling'),
        ('processing', 'In Progress'),
        ('completed', 'Completed'),
        ('missed', 'Missed'),
    ]

    number = models.IntegerField()
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    
    created_at = models.DateTimeField(auto_now_add=True)
    called_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    
    counter = models.ForeignKey(Counter, on_delete=models.SET_NULL, null=True, blank=True)
    petugas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='served_queues')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='my_queues')

    class Meta:
        ordering = ['created_at']

    def formatted_number(self):
        return f"{self.category.prefix}{self.number:03d}"

    def __str__(self):
        return f"{self.formatted_number()} - {self.status}"

class BankConfig(models.Model):
    bank_name = models.CharField(max_length=100, default='Antigravity Bank')
    running_text = models.TextField(default='Selamat Datang di Antigravity Bank. Utamakan Budaya Antre.')
    opening_time = models.TimeField(default='08:00:00')
    closing_time = models.TimeField(default='16:00:00')
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.bank_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return None


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)
