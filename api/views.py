from django.shortcuts import get_object_or_404, get_list_or_404
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Plan, User


def index(request):
    return JsonResponse({'status':'ok'})


def get_plans(request):
    plans = get_list_or_404(Plan)
    response = {'data':[model_to_dict(plan) for plan in plans]}
    return JsonResponse(response, json_dumps_params={'indent':4})


def plans_by_user(request, uid):
    plans = get_list_or_404(Plan, user_id=uid)
    response = {'data':[model_to_dict(plan) for plan in plans]}
    return JsonResponse(response, json_dumps_params={'indent':4})


def plan_by_id(request, pid):
    plan = model_to_dict(get_object_or_404(Plan, id=pid))
    response = {'data':plan}
    return JsonResponse(response, json_dumps_params={'indent':4})


def get_users(request):
    users = get_list_or_404(User)
    response = {'data':[model_to_dict(user) for user in users]}
    return JsonResponse(response, json_dumps_params={'indent':4})


def user_by_id(request, uid):
    user = model_to_dict(get_object_or_404(User, id=uid))
    response = {'data':user}
    return JsonResponse(response, json_dumps_params={'indent':4})