"""
Form classes
"""
from django import forms
from django.core.urlresolvers import reverse_lazy

from agnocomplete import fields, widgets
from agnocomplete.forms import UserContextForm

from .autocomplete import (
    AutocompleteColor,
    AutocompleteColorShort,
    AutocompletePerson,
    AutocompletePersonShort,
    HiddenAutocomplete,
    AutocompleteTag,
)
from .models import PersonTag


class SearchForm(forms.Form):
    search_color = fields.AgnocompleteField(AutocompleteColor)
    search_person = fields.AgnocompleteModelField(AutocompletePerson)


class SearchFormTextInput(forms.Form):
    """
    For some reasons, JQuery Autocomplete needs a TextInput instead of a basic
    select.
    """
    search_color = fields.AgnocompleteField(
        AutocompleteColor, widget=widgets.AgnocompleteTextInput)
    search_person = fields.AgnocompleteModelField(
        AutocompletePerson, widget=widgets.AgnocompleteTextInput)


class SearchContextForm(UserContextForm):
    search_person = fields.AgnocompleteModelField('AutocompletePersonDomain')


class SearchCustom(forms.Form):
    search_color = fields.AgnocompleteField(
        HiddenAutocomplete(url=reverse_lazy('hidden-autocomplete')),
    )


class SearchColorMulti(forms.Form):
    search_multi_color = fields.AgnocompleteMultipleField(
        AutocompleteColorShort)
    search_multi_color_create = fields.AgnocompleteMultipleField(
        AutocompleteColorShort,
        create=True,
    )


class PersonTagForm(forms.Form):
    person = fields.AgnocompleteModelField(AutocompletePersonShort)
    tags = fields.AgnocompleteModelMultipleField(AutocompleteTag)


class PersonTagModelForm(forms.ModelForm):
    person = fields.AgnocompleteModelField(AutocompletePersonShort)
    tags = fields.AgnocompleteModelMultipleField(AutocompleteTag)

    class Meta:
        model = PersonTag
        fields = '__all__'
