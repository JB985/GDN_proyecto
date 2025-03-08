from django.contrib import admin
from django.urls import path, include
from crud_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('roles/', views.role_list, name='role_list'),
    path('roles/<int:pk>/', views.user_detail, name='role_detail'),
    path('roles/create/', views.role_create, name='role_create'),
    path('roles/<int:pk>/edit/', views.role_edit, name='role_edit'),
    path('roles/<int:pk>/delete/', views.role_delete, name='role_delete'),
    path('subcategories/', views.sub_cat_list, name='sub_cat_list'),
    path('subcategories/create/', views.sub_cat_create, name='sub_cat_create'),
    path('subcategories/<int:pk>/edit/', views.sub_cat_edit, name='sub_cat_edit'),
    path('subcategories/<int:pk>/delete/', views.sub_cat_delete, name='sub_cat_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('mobiliaries/', views.mobiliary_list, name='mobiliary_list'),
    path('mobiliaries/create/', views.mobiliary_create, name='mobiliary_create'),
    path('mobiliaries/<int:pk>/edit/', views.mobiliary_edit, name='mobiliary_edit'),
    path('mobiliaries/<int:pk>/delete/', views.mobiliary_delete, name='mobiliary_delete'),
    path('regions/', views.region_list, name='region_list'),
    path('regions/create/', views.region_create, name='region_create'),
    path('regions/<int:pk>/edit/', views.region_edit, name='region_edit'),
    path('regions/<int:pk>/delete/', views.region_delete, name='region_delete'),
    path('centers/', views.center_list, name='center_list'),
    path('centers/create/', views.center_create, name='center_create'),
    path('centers/<int:pk>/edit/', views.center_edit, name='center_edit'),
    path('centers/<int:pk>/delete/', views.center_delete, name='center_delete'),
    path('sedes/', views.list_sede, name='sedes_list'),
    path('sedes/create/', views.create_sede, name='sedes_create'),
    path('sedes/<int:pk>/edit/', views.edit_sede, name='sedes_edit'),
    path('sedes/<int:pk>/delete/', views.delete_sede, name='sedes_delete'),
    path('programs/', views.list_programs, name='list_programs'),
    path('programs/create/', views.create_program, name='create_program'),
    path('programs/<int:pk>/edit/', views.edit_program, name='edit_program'),
    path('programs/<int:pk>/delete/', views.delete_program, name='delete_program'),
    path('fichas/', views.list_fichas, name='list_fichas'),
    path('fichas/create/', views.create_ficha, name='create_ficha'),
    path('fichas/<int:pk>/edit/', views.edit_ficha, name='edit_ficha'),
    path('fichas/<int:pk>/delete/', views.delete_ficha, name='delete_ficha'),
    path('mobprotect/', views.mobiliary_protected_list, name='mob_protect_list'),
    path('fichasprotect/', views.fichas_protected_list, name='fichas_protected_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('ambientes/', views.ambientes_list, name='ambientes_list'),
    path('ambientes/create/', views.ambiente_create, name='ambientes_create'),
    path('ambientes/<int:pk>/edit/', views.ambiente_edit, name='ambientes_edit'),
    path('ambientes/<int:pk>/delete/', views.ambiente_delete, name='ambientes_delete'),
]