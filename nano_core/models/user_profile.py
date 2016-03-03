from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key = True, related_name = "user_profile")

    POSITIONS = [
        ("UNDEF", "undefined"),
        ("PHD", "phd_student"),
        ("MSC","msc_student"),
        ("ENG","research_engineer"),
        ("ENG_ASST", "assistant_engineer"),
        ("PROF_ASST", "assistant_professor"),
        ("PROF", "full_professor"),
        ("MD", "medical_doctor"),
    ]

    position = models.CharField(max_length = 20, choices=POSITIONS, default=POSITIONS[0][0])

    phone    = models.CharField(max_length = 20, blank = True)
    fax      = models.CharField(max_length = 20, blank = True)
    address  = models.CharField(max_length = 50, blank = True)
    bio      = models.CharField(max_length = 1000, blank = True)
    picture  = models.FileField(upload_to = 'profile_pictures', blank = True)

    def __unicode__(self):
        return "{} | {}".format(self.user.username,self._meta.verbose_name)

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
