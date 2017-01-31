from django  import forms

#from crispy_forms.bootstrap import InlineField
from .models import DataRegistration

class SignUpData(forms.ModelForm):
    class Meta:
        model=DataRegistration
        fields=('first_name','last_name','birth_date','gender','batch_number','email','address','blood_gruoup','college','alma_mater','status')
   
    def clean_first_name(self):
        first_name=self.cleaned_data.get('first_name') 
        return first_name
    def clean_last_name(self):
        last_name=self.cleaned_data.get('last_name') 
        return last_name
    def clean_birth_date(self):
        birth_date=self.cleaned_data.get('birth_date') 
        return birth_date
    def clean_gender(self):
        gender=self.cleaned_data.get('gender') 
        return gender
    def clean_batch_number(self):
        batch_number=self.cleaned_data.get('batch_number') 
        return batch_number
    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_base,provider=email.split("@")
        domain,extension=provider.split('.')
        if not domain=="iiuc":
            raise form.ValidationError("Please use IIUC doamin")
        if not extension=="edu":
            raise form.ValidationError("Please Use a Valid .EDU email address")
        return email
    def clean_address(self):
        address=self.cleaned_data.get('address') 
        return address
    def clean_blood_gruoup(self):
        blood_gruoup=self.cleaned_data.get('blood_gruoup') 
        return blood_gruoup
    def clean_blood_college(self):
        college=self.cleaned_data.get('college') 
        return college
    def clean_alma_mater(self):
        alma_mater=self.cleaned_data.get('alma_mater') 
        return alma_mater
    def clean_status(self):
        status=self.cleaned_data.get('status') 
        return status
    

     