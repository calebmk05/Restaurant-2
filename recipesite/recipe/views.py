from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models


class RecipeListView(ListView):
    model = models.recipe
    template_name = 'recipe/home.html'
    context_object_name ='recipe'

class RecipeDetailView(DetailView):
    model = models.recipe


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.recipe
    fields = ['title', 'description', 'image', 'ingredients', 'method', 'meal_type', 'meal_diet', 'meal_holiday']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.recipe
    fields = ['title', 'description', 'image', 'ingredients', 'method', 'meal_type', 'meal_diet', 'meal_holiday']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class NavbarRecipe(ListView):
    model = models.MealType
    template_name = 'recipe/base.html'
    context_object_name = 'mealtype'

    def get_names(self):
        return list(self.get_queryset().values_list('meal', flat=True))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = self.get_names()
        return context
    

def meal_display(request, meal_id):
    meal = get_object_or_404(models.MealType, pk=meal_id)
    meals_in_category = models.recipe.objects.filter(meal_type=meal)

    context ={
        'meal': meal,
        'meal_type': meals_in_category,
    }

    return render(request, 'recipe/recipes.html', context)
