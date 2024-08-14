from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.applycall, name='apply_page'),
    path("apply_box/", views.box_apply_call, name='box_apply_main'),
    path("create_apply/", views.box_apply_create, name='box_apply_create'),
    path("apply_check/", views.box_checkcall, name='apply_check'),
    path("send_box/", views.sent_page, name="sent_page"),
    path("sending_box_create/", views.sent_apply_create, name='sent_apply_create'),
    path("save_failed_error", views.save_failed, name='failed'),
    path("researching_apply/", views.research_page_call, name='research_call'),
    path("researching_main/", views.research_apply, name='research'),
    path("picreq_call/", views.picreq_call, name='picreq_call'),
    path("picreq_sel/", views.picreq_call_select, name='pic_sel'),
    path("pickreq_faild/", views.pick_failed, name='pick_failed'),
    path("pick_success/", views.req_success_call, name='request_success'),
    path("progess_done/", views.pro_done_call, name='done'),
    path("progess_research/", views.pro_research_call, name='progress_research'),
    path("progess_req/", views.research_apply2, name='research2'),
    path("<int:apply_id>/progress_check/", views.pro_check_call ,name='progress_check'),
    path("progress_list/", views.pro_check_list, name='pro_check_list'),
    path("manager_page_main/", views.manager_page_main, name='ma_main'),
    path("manager_box_req/", views.manage_box_req, name='ma_boxreq'),
    path("manager_box_edit/", views.manage_box_req_edit, name='ma_boxreq_edit'),
    path("manager_pic_req/", views.manage_pic_req, name='ma_picreq'),
    path("manager_picreq_edit/", views.manage_pic_req_edit, name='ma_picreq_edit'),
    path('upload-xl/', views.upload_file_page, name='upload_file_page'),
    path('upload-x1_repl/', views.upload_xl, name='upload_xl'),
    path("manager_pic_ing/", views.manage_pic_ing, name='ma_picing'),
    path("manager_picing_edit/", views.manage_pic_ing_edit, name='ma_picing_edit'),
    path("manager_done/", views.manage_done, name='ma_done'),
    path("manager_infopage/", views.정보페이지_call, name = 'info_call'),
]