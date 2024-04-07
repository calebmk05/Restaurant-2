from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class MealType(models.Model):
    meal = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.meal
    
class MealDiet(models.Model):
    diet = models.CharField(max_length=50)

    def __str__(self):
        return self.diet
    
class HolidayMeal(models.Model):
    holiday = models.CharField(max_length=50)

    def __str__(self):
        return self.holiday
        

     
    


from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class recipe(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to="recipe_images", null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    ingredients = models.TextField(null=True)
    method = models.TextField(null=True)

    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE, null=True)
    meal_diet = models.ManyToManyField(MealDiet, help_text="Hold ctrl or cmd to select more than one option")
    meal_holiday = models.ManyToManyField(HolidayMeal, help_text="Hold ctrl or cmd to select more than one option")

    def get_absolute_urls(self):
        return reverse("recipe-detail", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title

