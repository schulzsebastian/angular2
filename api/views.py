from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Plan, User


def index(request):
    return JsonResponse({'status':'ok'})


def plan_by_id(request, pid):
    plan = model_to_dict(get_object_or_404(Plan, id=pid))
    return JsonResponse(plan)


def user_by_id(request, uid):
    user = model_to_dict(get_object_or_404(User, id=uid))
    return JsonResponse(user)