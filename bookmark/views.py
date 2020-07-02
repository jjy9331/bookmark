from django.shortcuts import render

from django.views.generic import ListView
from .models import Bookmark

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3   # ListView 페이지에서 Paginate 기능 활성화


# 새로운 Bookmark 추가함수
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']   # Bookmark 테이블에서 연결할 Field 목록
    success_url = reverse_lazy('list') # 작업 완료 후 연결 link name
    template_name_suffix = '_create'  #  모델클래스_create.html 와 연결


# 북마크 확인기능
class BookmarkDetailView(DetailView):
    model = Bookmark


# 수정 기능
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']  # Bookmark 테이블에서 연결할 Field 목록
    template_name_suffix = "_update" # 모델클래스_update.html 와 연결


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

