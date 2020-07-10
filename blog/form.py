from django import forms
from blog.models import BlogPost


# by using forms.Form you dont need model
# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'slug', 'publish_date']

    # this is form validation for fields
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        # my way
        # if instance is None:
        #     qs = BlogPost.objects.filter(title__iexact=title)
        #     if qs.exists():
        #         raise forms.ValidationError("Already Exists")
        #     print(title)
        #     return title
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Aleady exists")
        return title

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('Content is too short write more lines')
        return content
    # slug is already getting verified in  model
    # def clean_slug(self,*args,**kwargs):
    #     slug = self.cleaned_data.get('slug')
    #     qs = BlogPost.objects.filter(slug= slug)
    #     if qs.exists():
    #         raise forms.ValidationError("slug Exists")
    #     return slug
