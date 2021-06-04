# usr/bin/env python
# -*- coding:utf-8- -*-
from captcha.fields import CaptchaField
from django import forms
from .models import Student, Teacher


class StuLoginForm(forms.Form):
    uid = forms.CharField(label='学号', max_length=10)
    password = forms.CharField(label='密码', max_length=30, widget=forms.PasswordInput)
    captcha = CaptchaField(label='验证码')
    #添加学生登录验证码模型

class TeaLoginForm(forms.Form):
    uid = forms.CharField(label='教职工号', max_length=10)
    password = forms.CharField(label='密码', max_length=30, widget=forms.PasswordInput)
    captcha = CaptchaField(label='验证码')
    #添加老师登录验证码模型


class StuRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="确认密码")

    class Meta:
        model = Student
        fields = ('grade',
                  'name',
                  'password',
                  'confirm_password',
                  'gender',
                  'birthday',
                  'email',
                  'info')

    def clean(self):
        cleaned_data = super(StuRegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if confirm_password != password:
            self.add_error('confirm_password', 'Password does not match.')

        return cleaned_data


class StuUpdateForm(StuRegisterForm):
    class Meta:
        model = Student
        fields = ('name',
                  'password',
                  'confirm_password',
                  'gender',
                  'birthday',
                  'email',
                  'info')


class TeaRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="确认密码")

    class Meta:
        model = Teacher
        fields = ('name',
                  'password',
                  'confirm_password',
                  'gender',
                  'birthday',
                  'email',
                  'info')

    def clean(self):
        cleaned_data = super(TeaRegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if confirm_password != password:
            self.add_error('confirm_password', 'Password does not match.')