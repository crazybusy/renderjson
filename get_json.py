import requests, urllib
import os, sys
import json
import logging
from json_cli import json_cli

#----------------- Logger import ---------------------------------

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#------------------Functions--------------------------------------
def load_file(data_file):
    with open(data_file) as infile:
            return json.load(infile)

PARAMETERS_STRING = "parameters"
URL_STRING = 'url'
SEARCH_TERM_STRING='search_term'
PARAMETERS_FILE = 'get_json.txt'

if __name__ == "__main__":
    

    from simple_parameters import simple_parameters
    parser = simple_parameters.SimpleParser(PARAMETERS_FILE )
    (options, args) = parser.resolve_parameters(sys.argv)

    logger.debug("Input parameters:{}".format(args))

    if os.path.isfile(options.file):
        data = load_file(str(options.file))    
        
        parameters = data[PARAMETERS_STRING]

        if args[1:]:
            parameters[data[SEARCH_TERM_STRING]] = str(args[1:]).strip('[]\'')
        
        url = data[URL_STRING]
        url += urllib.parse.urlencode(parameters)
        
        show_result = json_cli()
        show_result.load_data(requests.get(url).json())
