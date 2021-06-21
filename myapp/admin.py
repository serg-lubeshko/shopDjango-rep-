from PIL import Image
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField, ModelForm
from django.http import request
from django.utils.safestring import mark_safe

from .models import *
from django import forms


class NotebookAdminForm(ModelForm):
    # MIN_RESOLUTION = (100, 100)
    # MAX_RESOLUTION = (800, 800)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style= "color:red">При загрузке изображения с разрешением больше {}x{} оно будет обрезано</span>'.format(
                *Product.MAX_RESOLUTION))

    def clean_image(self):
        images = self.cleaned_data['image']  # в переменных  images и  im метод size разное значение
        im = Image.open(images)
        width, height = im.size
        # min_width, min_height = self.MIN_RESOLUTION
        # max_width, max_height = self.MAX_RESOLUTION
        min_width, min_height = Product.MIN_RESOLUTION  # в стр 26 и 28 одно и тое. Просто работаем через модель
        max_width, max_height = Product.MAX_RESOLUTION
        if width < min_width or height < min_height:
            raise ValidationError('Разрешение изображения должен быть больше 100х100')
        if width > max_width or height > max_height:
            raise ValidationError('Разрешение изображения должен быть меньше 800х800')
        if images.size > Product.MAX_SIZE:
            raise ValidationError('Размер изображения должно быть меньше 3М')


class NotebookCategoryChoiseField(forms.ModelChoiceField):
    pass


# Для костомной логики оставил. А так как в смартфоне можно сразу класс ModelChoiceField

class NoteBookAdmin(admin.ModelAdmin):
    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiseField(Category.objects.filter(slug='Noutbuki'))
        return super().formfield_for_foreignkey(self, db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(pk=2))
        return super().formfield_for_foreignkey(self, db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NoteBookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
