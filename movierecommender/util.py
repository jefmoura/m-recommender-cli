#
# Author: Jeferson Moura
# Germany - 2nd February
#
import json


def get_data(file_name):
    json_map = {}
    with open(file_name, 'r') as js_file:
        json_data = js_file.read()
        json_map = json.loads(json_data)
    return json_map
