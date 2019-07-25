from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from  django.contrib.auth.forms  import PasswordChangeForm
from iron2.forms import RegForm,EditForm,DocumentForm,UserProfileForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.views.generic import TemplateView
from iron2.models import UserProfile,Document
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

def register(request):
  if(request.method=='POST'):
      form=RegForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect(reverse('iron2:login'))
  else:
      form=RegForm()
      args={'form':form}
      return render(request,'iron2/reg_form.html',args)


def profile(request,pk=2):
  if(pk):
    user = User.objects.get(pk=pk)
    userprofil=UserProfile.objects.get(user=user)
    print(pk)
  else:
      user=request.user
      userprofil = UserProfile.objects.get(user=user)

  args = {'user':user,'userprofile':userprofil}
  return render(request,'iron2/profile.html',args)

def edit_form(request):
  if(request.method=='POST'):
      form=EditForm(request.POST,instance=request.user)
      if form.is_valid():
          form.save()
          return redirect(reverse('home:home'))
  else:
      form=EditForm(instance=request.user)
      args={'form':form}
      return render(request,'iron2/edit_form.html',args)

def change_password(request):
  if(request.method=='POST'):
      form=PasswordChangeForm(data=request.POST,user=request.user)
      if form.is_valid():
          form.save()
          return redirect(reverse('iron2:login'))
  else:
      form=PasswordChangeForm(user=request.user)
      args={'form':form}
      return render(request,'iron2/change_password.html',args)

def UserProfileView(request):
    user=request.user
    instance=get_object_or_404(UserProfile,user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            madhur = form.save(commit=False)
            madhur.user = request.user
            madhur.save()
            return redirect(reverse('home:home'))
    else:
        user = request.user
        instance = get_object_or_404(UserProfile, user=user)
        form = UserProfileForm(instance=instance)


        documentantions = UserProfile.objects.all()

        args = {'form': form, 'documentantion': documentantions}
        return render(request, 'iron2/user.html', args)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = DocumentForm()
        documents=Document.objects.last()
        documen=Document.objects.all()
        args={'form': form,'documents':documents,'documen':documen}
        return render(request, 'iron2/model_form_upload.html',args )

def pdf_view(request,id):
    fs = FileSystemStorage(location='mark1/media/files')
    docum=Document.objects.get(id=id)
    print(docum.file.name[6:])
    filename = docum.file.name[6:]
    if fs.exists(filename):
            with fs.open(filename) as pdf:
                 print("hry i wsd")
                 response = HttpResponse(pdf, content_type='application/pdf')
                 response['Content-Disposition'] = 'attachment; filename=filename'
                 return response
    else:
            return HttpResponseNotFound('The requested pdf was not found in our server.')

