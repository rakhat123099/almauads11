from django import forms
from .models import Ad
from django.forms.widgets import DateTimeInput

class AdForm(forms.ModelForm):
    CHOICES = (('Lost', 'Поиск утерянных вещей'),('Roommates', 'Поиск руммейта'),('Job', 'Поиск работы'),('Vacancies', 'Открытые вакансии'),('Events', 'Мероприятия'),('Services', 'Услуги'),('Garagesale', 'Garage sale'),('Other', 'Прочее'))
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Введите ваше имя",
                "class": "form-control",
            }
        ),
        label="",
    )
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Введите ваш номер",
                "class": "form-control",
            }
        ),
        label="",
    )
    postdate = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "Введите дату публикации",
                "type": "date",
                "class": "form-control"
            }
        ),
        label=""
    )
    posttime = forms.TimeField(
        required=True,
        widget=forms.widgets.TimeInput(
            attrs={
                "placeholder": "Введите время публикации",
                "type": "time",
                "class": "form-control"
            }
        ),
        label=""
    )
    category = forms.ChoiceField(
        choices=CHOICES,
        required=True,
        widget=forms.widgets.Select(
            attrs={
                "placeholder": "Выберите категорию",
                "class": "form-select"
            }
        ),
        label=""
    )
    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Введите текст вашего объявления",
                "class": "form-control",
            }
        ),
        label="",
    )


    class Meta:
        model = Ad
        exclude = ("created", )