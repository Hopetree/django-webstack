from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.

# 菜单父模型
class BaseMenu(models.Model):
    name = models.CharField('名称', max_length=10)
    icon = models.CharField('图标', max_length=30)
    sort_order = models.IntegerField('排序', default=99, help_text='自定义排序')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        """这是一个元类，用来继承的"""
        abstract = True

    def __str__(self):
        return self.name


class FirstMenu(BaseMenu):
    class Meta:
        verbose_name = '一级菜单'
        verbose_name_plural = verbose_name
        ordering = ['sort_order']

    def get_second_menu_list(self):
        return SecondMenu.objects.filter(father=self).exclude(name=self.name).order_by('sort_order')

    def has_site(self):
        """判断一级菜单下面是否有网站"""
        num = 0
        for second_menu in self.second_menus.all():
            num += second_menu.navigation_sites.count()
        return num


class SecondMenu(BaseMenu):
    father = models.ForeignKey(FirstMenu, verbose_name='父菜单', on_delete=models.PROTECT,
                               related_name='second_menus')

    class Meta:
        verbose_name = '二级菜单'
        verbose_name_plural = verbose_name
        ordering = ['sort_order']

    def get_site_list(self):
        return NavigationSite.objects.filter(menu=self).order_by('sort_order')


class NavigationSite(models.Model):
    name = models.CharField('名称', max_length=30)
    description = models.CharField('描述', max_length=100)
    link = models.URLField('网站地址', max_length=150)
    sort_order = models.IntegerField('排序', default=99, help_text='自定义排序')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    logo = ProcessedImageField(upload_to='web/upload/%Y/%m/%d/',
                               default='web/default/default.png',
                               verbose_name='Logo',
                               processors=[ResizeToFill(50, 50)],
                               help_text='上传图片大小建议使用1:1的宽高比，为了清晰度原始图片宽度应该超过50px'
                               )

    menu = models.ForeignKey(SecondMenu, verbose_name='所属二级菜单', on_delete=models.PROTECT,
                             related_name='navigation_sites')

    class Meta:
        verbose_name = '导航网站'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']
