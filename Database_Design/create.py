import pymongo

# Connect to MongoDB server (default host and port)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a new database called "user"
db = myclient['user']

# Print a confirmation message
print("Database 'user' created successfully.")

# Disconnect from the MongoDB server
myclient.close()
