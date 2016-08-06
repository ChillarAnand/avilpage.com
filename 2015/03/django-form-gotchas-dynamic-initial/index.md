<!--
.. title: Django Gotchas #1 - Dynamic Initial Values In Forms!
.. slug: django-form-gotchas-dynamic-initial
.. date: 2015-03-19 18:52:00
.. tags: tech, django, python
.. description:
.. link:
.. type: text
-->



Django form fields accept initial argument. So You can set a default value for
a field.

```py
In [1]: from django import forms

In [2]: class SampleForm(forms.Form):
   ...:     name = forms.CharField(max_length=10, initial='avil page')
   ...:

In [3]: f = SampleForm()

In [4]: f.as_p()
Out[4]: u'<p>Name: <input maxlength="10" name="name" type="text" value="avil page" /></p>'
```

<br>


Sometimes it is required to override __init__ method in forms and set field
initial arguments.

```
In [11]: from django import forms

In [12]: class AdvancedForm(forms.Form):
   ....:
   ....:    def __init__(self, *args, **kwargs):
   ....:        super().__init__(*args, **kwargs)
   ....:        self.fields['name'].initial =  'override'
   ....:
   ....:        name=forms.CharField(max_length=10)
   ....:

In [13]: f2 = AdvancedForm()

In [14]: f2.as_p()
Out[14]: '<p>Name: <input maxlength="10" name="name" type="text" value="override" /></p>'
```

<br>


Now let's pass some initial data to form and see what happens.

```py
In [11]: from django import forms

In [12]: class AdvancedForm(forms.Form):
   ....:
   ....:    def __init__(self, *args, **kwargs):
   ....:        super().__init__(*args, **kwargs)
   ....:        self.fields['name'].initial = 'override'  # don't try this at home
   ....:
   ....:        name=forms.CharField(max_length=10)
   ....:

In [19]: f3 = AdvancedForm(initial={'name': 'precedence'})

In [20]: f3.as_p()
Out[20]: '<p>Name: <input maxlength="10" name="name" type="text" value="precedence" /></p>'
```


If You look at the value of input field, it's is NOT the overrided. It
still has form initial value!

If You look into [source code of django forms](https://github.com/django/django/blob/master/django/forms/forms.py#L631-L633) to find what is happening, You will find this.

```py
data = self.field.bound_data(
       self.data,
       self.form.initial.get(self.name, self.field.initial)  # precedence matters!!!!
)
```

So form's initial value has precedence over fields initial values.

So You have to override form's initial value instead of fields's initial value
to make it work as expected.

```py
In [21]: from django import forms

In [22]: class AdvancedForm(forms.Form):
   ....:
   ....:    def __init__(self, *args, **kwargs):
   ....:        super().__init__(*args, **kwargs)
   ....:        self.initial['name'] = 'override'  # aha!!!!
   ....:
   ....:        name=forms.CharField(max_length=10)
   ....:

In [23]: f4 = AdvancedForm(initial={'name': 'precedence'})

In [24]: f4.as_p()
Out[24]: '<p>Name: <input maxlength="10" name="name" type="text" value="override" /></p>'
```


Read official docs about [django forms](https://docs.djangoproject.com/en/1.7/ref/forms/api/).

Read more [articles about Python](/search/label/python)!
