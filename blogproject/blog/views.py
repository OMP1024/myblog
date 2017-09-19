from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag
import markdown
from comments.forms import CommentForm

app_name = 'blog'
# Create your views here.
#  视图函数
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {'post_list':post_list}
    # 参数： request 模板 模板参数
    return render(request,'blog/index.html',context)

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,extensions=['markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc',])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post':post,
               'form':form,
               'comment_list':comment_list}
    return render(request,'blog/detail.html',context=context)


def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,created_time__month=module)
    return render(request,'blog/index.html',{'post_list':post_list})


def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list': post_list})


def get_tags(request,pk):
    tag = get_object_or_404(Tag,pk=pk)
    post_list = Post.objects.filter(tags__name__contains=tag)
    return render(request,'blog/index.html',{'post_list':post_list})