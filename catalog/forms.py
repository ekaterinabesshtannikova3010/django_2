from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    forbidden_words = [
        'казино', 'криптовалюта', 'крипта',
        'биржа', 'дешево', 'бесплатно',
        'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(word in name.lower() for word in self.forbidden_words):
            raise forms.ValidationError("Название продукта содержит запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if any(word in description.lower() for word in self.forbidden_words):
            raise forms.ValidationError("Описание продукта содержит запрещенные слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',  # Используйте Ваши классы стилей
                'placeholder': f'Введите {field.label.lower()}'
            })
