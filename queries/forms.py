from django import forms
from polls.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


# 1 Получить перечень и общее число поставщиков, поставляющих указанный вид товара,
#   либо некоторый товар в объеме, не менее заданного за весь период сотрудничества,
#       либо за указанный период.
class Query1Form(forms.Form):
    required_product = forms.ModelChoiceField(queryset=Product.objects.all())
    volume = forms.IntegerField(validators=[validate_gt_0], required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))


# 2 Получить перечень и общее число покупателей, купивших указанный вид товара за
#   некоторый период, либо сделавших покупку товара в объеме, не менее заданного.
#   (в объеме не менее заданного (за 1 чек))
class Query2Form(forms.Form):
    required_product = forms.ModelChoiceField(queryset=Product.objects.all())
    volume = forms.IntegerField(validators=[validate_gt_0], required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))


# 3 Получить номенклатуру и объем товаров в указанной торговой точке.
#   (объем товаров присутсвующих сейчас)
class Query3Form(forms.Form):
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all())


class Query4Form(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all(), required=False)
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all(), required=False)


class Query5Form(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all(), required=False)


class Query6Form(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all())
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class Query7Form(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all(), required=False)
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all(), required=False)


class Query8Form(forms.Form):
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all(), required=False)
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all(), required=False)


