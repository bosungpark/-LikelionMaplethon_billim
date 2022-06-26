from django.contrib.auth.forms import UserCreationForm
from ..models.user_model import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','address']
        labels = {
            'username' : '아이디',
            'password1' : '패스워드',
            'password2' : '패스워드2',
            'email' : '이메일',
            'address':'주소',
        }
