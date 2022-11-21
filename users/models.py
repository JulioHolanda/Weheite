from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    professor = models.BooleanField()
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     try:
#         instance.profile.save()
#     except ObjectDoesNotExist:
#         Profile.objects.create(user=instance,professor=False)


class Forum(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.TextField(max_length=255)
    body = models.TextField(max_length=9999)
    respondida = models.ManyToManyField(User, default=None, blank=True, related_name='respondida')
    
    def __str__(self):
        return self.title

class Reply(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    body = models.TextField(max_length=9999)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.body

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
) 

DONE_CHOICES = (
    ('Done', 'Done'),
    ('Undone', 'Undone'),
)

class Like(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def str(self):
        return str(self.reply)

class Forum_done(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    value = models.CharField(choices=DONE_CHOICES, default='Undone', max_length=10)

    def str(self):
        return str(self.forum)

