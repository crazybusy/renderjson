from json2html import *
import json


PARAMETERS_FILE = 'json_to_html.txt'
OUTPUT_FILE="temp.html"

if __name__ == "__main__":
    

    from simple_parameters import simple_parameters
    parser = simple_parameters.SimpleParser(PARAMETERS_FILE )
    (options, args) = parser.resolve_parameters(sys.argv)

    
    with open(str(options.file)) as infile:
        all_data = json.load(infile)        
    html = json2html.convert(json = all_data)


    with open(OUTPUT_FILE , 'w') as outfile:
        outfile.writelines(html)
        outfile.close()
    

    
