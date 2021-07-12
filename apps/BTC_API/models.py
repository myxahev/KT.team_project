from django.db import models

# Create your models here.

"""models.DateTimeField()             # поле содержащее в себе Дату и Время
models.CharField(max_length=100)   # Текстовое поле ограниченной длины. Длина строки = xx символов
models.BooleanField()              # Поле содержащие в себе булево значение
models.ForeignKey()                # ссылка на внешнюю таблицу
models.PositiveIntegerField()      # положительное целое значение
models.URLField(max_length=100)     # ссылка на web страницу длина ссылки ограничена xx символами
models.DateField()                 # поле содержащие Дату"""

class Btc(models.Model):
  """
    table price BTC.
  """
  name = models.CharField(max_length=100)
  date_added = models.DateTimeField()
  last_updated = models.DateTimeField()
  price = models.PositiveIntegerField()
  volume_24h = models.PositiveIntegerField()
  percent_change_24h = models.CharField(max_length=100)

  def __unicode__(self):
    return self.name


