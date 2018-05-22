from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from comments.forms import CommentForm
from.models import post,Category
import markdown
def index(request):
	post_list=post.objects.all()
	return render(request,'blog/index.html',context={'post_list':post_list})
	# return HttpResponse('欢迎访问我的首页')
# Create your views here.
# def detail(request,pk):
# 	post=get_object_or_404(post,pk=pk)
# 	return render(request,'blog/detail.html',context={'post':post})
def detail(request, pk):
    p=get_object_or_404(post, pk=pk)
    p.body =markdown.markdown(p.body,
    	                      extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = p.comment_set.all()
    context = {'post': p,
               'form': form,
               'comment_list': comment_list
               }


    return render(request, 'blog/detail.html', context=context)

def archives(request,year,month):
    post_list=post.objects.filter(created_time__year=year,
                                  created_time__month=month
                                  ).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list = post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

    