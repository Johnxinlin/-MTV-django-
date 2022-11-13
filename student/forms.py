from django import forms

from student.models import Student, StudentDetail


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密码',
                               max_length=15,
                               min_length=4,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': '请输入长度为0-15位的密码'
                               }),
                               error_messages={
                                   'max_length': '密码长度大于15位',
                                   'min_length': '密码长度小于6位',
                               }
                               )


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密码',
                               max_length=15,
                               min_length=6,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': '请输入长度为0-15位的密码'
                               }),
                               error_messages={
                                   'max_length': '密码长度大于15位',
                                   'min_length': '密码长度小于6位',
                               }
                               )
    password_repeat = forms.CharField(label='再次输入密码',
                                      widget=forms.PasswordInput()
                                      )
    email = forms.EmailField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            msg = '密码不一致'
            self.add_error(password_repeat, msg)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['is_delete']


class StudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        exclude = ['student']

    def clean_num(self):
        data = self.cleaned_data.get('num')
        if not data[:-1].isdigit():
            self.add_error('num', '您输入的身份证号码格式有误')
            # raise forms.ValidationError('您输入的身份证号码格式有误')
        return data
