import datetime
import simplejson
import urllib.request

save_fn = 'path/drivetimes.txt'
origin = '1600+Pennsylvania+Ave+NW+Washington+DC+20006'
destination = '1451+Broadway+New+York+NY+10036'
APIkey = 'AIzaSyDDzhn_iQznGgyd5LyyTjkBe-O3lVxpkV8'
traffic_model = 'best_guess'

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&departure_time=now&traffic_model={2}&key={3}".format(origin,destination,traffic_model,APIkey)

result= simplejson.load(urllib.request.urlopen(url))

driving_time = result['rows'][0]['elements'][0]['duration_in_traffic']['value']

f = open(save_fn,'a')
    
dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
f.write(dt+","+str(driving_time)+"\n")

