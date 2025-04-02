from django.shortcuts import render, redirect
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

class PageCreateView(View):
  def get(self, request):
    form = PageForm()
    return render(request, "reminder/page_form.html", {"form": form})

  def post(self, request):
    form = PageForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("reminder:index")
    return render(request, "reminder/page_form.html", {"form": form})

index = IndexView.as_view()
create_view = PageCreateView.as_view()
