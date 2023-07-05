from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api_key = '3467d304d26fc16fa5cc707d10f3dbc0'  # Replace with your OpenWeatherMap API key

        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(weather_url)
            data = response.json()

            if data['cod'] == 200:
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                icon = data['weather'][0]['icon']

                weather_data = {
                    'city': city,
                    'temperature': temperature,
                    'description': description,
                    'icon': icon
                }

                return render_template('weather.html', weather=weather_data)
            else:
                error_message = f'Error occurred: {data["message"]}'
                return render_template('weather.html', error=error_message)
        except Exception as e:
            error_message = f'Error occurred: {str(e)}'
            return render_template('weather.html', error=error_message)
    else:
        return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)

