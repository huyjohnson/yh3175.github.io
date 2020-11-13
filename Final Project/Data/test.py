### JSON FILES
##import json
##import objectpath
##
##
### Opening JSON file
##f = open("allcounties_import.json")
##
### returns JSON object as a dictionary
##jdata = json.load(f)
##
##tree_obj = objectpath.Tree(jdata)
##
##print(tuple(tree_obj.execute('$..FIPS')))

# CSV file
def csv_list():
    """
    Extract a column from csv file and place into list.
    """
    with open('Combined_amz.csv', 'r') as csv_file:
        lines = csv_file.readlines()

    fips = []
    for line in lines:
        data = line.split(',')
        fips.append(data[5])

    del fips[0]
    return fips
    
# JSON FILES
import json

with open('allcounties_import.json') as json_file:
    jdata = json.load(json_file)

print(jdata['features']['FIPS'])
