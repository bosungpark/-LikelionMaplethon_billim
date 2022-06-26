from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """
    빌림에서는 이메일 인증등의 세밀한 컨트롤은 진행하지 않는다.
    따라서 편의를 위해 AbstractBaseUser대신
    AbstractUser를 상속받아 모델을 구현한다.
    """
    email=models.CharField(max_length=500)
    address=models.CharField(max_length=500, null=True)
    coin=models.IntegerField(default=2)
