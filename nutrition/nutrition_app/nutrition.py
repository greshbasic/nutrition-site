from .request_data import *

class NutritionInfo:
    def __init__(self, name):
        data_from_name = get_data_from_name(name)
        try:
            barcode = data_from_name['items'][0]['ean']
            self.data = get_data_from_barcode(barcode)
        except KeyError:
            print(data_from_name)
            self.data = {'status': False}
    
    def get_calories(self):
        if not self.data['status']:
            return "Calories not found"
        try:
            return int(self.data['product']['nutriments']['energy_value'])
        except KeyError:
            return "Calories not found"
        
    def get_name(self):
        if not self.data['status']:
            return "Calories not found"
        try:
            return self.data['product']['product_name']
        except KeyError:
            return "Name not found"
    
    def get_nutrition_grade(self):
        if not self.data['status']:
            return "Calories not found"
        try:
            return self.data['product']['nutrition_grades']
        except KeyError:
            return "Nutrition grade not found"
        
    
