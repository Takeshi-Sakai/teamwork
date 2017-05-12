from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hh_list(request):
    """ヒヤリハットの一覧"""
    return HttpResponse('ヒヤリハットの一覧')

def hh_edit(request, hh_id=None):
    """ヒヤリハットの編集"""
    return HttpResponse('ヒヤリハットの編集')

def hh_del(request, hh_id):
    """ヒヤリハットの削除"""
    return HttpResponse('ヒヤリハットの削除')