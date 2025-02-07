from rest_framework import serializers

class APISuccessSerializer(serializers.Serializer):
  """

    Required JSON Response Format (200 OK):
    {
        "number": 371,
        "is_prime": false,
        "is_perfect": false,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,  // sum of its digits
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    }

  """

  number = serializers.IntegerField()
  is_prime = serializers.BooleanField()
  is_perfect = serializers.BooleanField()
  properties = serializers.ListField()
  digit_sum = serializers.IntegerField()
  fun_fact = serializers.CharField()

  class Meta:
    fields = ["__all__"]

class APIFailSerializer(serializers.Serializer):
  """
    Required JSON Response Format (400 Bad Request)
    {
        "number": "alphabet",
        "error": true
    }
  """
  number = serializers.IntegerField()
  error = serializers.BooleanField()

  class Meta:
    fields = ["__all__"]

