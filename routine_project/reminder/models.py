from django.db import models
from django.core.validators import MinValueValidator

class routineModel(models.Model):
 id=models.AutoField(primary_key=True, verbose_name='ID')
 title=models.CharField(max_length=100, verbose_name='タイトル')
 period=models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)], help_text='例：7 = 毎週、30 = 毎月', verbose_name='周期')
 create_at=models.TimeField(auto_now_add=True, verbose_name='作成日時')
 url=models.URLField(null=True, blank=True, verbose_name='URL')
 notice_text=models.TextField(max_length=400, verbose_name='通知内容')

 def __str__(self):
  return f"{self.title} ({self.period}日ごと)"
