from service import times_client

# Connect with times service
connection = times_client.connect()

items = connection.find('.*')
for item in items:
    print item

ts = connection.load('mix_sim2_SIS_100_cpu_profile_norm')
print ts

# Close times connection
times_client.close()