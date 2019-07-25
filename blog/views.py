from django.shortcuts import render,redirect,get_object_or_404
from .forms import BlogForm,BlogEditForm
from .models import Blog
from django.urls import reverse

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def blog_create(request):
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        dave=form.save(commit=False)
        dave.user=request.user
        dave.save()
        return redirect(reverse('blog:blog_list'))
    else:
        form=BlogForm()
        args={'form':form}
        return render(request, 'blog/blog_create.html', args)


def blog_list(request):
    contents=Blog.objects.all()
    query=request.GET.get("q")
    print(query)

    if query:
        print("hey baby")
        contents=contents.filter(Q(type__startswith=query)|Q(Heading__startswith=query)|Q(caption__icontains=query))

    paginator = Paginator(contents, 3)  # Show 25 contacts per page

    page = request.GET.get('page')
    contents = paginator.get_page(page)
    try:
        contents=paginator.page(page)
    except PageNotAnInteger:
        contents=paginator.page(1)
    except EmptyPage:
        contents=paginator.page(paginator.num_pages)
    args = {'contents': contents}

    return render(request, 'blog/blog_list.html', args)


def blog_full(request,pk):

    content = Blog.objects.get(pk=pk)
    args = {'content': content}
    return render(request, 'blog/blog_full.html', args)

def blog_edit(request,pk):
    user = request.user
    instance = get_object_or_404(Blog, user=user,pk=pk)
    if request.method == 'POST':
        form=BlogEditForm(request.POST,request.FILES,instance=instance)
        madhur=form.save(commit=False)
        madhur.user=request.user
        madhur.save()
        return redirect(reverse('blog:blog_list'))
    else:
        form=BlogEditForm(instance=request.user)
        args={'form':form,'user':request.user}
        return render(request,'blog/blog_edit.html',args)


def myblog(request):
    user=request.user

    myblogs=Blog.objects.filter(user=user)
    return render(request, 'blog/myblog.html', {'myblogs':myblogs})
