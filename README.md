# django-webstack

![](https://camo.githubusercontent.com/cd5db39ba59752822b7770d5074571fc4db1660af9066dfdb9953ff53ed7195e/687474703a2f2f7777772e776562737461636b2e63632f6173736574732f696d616765732f707265766965772e676966)

一个导航APP，可以直接安装到django当做一个独立的应用，效果可以看我博客 https://tendcode.com/nav/

## 使用步骤

step 1 安裝包依赖

```bash
# 安装django-imagekit是为了上传网址logo
pip install Pillow==9.3.0
pip install django-imagekit==4.0.2
pip install django-webstack>=1.4.2
```

如果pip设置了非官方源（比如豆瓣源）导致安装失败，可能是没有同步官方的资源，此时可以临时设置成官方源试试:

```shell
pip install django-webstack>=1.4.2 --index-url https://pypi.org/simple --trusted-host pypi.org
```

step 2 配置中添加应用

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webstack',
]
```

step 3 生成数据表

```bash
python manage.py makemigrations
python manage.py migrate
```

step 4 添加到路由

```python
# 将应用路由添加到Django项目的根urls.py文件中

urlpatterns = [
    ...
    path('nav/', include(('webstack.urls', 'webstack'), namespace='webstack')),
]
```

step 5 前往管理界面添加数据即可显示到前台

应用会生成3张表，对应3个模型：一级菜单-二级菜单-导航网站，先添加一级菜单然后添加二级菜单，然后添加导航网址，一层一层关联即可，如果想要直接显示一级菜单，则可以添加一个跟一级菜单同名的二级菜单。

## 个性化配置（非必须）

应用本身安装就可以使用，但是你也可以自定义页面，包括页面的排版和静态资源都可以自定义，具体方式如下：

可以在项目跟目录的templates目录下创建一个webstack目录，并在其中创建一个index.html文件，用来覆盖原应用的index.html文件，原文件的内容自行查看代码，可以参考我项目的修改：https://github.com/Hopetree/izone/blob/master/templates/webstack/index.html

```html
{% extends 'webstack/base.html' %}
{% load static %}

{% block title %}程序员网址导航_TendCode{% endblock %}

{% block meta %}
<link rel="shortcut icon" href="{% static 'blog/img/favicon.ico' %}" type="image/x-icon"/>
<meta name="keywords" content="程序员网址导航,网址收藏,tendcode.com">
<meta name="description" content="程序员常用网址导航聚合站">
{% endblock %}

{% block top-file %}{% endblock %}

{% block logo %}
<div class="logo">
    <a href="{% url 'webstack:webstack_index' %}" class="logo-expanded">
        <img src="{% static 'blog/img/nav-logo.png' %}" height="40" alt=""/>
    </a>
    <a href="{% url 'webstack:webstack_index' %}" class="logo-collapsed">
        <img src="{% static 'webstack/assets/images/logo-collapsed@2x.png' %}" height="40" alt=""/>
    </a>
</div>
{% endblock %}

{% block navbar-list %}
<li style="min-height: 75px;"><a href="{% url 'blog:index' %}">首页</a></li>
<li style="min-height: 75px;"><a href="{% url 'blog:subject_index' %}">博客专题</a></li>
<li style="min-height: 75px;"><a href="{% url 'tool:total' %}">在线工具</a></li>
<li style="min-height: 75px;"><a href="{% url 'blog:about' %}">关于</a></li>
{% endblock %}

{% block main-menu %}{% endblock %}

{% block footer %}
<div class="footer-text">
    &copy; {{ this_year }}
    <a href="https://github.com/Hopetree/django-webstack">
        <strong>django-webstack</strong>
    </a>
    design by
    <a href="https://github.com/Hopetree" target="_blank">
        <strong>Hopetree</strong>
    </a>
</div>
{% endblock %}
```

拓展功能：

1. 菜单和网站都是可以后台动态添加的，包括网站的logo图标上传
2. 页面布局可以使用Django的模板个性化调整，静态文件也是
3. 图标库使用cdn，bootstrp也是cdn，加快网站访问
4. 网站添加了属性用来记录网站的可用状态，Django用到定时任务的可以添加定时任务更新网站状态，将不可访问网站标记为不显示，页面就不会显示，定时任务自动刷新状态，保证网站都是可访问的

你可以自定义网页标题、关键词和描述，并且可以添加自定义的静态文件包括css和js文件，并且可以自定义页面额外的菜单，一级页脚，甚至整个页面的排版。

## 原项目地址

本项目是基于Webstack网址导航项目改变而来，将静态导航网站改成了有后台的Django项目，原项目地址如下：

https://github.com/WebStackPage/WebStackPage.github.io

