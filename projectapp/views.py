from functools import reduce
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Comment, FreeComment, Post, FreePost, GENDER_CHOICES, COUNT_CHOICES, TOPIC_CHOICES, MODE_CHOICES
from django.conf import settings
from django.conf.urls.static import static
from django.db.models import Q

def home(request, posts_filtered=None):
    # posts = Post.objects.all()

    context = {}

    login_session = request.session.get('login_session', '')

    print(login_session)

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    posts = Post.objects.filter().order_by('-date') if posts_filtered == None else posts_filtered
    return render(request, 'index.html', {'posts':posts, 'gender': GENDER_CHOICES, 'count': COUNT_CHOICES, 'topic': TOPIC_CHOICES, 'context': context['login_session']})

def filterpost(request):
    posts_filtered = ()

    needed_filter = {}

    if 'gender' in request.GET:
        needed_filter['gender'] = Post.objects.all().filter(gender=request.GET['gender'])
    
    if 'count' in request.GET and request.GET['count'] != "상관없음":
        needed_filter['count'] = Post.objects.all().filter(count=request.GET['count'])

    if 'topic' in request.GET and request.GET['topic'] != "상관없음":
        needed_filter['topic'] = Post.objects.all().filter(topic=request.GET['topic'])

    new_li = set(needed_filter.values())
    print(new_li)

    if len(new_li) != 0:
        posts_filtered = set.intersection(*map(set, new_li))

    print(posts_filtered)

    if request.GET['gender'] == "상관없음" and request.GET['count'] == "상관없음" and request.GET['topic'] == "상관없음":
        posts_filtered = None
    

    return home(request, posts_filtered)

def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.session.get('login_session', '')
            obj.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def postupdate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return detail(request, post_id)
        else:
            return redirect('home')
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form': form, 'post':post})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form': comment_form})

# 댓글 저장
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.author = request.session.get('login_session', '')
        finished_form.save()
    return redirect('detail', post_id)

def commentupdate(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return detail(request, comment.post.id)
        else:
            return redirect('home')
    else:
        form = CommentForm(instance=comment)
        return render(request, 'editcomment.html', {'form': form, 'comment':comment})

def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return detail(request, comment.post.id)


def freehome(request, posts_filtered=None):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date') if posts_filtered == None else posts_filtered

    context = {}

    login_session = request.session.get('login_session', '')

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    return render(request, 'free_index.html', {'freeposts': freeposts, 'mode': MODE_CHOICES, 'context' : context['login_session']})

def filterfreepost(request):
    posts_filtered = []

    if 'mode' in request.GET and request.GET['mode'] != "":
        posts_filtered = FreePost.objects.all().filter(mode=request.GET['mode'])
    else:
        posts_filtered = None

    return freehome(request, posts_filtered)
        
    


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.session.get('login_session', '')           # user 추가!
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})

def freepostupdate(request, post_id):
    post = get_object_or_404(FreePost, pk=post_id)
    if request.method == 'POST':
        form = FreePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return freedetail(request, post_id)
        else:
            return redirect('freehome')
    else:
        form = FreePostForm(instance=post)
        return render(request, 'freeedit.html', {'form': form, 'post':post})

def freepostdelete(request, post_id):
    post = get_object_or_404(FreePost, pk=post_id)
    post.delete()
    return redirect('freehome')


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.author = request.session.get('login_session', '')  
        finished_form.save()
    return redirect('freedetail', post_id)

def freecommentupdate(request, comment_id):
    comment = get_object_or_404(FreeComment, pk=comment_id)
    if request.method == 'POST':
        form = FreeCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return freedetail(request, comment.post.id)
        else:
            return redirect('freehome')
    else:
        form = FreeCommentForm(instance=comment)
        return render(request, 'freeeditcomment.html', {'form': form, 'comment':comment})

def freecommentdelete(request, comment_id):
    comment = get_object_or_404(FreeComment, pk=comment_id)
    comment.delete()
    return freedetail(request, comment.post.id)


    