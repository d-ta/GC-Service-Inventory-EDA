import numpy as np
import pandas as pd
#import requests

#url
url = 'https://open.canada.ca/data/dataset/3ac0d080-6149-499a-8b06-7ce5f00ec56c/resource/3acf79c0-a5f5-4d9a-a30d-fb5ceba4b60a/download/service_inventory.csv'

#SSL certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#might also work: requests.get(url)

#Read csv file
df = pd.read_csv(url)

#Short description of the file
df.describe()
