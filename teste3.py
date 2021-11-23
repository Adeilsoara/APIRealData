import requests
import pdb
from google.transit import gtfs_realtime_pb2
def getPositions(req):
    #response = requests.get(req)
    print('piroca')
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(req.content)
    print(feed)

try:
    #pdb.set_trace()
    req = requests.get("https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/metro",
      headers={
        "Accept": "application/x-google-protobuf",
        "Authorization": "apikey G2j8KhTM3WJBztVuTCLlUsGzkPtE36hucASZ"
      }
      )

    print(req)
    getPositions(req)
except Exception as e:
    print(e)
