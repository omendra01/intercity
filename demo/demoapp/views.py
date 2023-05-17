from rest_framework import viewsets
from rest_framework.response import Response
import requests


class ResultViews(viewsets.ViewSet):
    def list(self,request):
    #*******************Bikes Url****************************    
        bikes_url ="https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
        bike_data = requests.get(bikes_url).json()
        bike = bike_data['data']['bikes']
        bike_status =sum([i['is_reserved'] for i in bike])
     

    #***************************Station Url***********************************
        active_station =0
        station_url ="https://gbfs.divvybikes.com/gbfs/en/station_status.json"
        station_data = requests.get(station_url).json()
        sts = station_data['data']['stations']
        Total_Docks_avl= sum([i['num_docks_available'] for i in sts])
        Total_Bikes_avl = sum([i['num_ebikes_available'] for i in sts])
        Total_station_active =([i['station_status'] for i in sts])
        for i in Total_station_active:
            if i =='active':
                active_station+=1
        return Response({'Total_Docks_avl':Total_Docks_avl,'Total_Bikes_avl':Total_Bikes_avl,'Total_station_active':active_station,'bike_status':bike_status})

