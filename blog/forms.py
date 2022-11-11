from django.db import models
from django.forms import fields
from .models import Post_image
from django import forms
from django.contrib.auth.forms import UserCreationForm


class post_images(forms.ModelForm):
	class Meta:
		model=Post_image
		fields=['image']