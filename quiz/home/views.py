from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from.models import *
import random
# Create your views here.

def home(request):
    return HttpResponse ("Hello from Django")
    

def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        data = []
        random.shuffle(list(question_obj))
        for question_obj in question_objs:
            print(question_obj.get_answers())
            data.append({
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks":question_obj.marks,
                "answers":question_obj.get_answers(),
            })
        payload = {'status' : True,'data' : data}

        return JsonResponse(payload)
    
    except Exception as e :
        print(e)
    return HttpResponse("Something went wrong")