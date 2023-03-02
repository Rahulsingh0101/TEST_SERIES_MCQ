from django.contrib import admin

# Register your models here.

from app.models import *

@admin.register((Questions))
class QuestionsModelAdmin(admin.ModelAdmin):
    list_display=['question','option_1','option_2','option_3','option_4','correct_ans']                 

