# renderjson
Working with json files


<h1>get_json</h1> is generic utility for interacting with JSON API's on the web. You need to create a template file for the API wit the values of the parameters that the API takes and provide this file as parameter. You can optionally specify a search string for the API on the command line. Eg. template file for google maps search

{
"url":"https://maps.googleapis.com/maps/api/geocode/json?",
"search_term":"address",
"parameters":{
	"key": "YOURKEY",        
	"address":"London, England"     
}
}

If you call get_json on the commnd line as below, it'll search google maps using the above details for London England and output the json result. 
python get_json -f /path/to/mapseach.json

If you specify some arguements on the command line, it'll search for those instead of the default value on file. E.g.
python get_json -f /path/to/mapseach.json Your search string here

<h1>json_cli</h1> is a utlity to display json files on the command line in a readabe format. It basically displays the keys that have values in a YAML like format. The objective is to CSS these somehow and render the json directly using CSS. The paths/keys (XPATH like) displayed should support easy templating using CSS. 
<h4>Sample JSON</h4>
{
    "title": "Person",
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "age": {
            "description": "Age in years",
            "type": "integer",
            "minimum": 0
        }
    },
    "required": ["firstName", "lastName"]
}
<h4Output by json_cli</h4> using 
python json_cli.py samples/basic.txt

1: title(<class 'str'>): Person
1: type(<class 'str'>): object
3: properties/firstName/type(<class 'str'>): string
3: properties/lastName/type(<class 'str'>): string
3: properties/age/description(<class 'str'>): Age in years
3: properties/age/type(<class 'str'>): integer
3: properties/age/minimum(<class 'int'>): 0
2: required/list index: 0(<class 'str'>): firstName
2: required/list index: 1(<class 'str'>): lastName

