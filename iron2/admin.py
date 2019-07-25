from django.contrib import admin
from iron2.models import UserProfile

# Register your models here
# .
class UserProfileAdmin(admin.ModelAdmin):
  list_display=('user','Website','Mobile','user_info')
  search_list=('Mobile','description',)
  list_display_links=('user_info',)
  list_editable=('Website',)

  def user_info(self,obj):
      return obj.description

  def get_queryset(self,request):
      queryset=super(UserProfileAdmin,self).get_queryset(request)
      queryset= queryset.order_by('Mobile')
      return queryset


admin.site.register(UserProfile,UserProfileAdmin)