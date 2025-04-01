from django.shortcuts import render
from django.views import View
from datetime import datetime
from zoneinfo import ZoneInfo
from reminder.forms import PageForm
from reminder.models import routineModel



class IndexView(View):
  def get(self, request):
    datetime_now = datetime.now(
      ZoneInfo("Asia/Tokyo")
    ).strftime("%Y年%m月%d日")
    return render(request, "reminder/index.html", {"datetime_now": datetime_now})

index = IndexView.as_view()
