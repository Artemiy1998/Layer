
import json

#@synchronized
class Scene3Ddata:
    #@synchronized
    def __init__(self):
        self.data = {}
        self.exit = False

   # @synchronized
    def set(self, data):
        temp_data = data.split(', ')
        for item in temp_data:
            temp_json = json.load('{'+item+'}')
            self.data.update(temp_json)

   # @synchronized
    def get(self):
        return json.dump(self.data)



json_data = Scene3Ddata()
