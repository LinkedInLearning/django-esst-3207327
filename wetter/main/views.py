from django.shortcuts import render
import json
import urllib.request
  
  
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API
  
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').read() #API-Key muss erstellt werden
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
  
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "lat": str(list_of_data['coord']['lat']),
            "lon": str(list_of_data['coord']['lon']),
            "temp": str(round(list_of_data['main']['temp'] - 273.15,2)) + ' C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']) + "%",
        }
        print(data)
    else:
        data ={}
    return render(request, "main/index.html", data)