from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("Name needs to start with z")

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email =forms.EmailField(label='Enter you email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
    # botcather = forms.CharField(required=False,
        if email !=vmail:
            raise forms.ValidationError("Email is not the same")
    #                            widget=forms.HiddenInput,
    #                            validators = [validators.MaxLengthValidator(0)])

    # def clean_botcather(self):
    #     botcatcher = self.cleaned_data['botcather']
    #     if len(botcather)>0:
    #         raise forms.ValidationError("GOTCHAG BO")
    #     return botcather
