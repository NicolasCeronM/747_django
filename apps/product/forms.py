from django import forms
from .models import Product, ProductImage, ProductSize

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'drop', 'discount', 'stock', 'is_available']

# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['image']
#         widgets = {
#             'image': forms.ClearableFileInput(attrs={'multiple': True})
#         }

class ProductSizeForm(forms.Form):
    size = forms.CharField(max_length=10)
