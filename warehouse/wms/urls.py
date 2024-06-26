from django.urls import path
from . import views

urlpatterns = [
    path('add-supervisor',views.add_supervisor),
    path('warehouse-login',views.warehouse_login),
    path('warehouse-login-action',views.warehouse_login_action),
    path('header',views.header),
    path('edit-user',views.edit_user),
    path('add-building',views.add_building),
    path('home',views.home),
    path('add-building-action',views.addbuilding_action),
    path('view-building',views.view_building),
    path('edit-building',views.edit_building),
    path('edit-building-action',views.edit_building_action),
    path('edit-building-action-save',views.edit_building_action_save),
    path('view-all-buildings',views.view_all_buildings),
    path('add-rack', views.add_rack),
    path('add-rack-action',views.add_rack_action),
    path('warehouse-logout-action',views.warehouse_logout_action),
    path('view-rack',views.view_rack),
    path('view-rack-action',views.view_rack_action),
    path('edit-rack',views.edit_rack),
    path('edit-rack-action',views.edit_rack_action),
    path('edit-rack-action-save',views.edit_rack_action_save),
    path('delete',views.delete),
    path('view-supervisor',views.view_supervisor),
    path('view-supervisor-action',views.view_supervisor_action),
    path('add-supervisor',views.add_supervisor),
    path('add-supervisor-action',views.add_supervisor_action),
    path('supervisor-header',views.supervisor_header),
    path('supervisor-warehouse-login',views.supervisor_warehouse_login),
    path('supervisor-warehouse-login-action',views.supervisor_warehouse_login_action),
    path('supervisor-warehouse-logout-action',views.supervisor_warehouse_logout_action),
    path('supervisor-home',views.supervisor_home),
    path('add-row',views.add_row),
    path('add-row-action',views.add_row_action),
    path('view-rows-action',views.view_rows_action),
    path('supervisor-add-product',views.supervisor_add_product),
    path('supervisor-add-product-action',views.supervisor_add_product_action),
    path('supervisor-view-product', views.supervisor_view_product),
    path('supervisor-view-product-action',views.supervisor_view_procducts_action),
    path('supervisor-delete-product',views.supervisor_delete_product),
    path('supervisor-edit-product',views.supervisor_edit_product),
    path('supervisor-edit-product-action',views.supervisor_edit_product_action),
    path('supervisor-edit-product-action-save',views.supervisor_edit_product_action_save),
    path('view-bin',views.view_bin),
    path('view-bin-action',views.view_bin_action),
    path('edit-bin',views.edit_bin),
    path('edit-bin-action',views.edit_bin_action),
    path('edit-bin-action-save',views.edit_bin_action_save),
    path('supervisor-add-box',views.supervisor_add_box),
    path('supervisor-add-box-action',views.supervisor_add_box_action),
    path('add-employee', views.add_employee),
    path('add-employee-action',views.add_employee_action),
    path('view-employee', views.view_employee),
    path('view-employee-action',views.view_employee_action),
    path('edit-employee', views.edit_employee),
    path('edit-employee-action',views.edit_employee_action),
    path('edit-employee-action-save',views.edit_employee_action_save),
    path('supervisor-view-box', views.supervisor_view_box),
    path('supervisor-add-employee-attendence', views.supervisor_add_employee_attendence),
    path('supervisor-view-employee', views.supervisor_view_employee),
    path('supervisor-box-transit',views.supervisor_box_transit),
    path('supervisor-view-employee-attendence', views.supervisor_view_employee_attendence),
    path('supervisor-view-rack-report', views.supervisor_view_rack_report),
    path('supervisor-free-space', views.supervisor_free_space),
    path('job-sheduling',views.job_sheduling),
    path('view-product',views.view_product),
    path('manager-view-product',views.manager_view_product),
    path('supervisor-view-employee-action', views.supervisor_view_employee_action),
    path('detect-intent-texts', views.detect_intent_texts),
    path('chatbotdemo',views.chatbotdemo),
    path('chat-free-space', views.chat_free_space),
    path('chat-employee-present', views.chat_employee_present),
    path('chat-employee-absent', views.chat_employee_absent),
    path('chat-employee-details', views.chat_employee_details),
    path('chat-supervisor-details', views.chat_supervisor_details),

]
