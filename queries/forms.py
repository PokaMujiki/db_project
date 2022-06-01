from django import forms
from polls.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class Query1Form(forms.Form):
    required_product = forms.ModelChoiceField(queryset=Product.objects.all())
    volume = forms.IntegerField(validators=[validate_gt_0], required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))


class Query2Form(forms.Form):
    required_product = forms.ModelChoiceField(queryset=Product.objects.all())
    volume = forms.IntegerField(validators=[validate_gt_0], required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))


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


class Query9Form(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    distributor = forms.ModelChoiceField(queryset=Distributor.objects.all())
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


class Query10Form(forms.Form):
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all())
    filter = forms.ChoiceField(choices=[(None, '----'),
                                        ("Point size", "Point size"),
                                        ("Halls amount", "Halls amount"),
                                        ("Counters amount", "Counters amount")])


class Query12Form(forms.Form):
    product_order = forms.ModelChoiceField(queryset=ProductsOrder.objects.all())


class Query13Form(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all(), required=False)
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all(), required=False)


class Query14Form(forms.Form):
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all(), required=False)
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all(), required=False)


class Query15Form(forms.Form):
    trade_point_type = forms.ModelChoiceField(queryset=TradePointType.objects.all(), required=False)
    trade_point = forms.ModelChoiceField(queryset=TradePoint.objects.all(), required=False)



