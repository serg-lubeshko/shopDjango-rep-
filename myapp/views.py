from django.shortcuts import render
from django.views.generic import DetailView

from myapp.models import Notebook, Smartphone


def test_view(request):
    return render(request, 'myapp/base.html')




class ProductDetailView(DetailView):

    CT_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_CLASS[kwargs[ct_model]]
        queryset = self.model.objects.all()
    # model = Model
    # queryset = Model.objects.all()
    slug_field = 'slug'
    context_object_name = 'product'
    template_name = 'product-detail.html'
    slug_url_kwarg = 'slug'
