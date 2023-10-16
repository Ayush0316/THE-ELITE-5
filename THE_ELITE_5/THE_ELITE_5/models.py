from django.db import models

# class YourModelManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().raw("SELECT * FROM your_table")

class H1BDisclosure(models.Model):
    case_number = models.CharField(max_length=500, primary_key=True)
    case_status = models.CharField(max_length=255)
    case_submitted = models.DateField()
    decision_date = models.DateField()
    visa_class = models.CharField(max_length=255)
    employment_start_date = models.DateField()
    employment_end_date = models.DateField()
    employer_name = models.CharField(max_length=500)
    employer_business_dba = models.CharField(max_length=500)
    employer_address = models.CharField(max_length=500)
    employer_city = models.CharField(max_length=255)
    employer_state = models.CharField(max_length=255)
    employer_postal_code = models.CharField(max_length=255)
    employer_country = models.CharField(max_length=255)
    employer_province = models.CharField(max_length=255)
    employer_phone = models.CharField(max_length=255)
    employer_phone_ext = models.CharField(max_length=255)
    agent_representing_employer = models.CharField(max_length=255)
    agent_attorney_name = models.CharField(max_length=500)
    agent_attorney_city = models.CharField(max_length=255)
    agent_attorney_state = models.CharField(max_length=255)
    job_title = models.CharField(max_length=500)
    soc_code = models.CharField(max_length=255)
    soc_name = models.CharField(max_length=500)
    naics_code = models.CharField(max_length=255)
    total_workers = models.IntegerField()
    new_employment = models.IntegerField()
    continued_employment = models.IntegerField()
    change_previous_employment = models.IntegerField()
    new_concurrent_employment = models.IntegerField()
    change_employer = models.IntegerField()
    amended_petition = models.IntegerField()
    full_time_position = models.CharField(max_length=255)
    prevailing_wage = models.FloatField()
    pw_unit_of_pay = models.CharField(max_length=255)
    pw_wage_level = models.CharField(max_length=255)
    pw_source = models.CharField(max_length=255)
    pw_source_year = models.IntegerField()
    pw_source_other = models.CharField(max_length=500)
    wage_rate_of_pay_from = models.FloatField()
    wage_rate_of_pay_to = models.FloatField()
    wage_unit_of_pay = models.CharField(max_length=255)
    h1b_dependent = models.CharField(max_length=255)
    willful_violator = models.CharField(max_length=255)
    support_h1b = models.CharField(max_length=255)
    labor_con_agree = models.CharField(max_length=255)
    public_disclosure_location = models.CharField(max_length=255)
    worksite_city = models.CharField(max_length=255)
    worksite_county = models.CharField(max_length=255)
    worksite_state = models.CharField(max_length=255)
    worksite_postal_code = models.CharField(max_length=255)
    original_cert_date = models.DateField()

    class Meta:
        db_table = 'next_testing'
        managed = False

    def __str__(self):
        attributes = [f"{field.name}: {getattr(self, field.name)}" for field in self._meta.fields]
        return ", ".join(attributes)