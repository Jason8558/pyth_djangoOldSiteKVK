from django import forms
from model_utils import Choices

class AnketaForm (forms.Form):
    marital_status_choices = Choices('Холост/не замужем', 'Замужем/женат', 'Разведен/разведена', 'Состоит в зарег. браке', 'Состоит в гр. браке', 'Вдова/вдовец')
    vacancy = forms.CharField(max_length = 150)
    fio = forms.CharField(max_length = 300)
    date_of_birth = forms.DateField()
    age = forms.IntegerField()
    registr = forms.CharField(max_length = 300)
    fact_live = forms.CharField(max_length = 300)
    phone = forms.CharField(max_length = 300)

    # СЕМЕЙНОЕ ПОЛОЖЕНИЕ
    marital_status = forms.ChoiceField(choices=marital_status_choices)
    fio_spouse = forms.CharField(max_length = 150)
    date_of_birth_spouse = forms.DateField()
    
    kid_fio = forms.CharField(max_length = 300)
    kid_date_of_birth = forms.DateField()

    kid_fio1 = forms.CharField(max_length = 300)
    kid_date_of_birth1 = forms.DateField()

    # ОБРАЗОВАНИЕ
    educational_institution = forms.CharField(max_length = 300)
    facultity = forms.CharField(max_length = 300)
    educ_period_from = forms.DateField()
    educ_period_to = forms.DateField()
    educ_duration = forms.IntegerField()

    educational_institution1 = forms.CharField(max_length = 300)
    facultity1 = forms.CharField(max_length = 300)
    educ_period_from1 = forms.DateField()
    educ_period_to1 = forms.DateField()
    educ_duration1 = forms.IntegerField()

    educ_additional = forms.CharField(max_length = 300)
    educ_self = forms.CharField(max_length = 300)
    educ_want = forms.CharField(max_length = 300)

    # ПРОФЕССИОНАЛЬНЫЙ ОПЫТ
    organization = forms.CharField(max_length = 300)
    org_address =  forms.CharField(max_length = 300)
    org_phone = forms.CharField(max_length = 300)
    org_position = forms.CharField(max_length = 300)
    org_duty =  forms.CharField(max_length = 300)
    subord_count = forms.IntegerField()
    org_salary = forms.IntegerField()
    fired_reason = forms.CharField(max_length = 300)

    organization1 = forms.CharField(max_length = 300)
    org_address1 =  forms.CharField(max_length = 300)
    org_phone1 = forms.CharField(max_length = 300)
    org_position1 = forms.CharField(max_length = 300)
    org_duty1 =  forms.CharField(max_length = 300)
    subord_count1 = forms.IntegerField()
    org_salary1 = forms.IntegerField()
    fired_reason1 = forms.CharField(max_length = 300)

    rec_fio = forms.CharField(max_length = 300)
    workplace = forms.CharField(max_length = 300)
    rec_position = forms.CharField(max_length = 300)
    rec_phone = forms.CharField(max_length = 300)

    rec_fio1 = forms.CharField(max_length = 300)
    workplace1 = forms.CharField(max_length = 300)
    rec_position1 = forms.CharField(max_length = 300)
    rec_phone1 = forms.CharField(max_length = 300)

    # ЗАРПЛАТА
    zp_begin = forms.IntegerField()
    zp_year = forms.IntegerField()
    zp_perspective = forms.IntegerField()

    # УГОЛОВНАЯ ОТВЕТСТВЕННОСТЬ
    crime = forms.BooleanField()

    # КОМАНДИРОВКИ
    trip = forms.BooleanField()

    # ВРЕМЯ ПРИСТУПЛЕНИЯ К РАБОТЕ
    work_begin_time = forms.CharField(max_length = 300)

    # ИСТОЧНИК ПОЛУЧЕНИЯ ИНФОРМАЦИИ О ВАКАНСИИ
    info_source = forms.CharField(max_length = 300)

    # самопрезентация
    advantage = forms.CharField(max_length = 2000)
