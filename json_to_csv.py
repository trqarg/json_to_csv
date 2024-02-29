from cherrypicker import CherryPicker
import json
import pandas as pd

with open('Wegmans_Extract.json') as file:
    data = json.load(file)

picker = CherryPicker(data)
flat = picker['products'].flatten().get()
df = pd.DataFrame(flat)
print(df)

df.to_csv('Wegmans_Extract.csv')
