from rest_framework import serializers

class postsensorDataSerializer(serializers.Serializer):
    sensor_id = serializers.CharField(max_length=100)
    sensor_name = serializers.CharField(max_length=100)
    sensor_status = serializers.CharField(max_length=20)
    sensor_value = serializers.JSONField()
    sensor_timestamp = serializers.DateTimeField()
    
    
class updatesensorDataSerializer(serializers.Serializer):
    sensor_name = serializers.CharField(max_length=100,required=False)
    sensor_status = serializers.CharField(max_length=20,required = False)
   
   
class NotifySerializer(serializers.Serializer):
    sensor_name = serializers.CharField(max_length=100,required=False)
    customer_id = serializers.CharField(max_length=100,required=False)
    
    
class NotifySerializer(serializers.Serializer):
    sensor_name = serializers.CharField(max_length=100,required=False)
    customer_id = serializers.CharField(max_length=100,required=False)
    checkparam = serializers.JSONField()
    
    
    
#     student Django

# student table - student Details
# Attendance  -- connected to student table


# getAPI -- all student detais
# getAPI to get particular student\
# updateAPI - update any mobile of any student
# deleteAPi - student id deleteAPi

# getAPI - if I want to know the attendance of particular
# student ID