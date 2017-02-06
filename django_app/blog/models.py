from django.db import models
from django.utils import timezone


# 모델을 정의 (모델은 객체의 종류)
# models.Model은 Post가 장고 모델임을 의미
# 장고는 Post가 데이터베이스에 저장되어야 하는걸 알게 됨
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
