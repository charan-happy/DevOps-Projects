from flask import Flask, render_template, jsonify
from weather_dashboard import WeatherDashboard
import threading
import time
from datetime import datetime

app = Flask(__name__)
weather_dashboard = WeatherDashboard()
CITIES = ['Pune', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']

def background_task():
    while True:
        try:
            for city in CITIES:
                weather_data = weather_dashboard.fetch_weather(city)
                if weather_data:
                    weather_dashboard.save_to_s3(weather_data, city)
                    print(f"Data saved to S3 for {city}")
            # Wait for 5 minutes before next update
            time.sleep(300)
        except Exception as e:
            print(f"Error in background task: {e}")
            time.sleep(60)

@app.route('/')
def index():
    return render_template('index.html', cities=CITIES)

@app.route('/api/weather')
def get_weather():
    weather_data = {}
    for city in CITIES:
        data = weather_dashboard.fetch_weather(city)
        if data:
            weather_data[city] = {
                'temp': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'condition': data['weather'][0]['main'],
                'wind': data['wind']['speed']
            }
    return jsonify(weather_data)

if __name__ == '__main__':
    # Start the background task for S3 uploads
    weather_dashboard.create_bucket()
    background_thread = threading.Thread(target=background_task, daemon=True)
    background_thread.start()
    
    # Run Flask app
    app.run(debug=True, use_reloader=False)