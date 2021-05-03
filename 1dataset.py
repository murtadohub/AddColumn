import pandas as pd 
dataset = pd.read_csv('data.csv')
print('ukuran dataset: %d baris dan %id kolom\n' % dataset.shape)
print('lima data teratas:')
print(dataset.head())