from django import forms

# create form as below 
#  import it to the article view
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    
    # clean only single input
    def clean_title(self):
        cleaned_data = self.cleaned_data # dictionary
        title = cleaned_data.get('title')
        return title
 
 
    # clean all inputs
    def clean(self):
        cleaned_data = self.cleaned_data #
        title = cleaned_data.get('title')
       
        # add an eror 
        if title == 'hello':
            self.add_error('title', 'this article is taken')
        
        return cleaned_data