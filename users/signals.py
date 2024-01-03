from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Locailable'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )

@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created is False:
        subject = 'Profile Updated'
        message = 'Your profile information has been updated.'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )

@receiver(post_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    try:
        subject = 'Account Deleted'
        message = 'Your account has been deleted successfully.'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )
    except:
        pass

# Connect the signals
post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=User)
post_delete.connect(delete_user, sender=User)
