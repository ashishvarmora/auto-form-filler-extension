import pandas as pd
import os
import json

folder = "client_data"
output = {}

for file in os.listdir(folder):
    if file.endswith(".xlsx"):
        df = pd.read_excel(os.path.join(folder, file), header=None, index_col=0)
        data = df[1].to_dict()
        client_name = data.get("Name", file.replace(".xlsx", ""))
        output[client_name] = data

with open("clients.json", "w") as f:
    json.dump(output, f, indent=2)
