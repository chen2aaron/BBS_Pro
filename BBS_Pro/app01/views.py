from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import comments
from django.contrib.auth.forms import *
from app01.models import BBS
from app01 import models
# Create your views here.


def index(request):
    bbs_list = BBS.objects.all()
    bbs_categories = models.Category.objects.all()
    return render_to_response(
        'index.html', {'bbs_list': bbs_list,
                       'user': request.user,
                       'bbs_category': bbs_categories,
                       }
    )


def category(request, cate_id):
    bbs_list = models.BBS.objects.filter(category__id=cate_id)
    bbs_categories = models.Category.objects.all()
    return render_to_response(
        'index.html', {'bbs_list': bbs_list,
                       'user': request.user,
                       'bbs_category': bbs_categories,
                       'cate_id': int(cate_id), }
    )


def bbs_detail(request, bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    return render_to_response(
        'bbs_detail.html',
        {'bbs_obj': bbs},
        context_instance=RequestContext(request)
    )


def sub_comment(request):
    print request.POST
    bbs_id = request.POST.get('bbs_id')

    comment = request.POST.get('comment_content')
    comments.models.Comment.objects.create(
        content_type_id=7,
        object_pk=bbs_id,
        site_id=1,
        user=request.user,
        comment=comment,
    )
    return HttpResponseRedirect(
        '/detail/%s' % bbs_id,
    )


def bbs_pub(request):
    return render_to_response(
        'bbs_pub.html',
        context_instance=RequestContext(request)
    )


def bbs_sub(request):
    print ',====>', request.POST.get('content')
    content = request.POST.get('content')
    author = models.BBS_user.objects.get(
        user__username=request.user)
    category = request.POST.get('category')
    models.BBS.objects.create(
        category=category,
        title='test title',
        summary='haha',
        content=content,
        author=author,
        view_count=1,
        ranking=1,
    )
    return HttpResponse('yes,you do it!')


def register(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render_to_response(
            'register.html', {'form': form},
            context_instance=RequestContext(request)
        )
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # auto login
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect("/")
            return render_to_response(
                'register.html', {'form': form},
                context_instance=RequestContext(request)
            )
# def Login():
#     pass
# def acc_login():

# def logout_view():
