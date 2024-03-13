import pandas as pd
df = pd.read_csv('en.openfoodfacts.org.products.csv', delimiter='\t')
df.head(100).to_csv('first10.csv')
# DtypeWarning: Columns (0,11,12,14,15,16,17,23,24,25,26,27,31,32,33,34,35,36,37,44,46,47,48,51,52,56,67,72) have mixed types. Specify dtype option on import or set low_memory=False.