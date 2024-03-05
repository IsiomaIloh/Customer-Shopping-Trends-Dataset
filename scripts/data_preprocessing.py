from data_loader import load_data

file_path = ('/Users/isiomailoh/Desktop/datasets/shopping_trends_project/data/shopping_trends_dataset.csv')
df = load_data(file_path)

print(df.isnull().sum())

print(df.duplicated().sum())