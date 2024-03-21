# show dbs
import pymongo

client = pymongo.MongoClient()

# List all the databases
dbs = client.list_database_names()

# Print the list
print(dbs)

# Disconnect from the MongoDB server
client.close()
