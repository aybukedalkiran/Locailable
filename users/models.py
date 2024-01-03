from django.db import models
from django.contrib.auth.models import User
import uuid
#from business.models import Business, Review


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
    
    USERNAME_FIELD = 'username'

"""
class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)  # 'up' veya 'down'

    def __str__(self):
        return f"{self.user.username} - {self.value}"
"""

"""
class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.user.username if self.user.username else 'Unknown User'
        business_name = self.business.business_name if self.business.business_name else 'Unknown Business'
        return f"{username} - {business_name} Review"
"""