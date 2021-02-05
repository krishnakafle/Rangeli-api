from rest_framework import serializers

from dataAPI.models import HouseholdQuestions, PersonalQuestions, HouseholdData, AttributeLookup, PersonalData


class houseHoldQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdQuestions
        fields = ['odk_question', 'display_name', 'column_category']

class personalQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalQuestions
        fields = ['odk_question', 'display_name', 'column_category', 'odk_data_type']

class lookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeLookup
        fields = ['name', 'label']

class DataSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=255)
    value = serializers.IntegerField()

class personalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        # fields = ['ward', 'q13', 'q14', 'q15', 'q16']
        exclude = ['sn', 'parent_key', 'key']

class householdMicroDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdData
        fields = ['ward', 'tol', 'roadname', 'q7', 'q9', 'total_pop']
        # exclude = ['sn', 'parent_key', 'key']

class personalMicroDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = ['ward', 'q13', 'q15', 'q16', 'q23', 'q26', 'q30']
        # exclude = ['sn', 'parent_key', 'key']