from django.shortcuts import render, redirect, get_object_or_404
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

class PageListView(View):
  def get(self, request):
    page_list = routineModel.objects.order_by('create_at')
    return render(request, "reminder/page_list.html", {"page_list": page_list} )

class PageDeleteView(View):
  def get(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    return render(request, "reminder/page_delete.html", {"page" : page})
  def post(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    page.delete()
    return redirect('reminder:page_list')

class PageUpdateView(View):
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

class PageDetailView(View):
  def get(self, request, id):
    page = get_object_or_404(routineModel, id=id)
    return render(request, 'reminder/page_detail.html', {"page": page})




index = IndexView.as_view()
create_view = PageCreateView.as_view()
list_view = PageListView.as_view()
detail_view = PageDetailView.as_view()
delete_view = PageDeleteView.as_view()
update_view = PageUpdateView.as_view()
