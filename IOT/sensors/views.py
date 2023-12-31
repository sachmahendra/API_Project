from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
import ast
import uuid


#  API TO RECIVE DATA FROM SENSORE//////////////////////// 
class postsensorData(APIView):
    def post(self,request):
        serializerdata = postsensorDataSerializer(data=request.data)
        if serializerdata.is_valid():
            #orm to create new record in db
            sensor.objects.create(**serializerdata.data)
            message = {'message':"Sensor Data Submitted Sucessfully"}
            return Response(message,status=status.HTTP_201_CREATED)
        return Response(serializerdata.errors, status=status.HTTP_400_BAD_REQUEST)
  
#  API TO GET WHOLE DATA FROM DATABASE////////////////////////////////////   
class getsensorData(APIView):
    def get(self,request):
        try:
            sensorData = list(sensor.objects.filter().values())
            return Response(sensorData, status=status.HTTP_200_OK)
        except Exception as e:
            message = {'Error': str(e)}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
  
#   API TO GET ANY PARTICULER DATA FROM THE ALL DATASET ////////////////////////      
class getsensorDataDetails(APIView):
    def get(self,request,sensorid):
        try:
            sensorData = list(sensor.objects.filter(sensor_id=sensorid).values())
            return Response(sensorData, status=status.HTTP_200_OK)
        except Exception as e:
            message = {'Error': str(e)}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)            

# API TO UPDATE DATA /////////////////////////////////////
class updatesensorDataDetails(APIView):
    def put(self,request):
        serializerdata = updatesensorDataSerializer(data=request.data)
        if serializerdata.is_valid():
            sensor_name = serializerdata.data["sensor_name"]
            sensor_status= serializerdata.data["sensor_status"]
            #orm to create new record in db
            sensor.objects.filter(sensor_name=sensor_name).update(sensor_status=sensor_status)
            message = {'message':"Sensor Data updated Sucessfully"}
            return Response(message,status=status.HTTP_201_CREATED)
        return Response(serializerdata.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class deletesensorData(APIView):
    def delete(self,request,sensor_id):
        try:
            sensor.objects.filter(sensor_id=sensor_id).delete()
            message ={"message": "Sensor Data deleted successfully"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = {'Error': str(e)}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
class notifyUser(APIView):
    def post(self,request):
        serializerdata = NotifySerializer(data=request.data)

        if serializerdata.is_valid():
            sensor_name = serializerdata.data["sensor_name"]
            customer_id = serializerdata.data["customer_id"]

            sensorList = list(sensor.objects.filter(sensor_name=sensor_name).values())
            #print("sensorList",sensorList)
            for i in sensorList:
                i["sensor_value"] =ast.literal_eval( i["sensor_value"])
                print(i)
                sensordata = i["sensor_value"]

                if sensordata["x-asis"]>200 and sensordata["y-asis"]>200 and sensordata["z-asis"]>200:
                    Notification.objects.create(
                        customer_id_id=customer_id,
                        sensor_id_id=i["sensor_id"],
                        notification_id= str(uuid.uuid4()),
                        message ="Alert!!!! Sensor Exceed the Normal Value"
                    )

            message = {'message':"Notification Sent to the Customer Sucessfully"}
            return Response(message,status=status.HTTP_201_CREATED)
        
        
        
class notifyUser(APIView):
    def post(self,request):
        serializerdata = NotifySerializer(data=request.data)

        if serializerdata.is_valid():
            sensor_name = serializerdata.data["sensor_name"]
            customer_id = serializerdata.data["customer_id"]
            checkparam = serializerdata.data["checkparam"]

            sensorList = list(sensor.objects.filter(sensor_name=sensor_name).values())
            #print("sensorList",sensorList)
            for i in sensorList:
                i["sensor_value"] = ast.literal_eval( i["sensor_value"])
                print(i)
                sensordata = i["sensor_value"]

                if sensordata["x-asis"]>checkparam["x"] and sensordata["y-asis"]>checkparam["y"] and sensordata["z-asis"]>checkparam["z"]:
                    Notification.objects.create(
                        customer_id_id=customer_id,
                        sensor_id_id=i["sensor_id"],
                        notification_id= str(uuid.uuid4()),
                        message ="Alert!!!! Sensor Exceed the Normal Value"
                    )

            message = {'message':"Notification Sent to the Customer Sucessfully"}
            return Response(message,status=status.HTTP_201_CREATED)