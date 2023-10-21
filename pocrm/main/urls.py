from django.urls import path
from .views import (KroyListView, KroyCreateView, KroyUpdateView, KroyDetailListView,
                    KroyDetailCreateView, KroyDetailUpdateView, KroyDetailView)

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),

    path('kroy/', KroyListView.as_view(), name='kroy-list'),
    path('kroy/create/', KroyCreateView.as_view(), name='kroy-create'),
    #path('kroy/<int:pk>/', KroyDetailView.as_view(), name='kroy-detail-view'),
    path('<int:kroy_id>/', views.KroyDetailView, name='kroy-detail-view'),
    path('kroy/update/<int:pk>/', KroyUpdateView.as_view(), name='kroy-update'),
    path('kroy-detail/', KroyDetailListView.as_view(), name='kroy-detail-list'),
    path('kroy-detail/create/', KroyDetailCreateView.as_view(), name='kroy-detail-create'),
    path('kroy-detail/update/<int:pk>/', KroyDetailUpdateView.as_view(), name='kroy-detail-update'),


]

