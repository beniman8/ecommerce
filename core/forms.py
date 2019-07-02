from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S','Stripe'),
    ('P','Paypall')


)

class CheckoutForm(forms.Form):

    street_adress = forms.CharField(widget = forms.TextInput(
        attrs={
            'placeholder': '1234 Main Street',
            'class': 'form-control',
            'id': 'address'
        }
    ))

    apartment_adress = forms.CharField(required=False,widget = forms.TextInput(
        attrs={
            'placeholder': 'Apartment or Suite',
            'class': 'form-control',
            'id': 'address-2'
        }
    ))

    country =  CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(
        attrs ={
            'class':'custom-select d-block w-100'
        }
    ))

    zip = forms.CharField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
             'id': 'zip'
        }
    ))

    same_shipping_address = forms.BooleanField(required = False)
    save_info = forms.BooleanField(required = False)
    payment_option = forms.ChoiceField(widget = forms.RadioSelect(),choices = PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Promo code',
            'aria-label':'Recipient\'s username',
            'aria-describedby':'basic-addon2'
        }
    ))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget =forms.Textarea)
    email = forms.EmailField()