from mpd import MPDClient

client = MPDClient()
client.connect('localhost', 6600)
print(client.outputs())