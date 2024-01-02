from django.db.models.base import Model
from django import forms
from .models import Business, Availability, Review


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'featured_image', 'address', 'availability']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['business', 'body', 'value']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['total_tables', 'booked_tables']

    def __init__(self, *args, **kwargs):
        super(AvailabilityForm, self).__init__(*args, **kwargs)
        self.fields['total_tables'].widget.attrs['readonly'] = True
        self.fields['booked_tables'].widget.attrs['readonly'] = True
