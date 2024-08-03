from django import forms

class PostForm(forms.Form):
    image= forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()

def clean(self):
    titl = self.cleaned_data.get("title")
    content = self.cleaned_data.get("content")
    if title.lower()==content.lower():
        return cleaned_data

def clean_title(self ):
    title = self.cleaned_data['title']
    if 'python' in title.lower():
        raise forms.ValidationError('Слово "python " не допустимо в заголовок ')
    return title
