from django.db import models
from django.shortcuts import reverse
from time import time
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from model_utils import Choices
def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
def set_slug():
    return gen_slug('page')
class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, blank=True, unique=True, default=set_slug)
    body = RichTextField()
    date_pub = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}'.format(self.title)

class Vacancy(models.Model):
    EDUC_CHOICES = Choices('Высшее','Средне-техническое','Начальное-профессиональное','Среднее','Среднее общие')
    title = models.CharField(max_length=150,verbose_name='название')
    education = models.CharField(choices=EDUC_CHOICES, blank=True,max_length=150, db_index=True, verbose_name='образование')
    requires = RichTextField(verbose_name='требования')
    duties = RichTextField(default='', verbose_name='обязанности')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'вакансию'
        verbose_name_plural = 'вакансии'
