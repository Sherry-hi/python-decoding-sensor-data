
from datetime import date

class HouseInfo:
    def houseInfo(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        for record in self.data:
            if rec_area == 0:
                field_data.append = record(field)
            elif rec_area == record['area']:
                field_data.append = record(field)
        return field_data
    
    def get_data_by_data(self, field, rec_date = date()):
        field_data = []
        for record in self.data:
            if rec_date == strftime(date(),"%m/%d/%y"):
                field_data.append = record(field)
        return field_data
            
                
                
                
        