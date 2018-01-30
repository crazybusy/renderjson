import json, os
import re, types

class json_cli():
    def setmode(self,  mode):
        self .mode= mode
        self.fields = {}
        return

    def handle_pair(self, level, key, value, path=None):
        type = self.get_type(value)

        if path :
            path +="/"+key
        else:
            path =key

        if self.mode== "READ":
            if key == "parameters" and type==list:
                for item in value:
                    self.get_field(item)

        if type == dict:
            for item in value:
                self.handle_pair(level+1,  item, value[item],  path)
        elif type == list:
            for i in value:                
                self.handle_pair(level+1,"list index: " +
                                 str(value.index(i)),i,  path)
        else:
            if self.mode == "SHOW":
                self.render(level, type, key, value, path)
        return

    def get_field(self,  field):
        print('Enter {}: '.format(field.get('name')))
        input_value = input()

        self.fields[field.get('name')]= input_value
        return 

    
    def get_type(self, value):
        if isinstance(value, str):
            type=str
        elif isinstance(value, bool):
            type=bool
        elif isinstance(value, int):
            type=int
        elif isinstance(value, float):
            type = float
        elif isinstance(value, list):
            type = list
        elif isinstance(value, dict):
            type = dict                      
        return type
    
    
    def render(self,  level, type, key, value, path):
        print("{}: {}({}): {}".format(level, path, type,  value))
        return

    def load_file(self, data_file):
        if os.path.isfile(data_file):
            with open(data_file) as infile:
                self.all_data = json.load(infile)

                self.handle_pair( 0, "", self.all_data)
        return
    def load_data(self, all_data):
        self.handle_pair( 0, "", all_data)
        return
    
    def dump_file(self, filename):
        with open(filename, 'w') as outfile:
                json.dump(self.fields, outfile)
        return


        
if __name__ == "__main__":
    temp = json_cli()
    temp.setmode( "SHOW")
    temp.load_file("samples/basic.txt")
    #temp.dump_file("values_json_cli.json")

    
