import requests


API_key = "132c526a5209b2140d5d8ce975b57b4f"

def get_data(place, days=None, option=None):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_value = 8 * days
    filtered_data = filtered_data[0:nr_value]
    if option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if option == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo", days=3, option="Temperature"))
