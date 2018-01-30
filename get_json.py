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
    if os.path.isfile(data_file):
        with open(data_file) as infile:
            return json.load(infile)
    else
        logger.debug("File {} not found".format(data_file))
    return 

PARAMETERS_STRING = "parameters"
URL_STRING = 'url'
SEARCH_TERM_STRING='search_term'
PARAMETERS_FILE = 'get_json.txt'

if __name__ == "__main__":
    

    from simple_parameters import simple_parameters
    parser = simple_parameters(PARAMETERS_FILE )
    (options, args) = parser.resolve_parameters(sys.argv)

    logger.debug("Input parameters:{}".format(options))

    if options.file:
        data = load_file(str(options.file))
        
        parameters = data[PARAMETERS_STRING]

        if args[1:]:
            parameters[data[SEARCH_TERM_STRING]] = args[1:]

        parameters = data[PARAMETERS_STRING]

        url = data[URL_STRING]
        url += urllib.parse.urlencode(parameters)

        show_result = json_cli()
        show_result.setmode("SHOW")
        show_result.load_data(requests.get(url).json())
