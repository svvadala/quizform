from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


RATING_CHOICES=[
('1','1'),
('2','2'),
('3','3'),
('4','4'),
('5','5'),
]

class QuizForm(forms.Form):
    question_one = forms.ChoiceField(label='How important is having SAFETY within a Residence Hall', choices=RATING_CHOICES, widget=forms.RadioSelect)
    question_two = forms.ChoiceField(label='How important is having a COMMUNITY within a Residence Hall', choices=RATING_CHOICES, widget=forms.RadioSelect)
    question_three = forms.ChoiceField(label='How important is NOISE LEVEL within a Residence Hall', choices=RATING_CHOICES, widget=forms.RadioSelect)
    question_four = forms.ChoiceField(label='How important is the STAFF within a Residence Hall', choices=RATING_CHOICES, widget=forms.RadioSelect)
    question_five = forms.ChoiceField(label='How important is having different AMMENITIES within a Residence Hall', choices=RATING_CHOICES, widget=forms.RadioSelect)
    question_six = forms.ChoiceField(label='How important is having different FACILITIES within a Residence Hall', choices=RATING_CHOICES, widget=forms.RadioSelect)


    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'question_one',
            'question_two',
            'question_three',
            'question_four',
            'question_five',
            'question_six',
            Submit('submit', 'Submit', css_class='btn-success')
        )
