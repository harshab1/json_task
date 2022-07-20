import json
import requests
import data_request

url = "http://api.worldbank.org/v2/countries/IND/indicators/SP.POP.TOTL?per_page=5000&format=json"
data = data_request.get_data(url)
print(data)

population_data = dict()

for item in data[1]:
  year = item['date']
  population = item['value']
  population_data[year] = population

print(population_data)


data_request.save_json('data_population.json', population_data)