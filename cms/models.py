from django.db import models


# Create your models here.
class Improvement(models.Model):
    """改善"""
    name = models.CharField('名前', max_length=255)
    subject = models.CharField('件名', max_length=255)
    done_date = models.DateField('処置完了日')
    boss_confirmation = models.DateField('上司確認')

    def __str__(self):
        return self.name


class Hh(models.Model):
    """ヒヤリハット"""
    hh = models.ForeignKey(Improvement, verbose_name='改善', related_name='hhat')
    comment = models.TextField('内容', blank=True)

    def __str__(self):
        return self.comment
