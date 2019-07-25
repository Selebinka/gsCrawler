from django import forms
    
class RunCrawlForm(forms.Form):
    keywords = forms.CharField(max_length=50, required=True)
    value = forms.IntegerField(required=False)