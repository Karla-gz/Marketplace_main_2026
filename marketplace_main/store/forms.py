from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Product
# =========================
# 👤 Registro de usuario
# =========================
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# =========================
# 📦 Producto
# =========================
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'