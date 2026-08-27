from django.views.generic import TemplateView

class AccueilView(TemplateView):
    template_name = "vitrine/accueil.html"