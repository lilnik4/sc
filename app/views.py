from django.shortcuts import render
from django.views.generic import TemplateView, ListView


from django.views.generic import CreateView
from .models import Match, Rating


class RatingView(CreateView):
    model = Rating

    fields = ['user','score_1', 'score_2']
    template_name = 'app/index.html'
    success_url = "/done"

    def get_context_data(self, **kwargs):
        context = super(RatingView, self).get_context_data(**kwargs)
        context['match'] = Match.objects.filter(active=True).first()
        return context

    def form_valid(self, form):
        from django.db import IntegrityError
        try:
            return super(RatingView, self).form_valid(form)
        except IntegrityError:
            from django import forms
            form.add_error("username", "User already exists")
            return self.form_invalid(form)


class DoneView(TemplateView):
    template_name = 'app/done.html'


class ResultView(ListView):
    model = Rating
    template_name = 'app/results.html'
