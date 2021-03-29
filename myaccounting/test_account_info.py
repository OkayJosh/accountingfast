# Importing libraries 
from binance.client import Client
import configparser

# Loading keys from config file
config = configparser.ConfigParser()
config.read_file(open('secret.cfg'))
test_api_key = config.get('BINANCE', 'TEST_API_KEY')
test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')

client = Client(test_api_key, test_secret_key)

client.API_URL = 'https://testnet.binance.vision/api'  # To change endpoint URL for test account  

#store account info into the AccountInfo Model
