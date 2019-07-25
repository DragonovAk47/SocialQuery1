from django.views.generic import TemplateView
from home.forms import PostForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from home.models import Picture,Post,Friend
from datetime import datetime
from django.urls import reverse
class HomeView(TemplateView):
    template_name='home/home.html'

    def get(self,request):
        posts=Post.objects.all().order_by('-date')
        users=User.objects.exclude(id=request.user.id)
        friend,created=Friend.objects.get_or_create(current_user=request.user)
        friends=friend.users.all()
        args = {'posts' :posts,'users': users,'friends': friends}
        return render(request,self.template_name,args)

    def post(self,request):
        pass




def post_create(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        dave=form.save(commit=False)
        dave.user=request.user
        dave.save()
        return redirect(reverse('home:home'))
    else:
        form=PostForm()
        args={'form':form}
        return render(request, 'home/post_create.html', args)



def change_friend(request,operation,pk):
    new_friend=User.objects.get(pk=pk)
    if operation=='add':
       Friend.add_friend(request.user,new_friend)
       Friend.add_friend(new_friend,request.user)
    if operation=='remove':
        Friend.lose_friend(request.user,new_friend)
        Friend.lose_friend(new_friend, request.user)
    return redirect(reverse('home:home'))

def friends_list(request,pk):
    user = User.objects.get(pk = pk)
    current = Friend.objects.get(current_user = user)
    friends = current.users.all()
    return render(request,'home/friends_list.html',{'friends':friends})
