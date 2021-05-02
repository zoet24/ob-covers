from django import forms
from .models import Product, Range, Style, Colour


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ranges = Range.objects.all()
        styles = Style.objects.all()
        colours = Colour.objects.all()

        self.fields['sku'].widget.attrs['autofocus'] = True

        friendly_names_ranges = [(r.id, r.get_friendly_name()) for r in ranges]
        friendly_names_styles = [(s.id, s.get_friendly_name()) for s in styles]
        friendly_names_colours = [(c.id, c.get_friendly_name()) for c in colours]

        self.fields['range'].choices = friendly_names_ranges
        self.fields['style'].choices = friendly_names_styles
        self.fields['colour'].choices = friendly_names_colours

        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'black-border rounded-0'
