from service import times_client

# Connect with times service
connection = times_client.connect()

items = connection.find('.*')
for item in items:
    print item

# Close times connection
times_client.close()