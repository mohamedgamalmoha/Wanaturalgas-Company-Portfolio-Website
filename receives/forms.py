from django import forms
from .models import MainRequests, Contact

from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, ButtonHolder, Submit, Row, Column, HTML


class MainRequestsForm(forms.ModelForm):

    class Meta:
        model = MainRequests
        fields = '__all__'


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Div(
                Div(
                    Row(
                        Column(
                            PrependedText('first_name', '<i class="fas fa-user"></i>', placeholder="First Name"),
                            css_class='form-group col-md-6'
                        ),
                        Column(
                            PrependedText('last_name', '<i class="fas fa-user"></i>', placeholder="Last Name"),
                            css_class='form-group col-md-6'
                        ),
                        css_class='form-row'
                    ),
                    Row(
                        Column(
                            PrependedText('emil_address', '<i class="far fa-envelope"></i>', placeholder="Email Address"),
                            css_class='form-group col-md-4 mb-0'
                        ),
                        Column(
                            PrependedText('phone_number', '<i class="fas fa-phone-volume"></i>', placeholder="Phone Number"),
                            css_class='form-group col-md-4 mb-0'
                        ),
                        Column(
                            PrependedText('zip_code', '<i class="fa fa-home"></i>', placeholder="Zip Code"),
                            css_class='form-group col-md-4 mb-0'
                        ),
                    ),
                    Div(
                        HTML(
                            '<h2> How can we help? </h2>  <p> Feel free to E-mail us for Fast & Responsive Service.</p>'
                        ),
                        'Question',
                        ButtonHolder(
                            Submit(
                                "submit-button", "Submit",
                                style='width: 400px;height: 40px;background-color: #34c6f2; color: #fff;'
                                      'border: 1px solid #34c6f2;'
                            ),
                        ),
                        style='display: block; margin-left:auto; margin-right: auto; width: 50%; text-align:center;',
                    ),
                    css_class="form-main"
                ),
                css_class="all-forms",
            ),
        )

    class Meta:
        model = Contact
        fields = '__all__'
