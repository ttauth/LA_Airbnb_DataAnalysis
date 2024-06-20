import gzip
import shutil
import os


gz_files = ['calendar.csv.gz', 'listings.csv.gz', 'reviews.csv.gz']


for gz_file in gz_files:

    csv_file = gz_file.replace('.gz', '')
    

    with gzip.open(gz_file, 'rb') as f_in:
        with open(csv_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    print(f'{gz_file} has been unzipped to {csv_file}')


unzipped_files = [file for file in os.listdir() if file.endswith('.csv')]
print('Unzipped files:', unzipped_files)
