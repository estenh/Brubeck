from django.contrib.gis.db import models

from django.contrib.auth.models import User

class Person(models.Model):

    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('e-mail address', blank=True, null=True)
    slug = models.SlugField(help_text="Used for URLs. Autogenerated from name.")
    mugshot = models.ImageField(upload_to='%Y/mugshots/staff', blank=True, null=True, help_text="For editors and columnists, mainly, though there's nothing stopping other staffers from having them, too. Accepts JPEG, GIF or PNG file formats. Automatically resized to the proper dimensions.")
    user = models.ForeignKey(User, blank=True, null=True, help_text="If this person has a username on the site, select it here to link the two. Their comments and other actions on the site will be shown differently, and this will facilitate that. This field also allows basic staffers to only modify content which lists them on the byline."))

    objects = models.GeoManager()

    class Meta:
        abstract = True
        verbose_name_plural = 'people'

    def __unicode__(self):
        name = ''
        if self.first_name:
            name = name + self.first_name + '  '
        if self.middle_name:
            name = name + self.middle_name + ' '
        name = name + self.last_name
        return name
