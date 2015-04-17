from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from app01.models import BBS
from django.template.context import RequestContext
from app01 import models
from django.contrib import comments
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
    models.BBS.objects.create(
        title='test title',
        summary='haha',
        content=content,
        author=author,
        view_count=1,
        ranking=1,
    )
    return HttpResponse('yes,you do it!')

# def Login():
#     pass
# def acc_login():

# def logout_view():
