from django import forms
from django.forms.formsets import formset_factory
from django.shortcuts import render
from djangoformsetjs.utils import formset_media_js
from example2.models import Parent, Tab, SubList
from .forms import TabForm, SubListForm
from nested_formset import nestedformset_factory, inlineformset_factory

# class TabForm(forms.ModelForm):
#
#     title = forms.CharField()
#
#     class Media(object):
#         # The form must have `formset_media_js` in its Media
#         js = formset_media_js + (
#             # Other form javascript...
#         )

#
# TabFormSet = formset_factory(TabForm, can_delete=True)
#

def formset_view(request):
    TabFormSet = nestedformset_factory(
        Parent,
        Tab,
        form=TabForm,
        extra=3,
        nested_formset=inlineformset_factory(
            Tab,
            SubList,
            form=SubListForm,
            extra=5
        )
    )

    tabs = TabFormSet()

    context = {
        "tabs": tabs,
    }

    if tabs.is_valid():
        pass

    return render(request, 'formset.html', context)
