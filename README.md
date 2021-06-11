# README

[TOC]

##安装环境

#### Python version: 3.8.2

#### Django version: 2.2.11

```shell
pip install django-easy-pdf
pip install reportlab
pip install django-simple-captcha
```

## TODO

- student opeartion
- search course
- form css



python manage.py makemigrations
python manage.py migrate

## TIPS

#### account

Teahcer:
任猎城
u: 1280000001
p: 12345678
镇天稽
u: 1110000001
p: 22334455
爱嘤诗贝伦
u: 1160000001
p: 12341234
牛有力
u: 2660000001
p: password



Student:
李大爽
u: 2020000001
p: libigshuang

张三
u: 2018000001
p: zhang333


2044000001
three12345

2020000002
xiaored



## Problems

#### 1 如何给Class-Based Views 的as_view()生成的view方法里面传参。

比如UpdateTeacherView和UpdateStudentView里面获取不到view方法传入的其他参数
解决方法： 重写get_context_data()， 在里面先写入固定的参数