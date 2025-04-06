from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from datetime import datetime
from zoneinfo import ZoneInfo
from reminder.forms import PageForm
from reminder.models import routineModel
from .utils import get_next_date
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(LoginRequiredMixin, View):
  def get(self, request):
    datetime_now = datetime.now(
      ZoneInfo("Asia/Tokyo")
    ).strftime("%Y年%m月%d日")
    return render(request, "reminder/index.html", {"datetime_now": datetime_now})

class PageCreateView(LoginRequiredMixin, View):
  def get(self, request):
    form = PageForm()
    return render(request, "reminder/page_form.html", {"form": form})

  def post(self, request):
    form = PageForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("reminder:index")
    return render(request, "reminder/page_form.html", {"form": form})

class PageListView(LoginRequiredMixin, View):
  def get(self, request):
    page_list = routineModel.objects.order_by('-create_at')
    enriched = []
    for page in page_list:
      next_date = get_next_date(page.start_date, page.period)
      start_date_str = page.start_date.strftime("%Y年%m月%d日")
      if next_date:
        next_date_str = next_date.strftime("%Y年%m月%d日")
      else:
        next_date_str = "なし"

      enriched.append({
        "page": page,
        "next_date": next_date_str,
        "start_date": start_date_str
      })
    return render(request, "reminder/page_list.html", {"page_list": enriched})

class PageDeleteView(LoginRequiredMixin, View):
  def get(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    return render(request, "reminder/page_delete.html", {"page" : page})
  def post(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    page.delete()
    return redirect('reminder:page_list')

class PageUpdateView(LoginRequiredMixin, View):
  def get(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    form = PageForm(instance=page)
    return render(request, 'reminder/page_update.html', {"form": form, "page": page})
  def post(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    form = PageForm(request.POST, instance=page)
    if form.is_valid():
      form.save()
      return redirect('reminder:page_detail', id=page.id)
    return render(request, 'reminder/page_update.html', {"form": form, "page": page})

class PageDetailView(LoginRequiredMixin, View):
  def get(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    return render(request, 'reminder/page_detail.html', {"page": page})




index = IndexView.as_view()
create_view = PageCreateView.as_view()
list_view = PageListView.as_view()
detail_view = PageDetailView.as_view()
delete_view = PageDeleteView.as_view()
update_view = PageUpdateView.as_view()
