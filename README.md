# README

[TOC]

## 安装依赖环境
### 1.导入第三方库
```shell
#这里用的清华源，可以自行更改
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### 2.启动时的疑难杂症
>ps:若启动出现`No module named 'django.utils.six'`情况

1. 前提确认安装第三方库`six`，可以先`pip install six`看看
2. 找到第三方库安装位置`site-packages`中找到six.py
3. 将`six.py`复制到`django/utils`下即可

## TODO

- student opeartion
- search course
- form css

```shell
python manage.py makemigrations
python manage.py migrate
```

## TIPS

#### account
```text
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
```

## Problems

#### 1 如何给Class-Based Views 的as_view()生成的view方法里面传参。

比如UpdateTeacherView和UpdateStudentView里面获取不到view方法传入的其他参数
解决方法： 重写get_context_data()， 在里面先写入固定的参数