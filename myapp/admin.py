from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm

from .models import *
from django import forms


class NotebookAdminForm(ModelForm):
    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображения с минимальным разрешением {}x{}'.format(
            *self.MIN_RESOLUTION)


class NotebookCategoryChoiseField(forms.ModelChoiceField):
    pass


# Для костомной логики оставил. А так как в смортфоне можно сразу класс ModelChoiceField

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
