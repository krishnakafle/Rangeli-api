from django.contrib.gis.db import models
from custom_rest_framework_mvt.managers import MVTManager

class HouseholdQuestionaireMatch(models.Model):
    small = models.CharField(max_length=150, primary_key=True)
    original = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_questionaire_match'

class AttributeLookup(models.Model):
    linked_table = models.CharField(max_length=150, blank=True, null=True)
    list_name = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    label = models.CharField(max_length=150, blank=True, null=True)
    key_att = models.CharField(max_length=150, blank=True, null=True)
    sn = models.CharField(max_length=150, primary_key=True)

    class Meta:
        managed = False
        db_table = 'attribute_lookup'

class HouseholdQuestions(models.Model):
    linked_table = models.CharField(max_length=30, blank=True, null=True)
    column_category = models.CharField(max_length=50, blank=True, null=True)
    meta_column = models.CharField(max_length=100, blank=True, null=True)
    odk_data_type = models.CharField(max_length=50, blank=True, null=True)
    choice_list = models.CharField(max_length=100, blank=True, null=True)
    odk_question = models.CharField(max_length=150, blank=True, null=True)
    display_name = models.CharField(max_length=300, blank=True, null=True)
    datatype = models.CharField(max_length=50, blank=True, null=True)
    required = models.CharField(max_length=30, blank=True, null=True)
    sn = models.IntegerField(primary_key=True, default=1)

    class Meta:
        managed = False
        db_table = 'household_questions'


