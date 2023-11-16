import pandas as pd
import numpy as np

df = pd.read_excel("your_file_name.xlsx")

df = df.iloc[:5000]

# pip install openpyxl
df.to_excel(r'result_file_name.xlsx', index=False, engine='openpyxl')