from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class WeatherFinderForm(forms.Form):
    location = forms.CharField(label='Location', max_length=20,
                               widget=forms.TextInput(attrs={'placeholder':
                                                             ('You can enter any type of content,'
                                                              'such as name of the city or zipcode.')}))

    def __init__(self, *args, **kwargs):
        super(WeatherFinderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Show Temperature'))
