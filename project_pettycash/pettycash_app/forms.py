from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
        widgets = {
            'category': forms.TextInput(attrs={
                'id': 'formCategoryName',
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',
                'placeholder': 'Category Name',
            }),
            'general_ledger_code': forms.NumberInput(attrs={
                'id': 'formCategoryCode',
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',
                'placeholder': 'GL Code',
            }),
        }

class PettyCashForm(forms.ModelForm):
    class Meta:
        model = PettyCash
        fields = '__all__'
        
        widgets = {
            'created_date': forms.DateInput(attrs={
                'id': 'formPettyCashDate',    
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',   
                'placeholder': 'Select Date',  
                'type': 'date',
            }),
            'category': forms.Select(attrs={
                'id': 'formPettyCashCategory',    
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',    
            }),
            'cash_flow': forms.Select(attrs={
                'id': 'formPettyCashFlow',    
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',    
            }),
            'amount': forms.NumberInput(attrs={
                'id': 'formPettyCashAmount',
                'class': 'bg-white text-gray-900 pl-8 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',
                'placeholder': 'Amount',
            }),
            'to_or_from': forms.TextInput(attrs={
                'id': 'formPettyCashToOrFrom',
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500 uppercase',
                'placeholder': 'To/From',
            }),
            'description': forms.Textarea(attrs={
                'id': 'formPettyCashDescription',
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',
                'rows': '4',
                'placeholder': 'Description...',
            }),
            'image': forms.FileInput(attrs={
                'id': 'formPettyCashSignature',
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',
            }),
        }
        
class FederalBankPettyCashForm(forms.ModelForm):
    class Meta:
        model = FederalBank
        fields = '__all__'
        
        widgets = {
            'created_date': forms.DateInput(attrs={
                'id': 'formFederalPettyCashDate',    
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',   
                'placeholder': 'Select Date',  
                'type': 'date',
            }),
            'category': forms.Select(attrs={
                'id': 'formFederalPettyCashCategory',    
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',    
            }),
            'cash_flow': forms.Select(attrs={
                'id': 'formFederalPettyCashFlow',    
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',    
            }),
            'amount': forms.NumberInput(attrs={
                'id': 'formFederalPettyCashAmount',
                'class': 'bg-white text-gray-900 pl-8 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',
                'placeholder': 'Amount',
            }),
            'to_or_from': forms.TextInput(attrs={
                'id': 'formFederalPettyCashToOrFrom',
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500 uppercase',
                'placeholder': 'To/From',
            }),
            'description': forms.Textarea(attrs={
                'id': 'formFederalPettyCashDescription',
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',
                'rows': '4',
                'placeholder': 'Description...',
            }),
        }

class SBIBankPettyCashForm(forms.ModelForm):
    class Meta:
        model = SBIBank
        fields = '__all__'
        
        widgets = {
            'created_date': forms.DateInput(attrs={
                'id': 'formSBIPettyCashDate',    
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',   
                'placeholder': 'Select Date',  
                'type': 'date',
            }),
            'category': forms.Select(attrs={
                'id': 'formSBIPettyCashCategory',    
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',    
            }),
            'cash_flow': forms.Select(attrs={
                'id': 'formSBIPettyCashFlow',    
                'class': 'bg-white text-gray-900 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',    
            }),
            'amount': forms.NumberInput(attrs={
                'id': 'formSBIPettyCashAmount',
                'class': 'bg-white text-gray-900 pl-8 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',
                'placeholder': 'Amount',
            }),
            'to_or_from': forms.TextInput(attrs={
                'id': 'formSBIPettyCashToOrFrom',
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500 uppercase',
                'placeholder': 'To/From',
            }),
            'description': forms.Textarea(attrs={
                'id': 'formSBIPettyCashDescription',
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',
                'rows': '4',
                'placeholder': 'Description...',
            }),
        }

class OpeningBalanceForm(forms.ModelForm):
    class Meta:
        model = OpeningBalance
        fields = '__all__'
        
        widgets = {
            'opening_date': forms.DateInput(attrs={
                'id': 'formOPDate',    
                'class': 'block bg-white p-2.5 w-full text-sm rounded-lg border-none focus:ring-blue-500',   
                'placeholder': 'Select Opening Date',  
                'type': 'date',
            }),
            'opening_balance': forms.NumberInput(attrs={
                'id': 'formOPBalance', 
                'class': 'bg-white text-gray-900 pl-8 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',
                'placeholder': 'Opening Balance', 
            }),
            'opening_balance_of': forms.Select(attrs={
                'id': 'formOPCurrent',
                'class': 'bg-white text-gray-900 pl-8 text-sm rounded-lg border-none focus:ring-blue-500 block w-full p-2.5',
            }),
        }