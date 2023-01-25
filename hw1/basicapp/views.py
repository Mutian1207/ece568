from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    CreateView,UpdateView,DetailView,RedirectView
                                    )

# Create your views here.
class IndexView(TemplateView):
    template_name = "homepage.html"

