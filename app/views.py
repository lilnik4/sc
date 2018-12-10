from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView


from django.views.generic import CreateView
from .models import Match, Rating, Match2, Rating2,Rules
from .forms import RatingForm, Rating2Form

def rating_view(request):
    match = None
    match2 = None
    form = None
    form2= None
    rule = Rules.objects.all()
    if Match.objects.filter(active=True).count() > 0:
        match = Match.objects.filter(active=True)[0]

    if Match2.objects.filter(active=True).count() > 0:
        match2 = Match2.objects.filter(active=True)[0]

    if request.method == 'POST':
        if match != None:
            form = RatingForm(request.POST)
        elif match2 != None:
            form2 = Rating2Form(request.POST)

        if form and form.is_valid():
            rating = form.save()
            return redirect('/done')

        if form2 and form2.is_valid():
            rating = form2.save()
            return redirect('/done')


    else:
        if match != None:
            form = RatingForm()
        elif match2 != None:
            form2 = Rating2Form()

    return render(request, 'app/index.html', {'form':form,
                                              'form2':form2,
                                              'match': match,
                                              'match2': match2,
                                              'rule': rule})

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


def result_view(request):
    match = Match.objects.all()
    match2 = Match2.objects.all()
    rating = Rating.objects.all()
    rating2 = Rating2.objects.all()

    return render(request, 'app/results.html', {'match2':match2,
                                                'match':match,
                                                'rating':rating,
                                                'rating2':rating2})
