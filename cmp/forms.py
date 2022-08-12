from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=250)    
    class Meta:
        model = Proveedor
        exclude = ['usuarioModificador','fechaModificacion','usuarioCreador','fechaCreacion']
        widget = {'descripcion': forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})