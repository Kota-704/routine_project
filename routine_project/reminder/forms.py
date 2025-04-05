from django.forms import ModelForm
from reminder.models import routineModel

class PageForm(ModelForm):
  class Meta:
    model = routineModel
    fields = ["title", "period", "start_date", "url", "notice_text" ]
