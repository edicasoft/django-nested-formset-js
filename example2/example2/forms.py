from django import forms
from .models import Tab, SubList
from djangoformsetjs.utils import formset_media_js


class TabForm(forms.ModelForm):
    # food = forms.ChoiceField(widget=forms.RadioSelect(), choices=GameProperties.FOOD_OPTS, empty_label=None)

    class Meta:
        model = Tab
        exclude = ('parent',)
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", "placeholder": "Once upon a time...",
                                            "required": "true"}),
        }

    class Media(object):
        js = formset_media_js + (
            # Other form javascript...
        )


class SubListForm(forms.ModelForm):
    class Meta:
        model = SubList
        # fields = '__all__'
        exclude = ('tab',)
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", "placeholder": "some title"}),
        }
