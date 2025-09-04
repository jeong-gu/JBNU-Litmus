import django
import pickle

with open('/home/ubuntu/log.ksl', 'rb') as f:
    data = pickle.load(f)
print(data)
