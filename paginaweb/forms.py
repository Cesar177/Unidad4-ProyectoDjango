from django import forms

class ProyectoForm(forms.Form):

    foto = forms.URLField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))
    descripcion = forms.CharField(max_length=800, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))
    tags = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))
    url = forms.URLField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))