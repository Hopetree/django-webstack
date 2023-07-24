# django-webstack

一个导航APP，可以直接安装到django当做一个独立的应用，效果可以看我博客 https://tendcode.com/nav/

step 1 安裝包依赖

```bash
pip install Pillow==9.3.0
pip install django-imagekit==4.0.2
pip install django-webstack
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
urlpatterns = [
    path('nav/', include('webstack.urls')),
]
```

step 5 前往管理界面添加数据即可显示到前台

