# Significance of this project: 
# reference website: https://www.dataquest.io/blog/python-api-tutorial/
# I will practice using API with from mnowotka's JSON of chemical molecules

#getting some data from a given webstie so we can see its status (404, 200, etc.)
import requests
response = requests.get("https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL25.json")

print(response.status_code)

#seeing the data from the JSON we are using
print(response.json())
