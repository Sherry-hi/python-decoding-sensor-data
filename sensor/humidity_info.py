from house_info import HouseInfo

class HumidityData(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec)*100)
            
    def get_data_by_area(self, field, rec_area=0):
        recs = super().get_data_by_area(field, rec_area)
        return self._convert_data(recs)
    
    def get_data_by_date(self, field, rec_date=...):
        recs = super().get_data_by_date(field, rec_date)
        return self._convert_data(recs)
    