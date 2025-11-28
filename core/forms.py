from django import forms
from core.models import Airport, AirportRoute

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'name']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Airport Code (e.g., COK)'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Airport Name'}),
        }

class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ['from_airport', 'to_airport', 'position', 'duration']
        widgets = {
            'from_airport': forms.Select(attrs={'class': 'form-select'}),
            'to_airport': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in minutes'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        from_airport = cleaned_data.get('from_airport')
        to_airport = cleaned_data.get('to_airport')
        if from_airport == to_airport:
            raise forms.ValidationError("From and To airports cannot be the same.")
        return cleaned_data

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration:
            if duration < 1:
                raise forms.ValidationError("Duration must be at least 1 minute.")
            if duration > 1440: 
                raise forms.ValidationError("Duration cannot exceed 24 hours (1440 minutes).")
        return duration


class NodeSearchForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all().order_by('code'),
        label="Start Airport",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Choose start airport'
        })
    )
    position = forms.ChoiceField(
        choices=[('Left', 'Left'), ('Right', 'Right')],
        label="Direction",
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    n_value = forms.IntegerField(
        min_value=1, 
        label="N Value",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter position number',
            'min': '1'
        })
    )



class LongestNodeForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        required=True,
        label="Select Starting Airport",
        widget=forms.Select(attrs={
            'class': 'form-select'
        })

    )

class ShortestNodeForm(forms.Form):
    from_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all().order_by('code'),
        label="From Airport",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select departure airport'
        })
    )
    to_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all().order_by('code'),
        label="To Airport",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select arrival airport'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        from_airport = cleaned_data.get('from_airport')
        to_airport = cleaned_data.get('to_airport')
        
        if from_airport and to_airport and from_airport == to_airport:
            raise forms.ValidationError("Departure and arrival airports cannot be the same.")
        
        return cleaned_data
