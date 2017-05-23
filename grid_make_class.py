import numpy as np
import pandas as pd

class GM:
    #入力：グリッドサイズ，始点の緯度経度，終点の緯度経度
    #出力：[[緯度（低い），緯度（高い），経度（低い），経度（高い）],…]
    def __init__(self, dist, lat, lon, threshold_lat, threshold_lon):
        self.dist = dist
        self.lat = lat
        self.lon = lon
        self.threshold_lat = threshold_lat
        self.threshold_lon = threshold_lon
    
    def calc_lat(self, lat):
        #緯度を入力すると500mプラスした緯度を返す
        c_lat = 2 * np.pi * 6356752.314
        lat_par_meter = 360 / c_lat
        result_lat = lat + lat_par_meter * self.dist
        
        return result_lat
    
    def calc_lon(self, lat, lon):
        #経度を入力すると500mプラスした経度を返す
        r = 6378136.6 * np.cos(np.radians(lat))
        c_lon = 2 * np.pi * r
        lon_par_meter = 360 / c_lon
        result_lon = lon + lon_par_meter * self.dist
        
        return result_lon
    
    def mesh_make(self):
        #緯度、経度のリストを返す
        lat_list = []
        lon_list = []
        mesh_temp = []
        mesh_list = [] #緯度（低い），緯度（高い），経度（低い），経度（高い）の順
        
        lat_list.append(self.lat)        
        while self.lat <= self.threshold_lat:
            self.lat = self.calc_lat(self.lat)
            lat_list.append(self.lat)
        
        lon_list.append(self.lon)
        for row in lat_list:
            while self.lon <= self.threshold_lon:
                self.lon = self.calc_lon(row, self.lon)
                lon_list.append(self.lon)
            
        for i in range(len(lat_list)-1):
            for j in range(len(lon_list)-1):
                mesh_temp.append(lat_list[i])
                mesh_temp.append(lat_list[i+1])
                mesh_temp.append(lon_list[j])
                mesh_temp.append(lon_list[j+1])
                mesh_list.append(mesh_temp)
                mesh_temp = []
                
                
        return mesh_list