class HouseholdData(models.Model):
    submissiondate = models.CharField(max_length=200, blank=True, null=True)
    start = models.CharField(max_length=200, blank=True, null=True)
    end = models.CharField(max_length=200, blank=True, null=True)
    phonenumber = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    ward = models.CharField(max_length=200, blank=True, null=True)
    tol = models.CharField(max_length=200, blank=True, null=True)
    housecode = models.CharField(max_length=200, blank=True, null=True)
    roadname = models.CharField(max_length=200, blank=True, null=True)
    housephoto = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    altitude = models.CharField(max_length=200, blank=True, null=True)
    accuracy = models.CharField(max_length=200, blank=True, null=True)
    funcational_type = models.CharField(max_length=200, blank=True, null=True)
    q3_1 = models.CharField(max_length=200, blank=True, null=True)
    q3_2 = models.CharField(max_length=200, blank=True, null=True)
    q3_3 = models.CharField(max_length=200, blank=True, null=True)
    q3_4 = models.CharField(max_length=200, blank=True, null=True)
    q3_5 = models.CharField(max_length=200, blank=True, null=True)
    q3_6 = models.CharField(max_length=200, blank=True, null=True)
    q3_61 = models.CharField(max_length=200, blank=True, null=True)
    q5 = models.CharField(max_length=200, blank=True, null=True)
    q6 = models.CharField(max_length=200, blank=True, null=True)
    q7 = models.CharField(max_length=200, blank=True, null=True)
    q7_1 = models.CharField(max_length=200, blank=True, null=True)
    q8 = models.CharField(max_length=200, blank=True, null=True)
    q11 = models.CharField(max_length=200, blank=True, null=True)
    q9 = models.CharField(max_length=200, blank=True, null=True)
    q10 = models.CharField(max_length=200, blank=True, null=True)
    total_pop = models.CharField(max_length=200, blank=True, null=True)
    q37 = models.CharField(max_length=200, blank=True, null=True)
    q37_1 = models.CharField(max_length=200, blank=True, null=True)
    q35 = models.CharField(max_length=200, blank=True, null=True)
    q35_1 = models.CharField(max_length=200, blank=True, null=True)
    q34 = models.CharField(max_length=200, blank=True, null=True)
    q34_1 = models.CharField(max_length=200, blank=True, null=True)
    q36 = models.CharField(max_length=200, blank=True, null=True)
    q39 = models.CharField(max_length=200, blank=True, null=True)
    q40 = models.CharField(max_length=200, blank=True, null=True)
    q41 = models.CharField(max_length=200, blank=True, null=True)
    q41_2 = models.CharField(max_length=200, blank=True, null=True)
    q41_3 = models.CharField(max_length=200, blank=True, null=True)
    q41_1 = models.CharField(max_length=200, blank=True, null=True)
    q42_1_1 = models.CharField(max_length=200, blank=True, null=True)
    q42_1_2 = models.CharField(max_length=200, blank=True, null=True)
    q42_1_3 = models.CharField(max_length=200, blank=True, null=True)
    q42_3_1 = models.CharField(max_length=200, blank=True, null=True)
    q42_3_2 = models.CharField(max_length=200, blank=True, null=True)
    q42_3_3 = models.CharField(max_length=200, blank=True, null=True)
    q43 = models.CharField(max_length=200, blank=True, null=True)
    q44_1_1 = models.CharField(max_length=200, blank=True, null=True)
    q44_1_2 = models.CharField(max_length=200, blank=True, null=True)
    q44_1_3 = models.CharField(max_length=200, blank=True, null=True)
    q44_3_1 = models.CharField(max_length=200, blank=True, null=True)
    q44_3_2 = models.CharField(max_length=200, blank=True, null=True)
    q44_3_3 = models.CharField(max_length=200, blank=True, null=True)
    q45 = models.CharField(max_length=200, blank=True, null=True)
    q48_a = models.CharField(max_length=200, blank=True, null=True)
    q48_c = models.CharField(max_length=200, blank=True, null=True)
    q48_b = models.CharField(max_length=200, blank=True, null=True)
    q48_d = models.CharField(max_length=200, blank=True, null=True)
    q48_a1 = models.CharField(max_length=200, blank=True, null=True)
    q48_a2 = models.CharField(max_length=200, blank=True, null=True)
    q48_a3 = models.CharField(max_length=200, blank=True, null=True)
    q49 = models.CharField(max_length=200, blank=True, null=True)
    q50 = models.CharField(max_length=200, blank=True, null=True)
    q51_1 = models.CharField(max_length=200, blank=True, null=True)
    q51_2 = models.CharField(max_length=200, blank=True, null=True)
    q51_3 = models.CharField(max_length=200, blank=True, null=True)
    q53 = models.CharField(max_length=200, blank=True, null=True)
    q54 = models.CharField(max_length=200, blank=True, null=True)
    q55 = models.CharField(max_length=200, blank=True, null=True)
    q56 = models.CharField(max_length=200, blank=True, null=True)
    q57 = models.CharField(max_length=200, blank=True, null=True)
    q58 = models.CharField(max_length=200, blank=True, null=True)
    q59 = models.CharField(max_length=200, blank=True, null=True)
    q60 = models.CharField(max_length=200, blank=True, null=True)
    q60_1 = models.CharField(max_length=200, blank=True, null=True)
    q61 = models.CharField(max_length=200, blank=True, null=True)
    q62 = models.CharField(max_length=200, blank=True, null=True)
    q63 = models.CharField(max_length=200, blank=True, null=True)
    q65 = models.CharField(max_length=200, blank=True, null=True)
    q66 = models.CharField(max_length=200, blank=True, null=True)
    q66_1a = models.CharField(max_length=200, blank=True, null=True)
    q66_1b = models.CharField(max_length=200, blank=True, null=True)
    q66_1c = models.CharField(max_length=200, blank=True, null=True)
    q66_2a = models.CharField(max_length=200, blank=True, null=True)
    q66_2b = models.CharField(max_length=200, blank=True, null=True)
    q66_2c = models.CharField(max_length=200, blank=True, null=True)
    q66_3a = models.CharField(max_length=200, blank=True, null=True)
    q66_3b = models.CharField(max_length=200, blank=True, null=True)
    q66_3c = models.CharField(max_length=200, blank=True, null=True)
    q61_4a = models.CharField(max_length=200, blank=True, null=True)
    q61_4b = models.CharField(max_length=200, blank=True, null=True)
    q61_4c = models.CharField(max_length=200, blank=True, null=True)
    q66_5a = models.CharField(max_length=200, blank=True, null=True)
    q66_5b = models.CharField(max_length=200, blank=True, null=True)
    q66_5c = models.CharField(max_length=200, blank=True, null=True)
    q66_6a = models.CharField(max_length=200, blank=True, null=True)
    q66_6b = models.CharField(max_length=200, blank=True, null=True)
    q66_6c = models.CharField(max_length=200, blank=True, null=True)
    q66_7a = models.CharField(max_length=200, blank=True, null=True)
    q66_7b = models.CharField(max_length=200, blank=True, null=True)
    q66_7c = models.CharField(max_length=200, blank=True, null=True)
    q66_8a = models.CharField(max_length=200, blank=True, null=True)
    q66_8b = models.CharField(max_length=200, blank=True, null=True)
    q66_8c = models.CharField(max_length=200, blank=True, null=True)
    q66_9a = models.CharField(max_length=200, blank=True, null=True)
    q66_9b = models.CharField(max_length=200, blank=True, null=True)
    q66_9c = models.CharField(max_length=200, blank=True, null=True)
    q66_10a = models.CharField(max_length=200, blank=True, null=True)
    q66_10b = models.CharField(max_length=200, blank=True, null=True)
    q66_10c = models.CharField(max_length=200, blank=True, null=True)
    q66_11a = models.CharField(max_length=200, blank=True, null=True)
    q66_11b = models.CharField(max_length=200, blank=True, null=True)
    q66_11c = models.CharField(max_length=200, blank=True, null=True)
    q66_12a = models.CharField(max_length=200, blank=True, null=True)
    q66_12b = models.CharField(max_length=200, blank=True, null=True)
    q61_12c = models.CharField(max_length=200, blank=True, null=True)
    q66_13a = models.CharField(max_length=200, blank=True, null=True)
    q66_13b = models.CharField(max_length=200, blank=True, null=True)
    q66_13c = models.CharField(max_length=200, blank=True, null=True)
    q66_14a = models.CharField(max_length=200, blank=True, null=True)
    q66_14b = models.CharField(max_length=200, blank=True, null=True)
    q66_14c = models.CharField(max_length=200, blank=True, null=True)
    q66_15a = models.CharField(max_length=200, blank=True, null=True)
    q66_15b = models.CharField(max_length=200, blank=True, null=True)
    q66_15c = models.CharField(max_length=200, blank=True, null=True)
    q66_16a = models.CharField(max_length=200, blank=True, null=True)
    q66_16b = models.CharField(max_length=200, blank=True, null=True)
    q66_16c = models.CharField(max_length=200, blank=True, null=True)
    q66_17a = models.CharField(max_length=200, blank=True, null=True)
    q66_17b = models.CharField(max_length=200, blank=True, null=True)
    q66_17c = models.CharField(max_length=200, blank=True, null=True)
    q66_18a = models.CharField(max_length=200, blank=True, null=True)
    q66_18b = models.CharField(max_length=200, blank=True, null=True)
    q66_18c = models.CharField(max_length=200, blank=True, null=True)
    q66_19a = models.CharField(max_length=200, blank=True, null=True)
    q66_19b = models.CharField(max_length=200, blank=True, null=True)
    q66_19c = models.CharField(max_length=200, blank=True, null=True)
    q66_20a = models.CharField(max_length=200, blank=True, null=True)
    q66_20b = models.CharField(max_length=200, blank=True, null=True)
    q66_20c = models.CharField(max_length=200, blank=True, null=True)
    q66_21a = models.CharField(max_length=200, blank=True, null=True)
    q66_21b = models.CharField(max_length=200, blank=True, null=True)
    q66_21c = models.CharField(max_length=200, blank=True, null=True)
    q66_22a = models.CharField(max_length=200, blank=True, null=True)
    q66_22b = models.CharField(max_length=200, blank=True, null=True)
    q66_22c = models.CharField(max_length=200, blank=True, null=True)
    q66_23a = models.CharField(max_length=200, blank=True, null=True)
    q66_23b = models.CharField(max_length=200, blank=True, null=True)
    q66_23c = models.CharField(max_length=200, blank=True, null=True)
    q66_24a = models.CharField(max_length=200, blank=True, null=True)
    q66_24b = models.CharField(max_length=200, blank=True, null=True)
    q66_24c = models.CharField(max_length=200, blank=True, null=True)
    q66_25a = models.CharField(max_length=200, blank=True, null=True)
    q66_25b = models.CharField(max_length=200, blank=True, null=True)
    q66_25c = models.CharField(max_length=200, blank=True, null=True)
    q66_26a = models.CharField(max_length=200, blank=True, null=True)
    q66_26b = models.CharField(max_length=200, blank=True, null=True)
    q66_26c = models.CharField(max_length=200, blank=True, null=True)
    q66_27a = models.CharField(max_length=200, blank=True, null=True)
    q66_27b = models.CharField(max_length=200, blank=True, null=True)
    q66_27c = models.CharField(max_length=200, blank=True, null=True)
    q66_28a = models.CharField(max_length=200, blank=True, null=True)
    q66_28b = models.CharField(max_length=200, blank=True, null=True)
    q66_28c = models.CharField(max_length=200, blank=True, null=True)
    q66_29a = models.CharField(max_length=200, blank=True, null=True)
    q66_29b = models.CharField(max_length=200, blank=True, null=True)
    q66_29c = models.CharField(max_length=200, blank=True, null=True)
    q66_31a = models.CharField(max_length=200, blank=True, null=True)
    q66_31b = models.CharField(max_length=200, blank=True, null=True)
    q66_31c = models.CharField(max_length=200, blank=True, null=True)
    q67 = models.CharField(max_length=200, blank=True, null=True)
    q67_1a = models.CharField(max_length=200, blank=True, null=True)
    q67_1b = models.CharField(max_length=200, blank=True, null=True)
    q67_1f = models.CharField(max_length=200, blank=True, null=True)
    q67_1g = models.CharField(max_length=200, blank=True, null=True)
    q67_2a = models.CharField(max_length=200, blank=True, null=True)
    q67_2b = models.CharField(max_length=200, blank=True, null=True)
    q67_2c = models.CharField(max_length=200, blank=True, null=True)
    q67_2f = models.CharField(max_length=200, blank=True, null=True)
    q67_2g = models.CharField(max_length=200, blank=True, null=True)
    q67_3a = models.CharField(max_length=200, blank=True, null=True)
    q67_3c = models.CharField(max_length=200, blank=True, null=True)
    q67_3e = models.CharField(max_length=200, blank=True, null=True)
    q67_3g = models.CharField(max_length=200, blank=True, null=True)
    q67_5a = models.CharField(max_length=200, blank=True, null=True)
    q67_5c = models.CharField(max_length=200, blank=True, null=True)
    q67_5g = models.CharField(max_length=200, blank=True, null=True)
    q67_6a = models.CharField(max_length=200, blank=True, null=True)
    q67_6c = models.CharField(max_length=200, blank=True, null=True)
    q67_6d = models.CharField(max_length=200, blank=True, null=True)
    q67_6g = models.CharField(max_length=200, blank=True, null=True)
    q67_7a = models.CharField(max_length=200, blank=True, null=True)
    q67_7c = models.CharField(max_length=200, blank=True, null=True)
    q67_7d = models.CharField(max_length=200, blank=True, null=True)
    q67_7g = models.CharField(max_length=200, blank=True, null=True)
    q67_8 = models.CharField(max_length=200, blank=True, null=True)
    q67_8a = models.CharField(max_length=200, blank=True, null=True)
    q67_8b = models.CharField(max_length=200, blank=True, null=True)
    q67_8d = models.CharField(max_length=200, blank=True, null=True)
    q67_8e = models.CharField(max_length=200, blank=True, null=True)
    q67_8f = models.CharField(max_length=200, blank=True, null=True)
    q68 = models.CharField(max_length=200, blank=True, null=True)
    q69 = models.CharField(max_length=200, blank=True, null=True)
    q69_1 = models.CharField(max_length=200, blank=True, null=True)
    q69_2 = models.CharField(max_length=200, blank=True, null=True)
    q150 = models.CharField(max_length=200, blank=True, null=True)
    q150_1 = models.CharField(max_length=200, blank=True, null=True)
    q150_2 = models.CharField(max_length=200, blank=True, null=True)
    q150_3 = models.CharField(max_length=200, blank=True, null=True)
    q70_1 = models.CharField(max_length=200, blank=True, null=True)
    q70_2 = models.CharField(max_length=200, blank=True, null=True)
    q70_3 = models.CharField(max_length=200, blank=True, null=True)
    q70_4 = models.CharField(max_length=200, blank=True, null=True)
    q70_5 = models.CharField(max_length=200, blank=True, null=True)
    q70_6 = models.CharField(max_length=200, blank=True, null=True)
    q70_7 = models.CharField(max_length=200, blank=True, null=True)
    q70_8 = models.CharField(max_length=200, blank=True, null=True)
    q70_9 = models.CharField(max_length=200, blank=True, null=True)
    q70_10 = models.CharField(max_length=200, blank=True, null=True)
    q70_11 = models.CharField(max_length=200, blank=True, null=True)
    q70_12 = models.CharField(max_length=200, blank=True, null=True)
    q71_1 = models.CharField(max_length=200, blank=True, null=True)
    q71_2 = models.CharField(max_length=200, blank=True, null=True)
    q71_3 = models.CharField(max_length=200, blank=True, null=True)
    q71_4 = models.CharField(max_length=200, blank=True, null=True)
    q71_5 = models.CharField(max_length=200, blank=True, null=True)
    q71_6 = models.CharField(max_length=200, blank=True, null=True)
    q71_7 = models.CharField(max_length=200, blank=True, null=True)
    q71_8 = models.CharField(max_length=200, blank=True, null=True)
    q71_9 = models.CharField(max_length=200, blank=True, null=True)
    q71_10 = models.CharField(max_length=200, blank=True, null=True)
    q71_11 = models.CharField(max_length=200, blank=True, null=True)
    q71_12 = models.CharField(max_length=200, blank=True, null=True)
    q71_13 = models.CharField(max_length=200, blank=True, null=True)
    q71_14 = models.CharField(max_length=200, blank=True, null=True)
    q72 = models.CharField(max_length=200, blank=True, null=True)
    q73 = models.CharField(max_length=200, blank=True, null=True)
    q73_1 = models.CharField(max_length=200, blank=True, null=True)
    q75 = models.CharField(max_length=200, blank=True, null=True)
    q78 = models.CharField(max_length=200, blank=True, null=True)
    q79 = models.CharField(max_length=200, blank=True, null=True)
    q80 = models.CharField(max_length=200, blank=True, null=True)
    q81_1 = models.CharField(max_length=200, blank=True, null=True)
    q81_2 = models.CharField(max_length=200, blank=True, null=True)
    q81_3 = models.CharField(max_length=200, blank=True, null=True)
    q81_4 = models.CharField(max_length=200, blank=True, null=True)
    q81_5 = models.CharField(max_length=200, blank=True, null=True)
    q81_6 = models.CharField(max_length=200, blank=True, null=True)
    q81_7 = models.CharField(max_length=200, blank=True, null=True)
    q81_8 = models.CharField(max_length=200, blank=True, null=True)
    q81_9 = models.CharField(max_length=200, blank=True, null=True)
    q81_10 = models.CharField(max_length=200, blank=True, null=True)
    q81_11 = models.CharField(max_length=200, blank=True, null=True)
    q81_12 = models.CharField(max_length=200, blank=True, null=True)
    q81_13 = models.CharField(max_length=200, blank=True, null=True)
    q83 = models.CharField(max_length=200, blank=True, null=True)
    q84 = models.CharField(max_length=200, blank=True, null=True)
    q85 = models.CharField(max_length=200, blank=True, null=True)
    q85_1 = models.CharField(max_length=200, blank=True, null=True)
    q86 = models.CharField(max_length=200, blank=True, null=True)
    q86_1 = models.CharField(max_length=200, blank=True, null=True)
    q89 = models.CharField(max_length=200, blank=True, null=True)
    q90 = models.CharField(max_length=200, blank=True, null=True)
    q91 = models.CharField(max_length=200, blank=True, null=True)
    q91_1 = models.CharField(max_length=200, blank=True, null=True)
    q92 = models.CharField(max_length=200, blank=True, null=True)
    q93 = models.CharField(max_length=200, blank=True, null=True)
    q94 = models.CharField(max_length=200, blank=True, null=True)
    q95 = models.CharField(max_length=200, blank=True, null=True)
    q98_1 = models.CharField(max_length=200, blank=True, null=True)
    q101_1 = models.CharField(max_length=200, blank=True, null=True)
    q101_2 = models.CharField(max_length=200, blank=True, null=True)
    q101_3 = models.CharField(max_length=200, blank=True, null=True)
    q101_4 = models.CharField(max_length=200, blank=True, null=True)
    q101_5 = models.CharField(max_length=200, blank=True, null=True)
    q101_6 = models.CharField(max_length=200, blank=True, null=True)
    q109_1 = models.CharField(max_length=200, blank=True, null=True)
    q109_2 = models.CharField(max_length=200, blank=True, null=True)
    q109_3 = models.CharField(max_length=200, blank=True, null=True)
    q110 = models.CharField(max_length=200, blank=True, null=True)
    q111 = models.CharField(max_length=200, blank=True, null=True)
    q112 = models.CharField(max_length=200, blank=True, null=True)
    q114 = models.CharField(max_length=200, blank=True, null=True)
    q114_1 = models.CharField(max_length=200, blank=True, null=True)
    q115 = models.CharField(max_length=200, blank=True, null=True)
    q116 = models.CharField(max_length=200, blank=True, null=True)
    q117 = models.CharField(max_length=200, blank=True, null=True)
    q118 = models.CharField(max_length=200, blank=True, null=True)
    q119 = models.CharField(max_length=200, blank=True, null=True)
    q127_1 = models.CharField(max_length=200, blank=True, null=True)
    q129 = models.CharField(max_length=200, blank=True, null=True)
    q129_1 = models.CharField(max_length=200, blank=True, null=True)
    q129_2 = models.CharField(max_length=200, blank=True, null=True)
    q129_3 = models.CharField(max_length=200, blank=True, null=True)
    q129_4 = models.CharField(max_length=200, blank=True, null=True)
    q129_5 = models.CharField(max_length=200, blank=True, null=True)
    q129_6 = models.CharField(max_length=200, blank=True, null=True)
    q129_9 = models.CharField(max_length=200, blank=True, null=True)
    q129_10 = models.CharField(max_length=200, blank=True, null=True)
    q129_13 = models.CharField(max_length=200, blank=True, null=True)
    q129_14 = models.CharField(max_length=200, blank=True, null=True)
    q129_15 = models.CharField(max_length=200, blank=True, null=True)
    q129_16 = models.CharField(max_length=200, blank=True, null=True)
    q130 = models.CharField(max_length=200, blank=True, null=True)
    q131 = models.CharField(max_length=200, blank=True, null=True)
    q132 = models.CharField(max_length=200, blank=True, null=True)
    q133 = models.CharField(max_length=200, blank=True, null=True)
    q135 = models.CharField(max_length=200, blank=True, null=True)
    instanceid = models.CharField(max_length=200, blank=True, null=True)
    key = models.CharField(max_length=200, primary_key=True, default='eeeeee')
    sn = models.CharField(max_length=200, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = True
        db_table = 'household_data'

class PersonalQuestionaireMatch(models.Model):
    small = models.CharField(max_length=150, primary_key=True)
    original = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_questionaire_match'

class PersonalQuestions(models.Model):
    fid = models.BigIntegerField(blank=True, null=True)
    linked_table = models.CharField(max_length=200, blank=True, null=True)
    column_category = models.CharField(max_length=200, blank=True, null=True)
    meta_column = models.CharField(max_length=200, blank=True, null=True)
    odk_data_type = models.CharField(max_length=200, blank=True, null=True)
    choice_list = models.CharField(max_length=200, blank=True, null=True)
    odk_question = models.CharField(max_length=200, blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    datatype = models.CharField(max_length=200, blank=True, null=True)
    required = models.CharField(max_length=200, blank=True, null=True)
    sn = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'personal_questions'

class PersonalData(models.Model):
    fid = models.BigIntegerField(blank=True, null=True)
    ward = models.CharField(max_length=200, blank=True, null=True)
    q13 = models.CharField(max_length=200, blank=True, null=True)
    q14 = models.CharField(max_length=200, blank=True, null=True)
    q15 = models.CharField(max_length=200, blank=True, null=True)
    q16 = models.CharField(max_length=200, blank=True, null=True)
    age_group = models.CharField(max_length=200, blank=True, null=True)
    q17 = models.CharField(max_length=200, blank=True, null=True)
    q17_1 = models.CharField(max_length=200, blank=True, null=True)
    q18 = models.CharField(max_length=200, blank=True, null=True)
    q18_1 = models.CharField(max_length=200, blank=True, null=True)
    q19 = models.CharField(max_length=200, blank=True, null=True)
    q19_1 = models.CharField(max_length=200, blank=True, null=True)
    q20 = models.CharField(max_length=200, blank=True, null=True)
    q21 = models.CharField(max_length=200, blank=True, null=True)
    q21_1 = models.CharField(max_length=200, blank=True, null=True)
    q22 = models.CharField(max_length=200, blank=True, null=True)
    q23 = models.CharField(max_length=200, blank=True, null=True)
    q24 = models.CharField(max_length=200, blank=True, null=True)
    q25 = models.CharField(max_length=200, blank=True, null=True)
    q25_1 = models.CharField(max_length=200, blank=True, null=True)
    q151 = models.CharField(max_length=200, blank=True, null=True)
    q151_1 = models.CharField(max_length=200, blank=True, null=True)
    q151_2 = models.CharField(max_length=200, blank=True, null=True)
    q25_2 = models.CharField(max_length=200, blank=True, null=True)
    q25_3 = models.CharField(max_length=200, blank=True, null=True)
    q25_4 = models.CharField(max_length=200, blank=True, null=True)
    q25_5 = models.CharField(max_length=200, blank=True, null=True)
    q26 = models.CharField(max_length=200, blank=True, null=True)
    q27 = models.CharField(max_length=200, blank=True, null=True)
    q28 = models.CharField(max_length=200, blank=True, null=True)
    q29 = models.CharField(max_length=200, blank=True, null=True)
    q29_1 = models.CharField(max_length=200, blank=True, null=True)
    q30 = models.CharField(max_length=200, blank=True, null=True)
    q30_1 = models.CharField(max_length=200, blank=True, null=True)
    q30_2 = models.CharField(max_length=200, blank=True, null=True)
    q30_3 = models.CharField(max_length=200, blank=True, null=True)
    q31 = models.CharField(max_length=200, blank=True, null=True)
    q32 = models.CharField(max_length=200, blank=True, null=True)
    q32_1 = models.CharField(max_length=200, blank=True, null=True)
    q33 = models.CharField(max_length=200, blank=True, null=True)
    q126 = models.CharField(max_length=200, blank=True, null=True)
    q127 = models.CharField(max_length=200, blank=True, null=True)
    q120 = models.CharField(max_length=200, blank=True, null=True)
    q121 = models.CharField(max_length=200, blank=True, null=True)
    q122 = models.CharField(max_length=200, blank=True, null=True)
    q123 = models.CharField(max_length=200, blank=True, null=True)
    q87 = models.CharField(max_length=200, blank=True, null=True)
    q88_4 = models.CharField(max_length=200, blank=True, null=True)
    q88_5 = models.CharField(max_length=200, blank=True, null=True)
    q88_6 = models.CharField(max_length=200, blank=True, null=True)
    q88_6_1 = models.CharField(max_length=200, blank=True, null=True)
    q103 = models.CharField(max_length=200, blank=True, null=True)
    q104_4 = models.CharField(max_length=200, blank=True, null=True)
    q104_4_1 = models.CharField(max_length=200, blank=True, null=True)
    # parent_key = models.CharField(max_length=200, blank=True, null=True)
    parent_key = models.ForeignKey(HouseholdData, on_delete=models.CASCADE, default='uuid:c181415b-19ad-43a1-8580-1f58cd56522d')
    key = models.CharField(max_length=200, blank=True, null=True)
    # sn = models.CharField(max_length=200, blank=True, null=True)
    sn = models.CharField(primary_key=True, max_length=200, default='eeeeeee')

    class Meta:
        managed = True
        db_table = 'personal_data'
