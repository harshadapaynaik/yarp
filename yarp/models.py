from django.db import models
from django.contrib.auth.models import User
import yarp.settings as settings
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _


class Post(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=60,  unique=True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	attachment = models.ImageField(upload_to=settings.MEDIA_ROOT+'img/post/%Y/%m/')
	is_published = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	slug = models.SlugField(_('slug'), max_length=40, blank=True)


	def save(self, *args, **kwargs):
	    if not self.id:
	        self.slug = slugify(self.title)
	    super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title