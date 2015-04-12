from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app01.models import BBS
# Create your views here.


def index(request):
    bbs_list = BBS.objects.all()
    return render_to_response('index.html', {'bbs_list': bbs_list})


def bbs_detail(request, bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj': bbs})
