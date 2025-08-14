
from django import forms
from django.core import validators

# widgets == fiels to html input

class contactForm(forms.Form):

    name=forms.CharField(label="full Name :", help_text="Total 50 character", required=False, widget=forms.Textarea(attrs={'id': 'text_area', 'rows': 3, 'cols': 20, 'class': 'class1 class2', 'placeholder': 'Enter your name'}))
    


    # file=forms.FileField()



    email=forms.EmailField(label="Email Address :", help_text="Enter your email address", required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))


    # age=forms.IntegerField()
    age=forms.CharField(widget=forms.NumberInput)


    # weight=forms.FloatField()
    # balance=forms.DecimalField()

    check=forms.BooleanField()

    birthday=forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))

    appointment=forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))

    CHOICES=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]

    size=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    pizzaTypes=[('P', 'Pepperoni'), ('C', 'Cheese'), ('V', 'Veggie'), ('M', 'Meat Lovers')]
    pizza=forms.MultipleChoiceField(choices=pizzaTypes, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname=self.cleaned_data['name']
#     #     if len(valname) <10 :
#     #         raise forms.ValidationError("Enter a name with at least 10 characters.")
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail=self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valemail

#     def clean(self):
#         cleaned_data=super().clean()
#         valname=self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
#         if len(valname) <10 :
#             raise forms.ValidationError("Enter a name with at least 10 characters.")

#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")


# def len_check(value):
#     if len(value)<10:
#         raise forms.ValidationError("At least 10 characters needed")



# class StudentData(forms.Form):
#     name=forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
#     text=forms.CharField(widget=forms.TextInput, validators=[len_check])
#     email=forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid mail")])
#     age=forms.IntegerField(validators=[validators.MaxValueValidator(34, message='max age 34'), validators.MinValueValidator(24, message='min age 24')])

#     file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='only pdf file allowed')])


class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data['password']
        val_con_pass=self.cleaned_data['confirm_password']
        val_name=self.cleaned_data['name']

        if val_pass != val_con_pass:
            raise forms.ValidationError("Password doesn't match")
        
        if len(val_name) <10 :
            raise forms.ValidationError("Name must be at least 10 characters.")

