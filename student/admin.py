from django.contrib import admin

# Register your models here.
from .models import Student, StudentDetail


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'age', 'qq', 'phone']
    list_display_links = ['name']  # 通过哪个字段进行跳转
    list_filter = ['sex', 'name']   # 过滤
    search_fields = ['name', 'qq', 'phone']
    list_per_page = 3

    # fields = ['sex', 'name']    # 只允许修改的字段
    # exclude = ['qq']    # 排除的字段

    # 分组
    fieldsets = [
        (None, {'fields': ['name', 'sex']}),
        ('详细信息', {'fields': ['qq', 'phone']}),
        ('设置', {'fields': ['is_delete']})
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentDetail)
