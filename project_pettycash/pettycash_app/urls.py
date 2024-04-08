from django.urls import path
from . import views

app_name = 'pettycash_app'

urlpatterns = [
    #home
    path('', views.chooseCashBook, name='choose_cashbook'),

    #category
    path('category/', views.viewCategory, name='category'),
    path('create_category/', views.createCategory, name='create_category'),
    path('update_category/<uuid:id>/', views.updateCategory, name='update_category'),
    path('delete_category/<uuid:id>/', views.deleteCategory, name='delete_category'),
    
    #pettycash
    path('view_pettycash/', views.viewPettyCash, name='view_pettycash'),
    path('create_pettycash/', views.createPettyCash, name='create_pettycash'),
    path('update_pettycash/<uuid:id>/', views.updatePettyCash, name='update_pettycash'),
    path('each_pettycash/<uuid:id>/', views.eachPettyCash, name='each_pettycash'),
    path('delete_pettycash/<uuid:id>/', views.deletePettyCash, name='delete_pettycash'),
    path('petty_cash_signature/', views.pettyCashSignature, name='petty_cash_signature'),
    
    #federal pettycash
    path('view_federal_pettycash/', views.viewFederalPettyCash, name='view_federal_pettycash'),
    path('create_federal_pettycash/', views.createFederalPettyCash, name='create_federal_pettycash'),
    path('update_federal_pettycash/<uuid:id>/', views.updateFederalPettyCash, name='update_federal_pettycash'),
    path('each_federal_pettycash/<uuid:id>/', views.eachFederalPettyCash, name='each_federal_pettycash'),
    path('federal_bank_signature/', views.federalBankSignature, name='federal_bank_signature'),
    path('delete_federal_pettycash/<uuid:id>/', views.deleteFederalPettyCash, name='delete_federal_pettycash'),
    
    #sbi pettycash
    path('view_sbi_pettycash/', views.viewSBIPettyCash, name='view_sbi_pettycash'),
    path('create_sbi_pettycash/', views.createSBIPettyCash, name='create_sbi_pettycash'),
    path('update_sbi_pettycash/<uuid:id>/', views.updateSBIPettyCash, name='update_sbi_pettycash'),
    path('each_sbi_pettycash/<uuid:id>/', views.eachSBIPettyCash, name='each_sbi_pettycash'),
    path('sbi_bank_signature/', views.SbiBankSignature, name='sbi_bank_signature'),
    path('delete_sbi_pettycash/<uuid:id>/', views.deleteSBIPettyCash, name='delete_sbi_pettycash'),

    #fetching opening balance
    path('opening_balance/', views.fetchOpeningBalance, name='opening_balance'),
    path('federal_opening_balance/', views.fetchFederalOpeningBalance, name='federal_opening_balance'),
    path('sbi_opening_balance/', views.fetchSBIOpeningBalance, name='sbi_opening_balance'),
    
    #filtering
    path('filter_pettycash/', views.filter_pettycash, name='filter_pettycash'),
    path('filter_federal_pettycash/', views.filter_federal_pettycash, name='filter_federal_pettycash'),
    path('filter_sbi_pettycash/', views.filter_sbi_pettycash, name='filter_sbi_pettycash'),
    
    #opening Balance
    path('view_opening_balance/', views.viewOpeningBalance, name='view_opening_balance'),
    path('create_opening_balance/', views.createOpeningBalance, name='create_opening_balance'),
    path('update_opening_balance/<uuid:id>/', views.updateOpeningBalance, name='update_opening_balance'),
    path('delete_opening_balance/<uuid:id>/', views.deleteOpeningBalance, name='delete_opening_balance'),
    
    #excel file generating
    path('pettycash_balance_sheet_excel/', views.pettycash_balance_sheet_excel, name='pettycash_balance_sheet'),
    path('federal_balance_sheet_excel/', views.federal_balance_sheet_excel, name='federal_balance_sheet'),
    path('sbi_balance_sheet_excel/', views.sbi_balance_sheet_excel, name='sbi_balance_sheet'),
    
    #pdf file generating
    path('pettycash_all_pdf/', views.pettycash_all_pdf, name='pettycash_all_pdf'),
    path('pettycash_custom_pdf/', views.pettycash_custom_pdf, name='pettycash_custom_pdf'),
]