
from django import forms


class contactForm(forms.Form):

    name=forms.CharField(label="User Name")
    email=forms.EmailField()
    age=forms.IntegerField()
    weight=forms.FloatField()
    balance=forms.DecimalField()
    check=forms.BooleanField()
    birthday=forms.DateField()
    appointment=forms.DateTimeField()
    CHOICES=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size=forms.ChoiceField(choices=CHOICES)
    pizzaTypes=[('P', 'Pepperoni'), ('C', 'Cheese'), ('V', 'Veggie'), ('M', 'Meat Lovers')]
    pizza=forms.MultipleChoiceField(choices=pizzaTypes)