from django.contrib import admin
from django.forms import ModelChoiceField

from .models import *
from django import forms


class NotebookCategoryChoiseField(forms.ModelChoiceField):
    pass
#Для костомной логики оставил. А так как в смортфоне можно сразу класс ModelChoiceField

class NoteBookAdmin(admin.ModelAdmin):

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
