from django.shortcuts import render
from django.views.generic import TemplateView


from django.views.generic import CreateView
from .models import Match, Rating


class RatingView(CreateView):
    model = Rating

    fields = ['user','score_1', 'score_2']
    template_name = 'app/index.html'
    success_url = "/felan/bahman"

    def get_context_data(self, **kwargs):
        context = super(RatingView, self).get_context_data(**kwargs)
        context['match'] = Match.objects.filter(active=True).first()
        return context