import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

# load environmental variable
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API')
        self.AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
        self.s3_client = boto3.client('s3')
    
        if not self.api_key:
            raise ValueError("Missing required environment variables")
        
                # Initialize AWS client with credentials
        self.s3_client = boto3.client(
            's3', region_name='ap-south-1')
    def bucket_exists(self):
        try:
            self.s3_client.head_bucket(Bucket=self.AWS_BUCKET_NAME)
            return True
        except:
            return False   
    def create_bucket(self):
        if self.bucket_exists():
            print(f"Using existing bucket: {self.AWS_BUCKET_NAME}")
            return
        # create s3 bucket if it doesn't exist
        try:
            self.s3_client.create_bucket(Bucket=self.AWS_BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
            print(f"Created Bucket: {self.AWS_BUCKET_NAME} with configuration: {{'LocationConstraint': 'ap-south-1'}}")
        except self.s3_client.exceptions.BucketAlreadyExists:
            print(f"Bucket already exists: {self.AWS_BUCKET_NAME}")
        except Exception as e:
            print(f"Error creating bucket: {e}")
            raise
    
    def fetch_weather(self, city):
        """Fetch weather data from OpenWeather API"""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error fetching weather data: {e}")
            return None
        
    def save_to_s3(self, data, city):
        """Save weather data to S3 bucket"""
        if not data:
            return False 
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file_name = f"weather_data/{city}-{timestamp}.json"
        
        try:
            self.s3_client.put_object(Bucket=self.AWS_BUCKET_NAME, Key=file_name, Body=json.dumps(data), ContentType='application/json')
            print(f"Saved weather data to: {file_name}")
        except Exception as e:
            print(f"Error saving data to S3: {e}")
            return False 
        
    def main(self):
        try:
            dashboard = WeatherDashboard()
            # create s3 bucket
            dashboard.create_bucket()

            # list of cities to track
            cities = ['Pune', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']

            for city in cities:
                print(f"\nProcessing weather data for {city}")
                weather_data = dashboard.fetch_weather(city)
                if weather_data:
                    dashboard.save_to_s3(weather_data, city)
                    print(f"successfully processed {city}")
                else:
                    print(f"Failed to process {city}")
                    
        except Exception as e:
            print(f"Main execution failed: {e}")

if __name__ == "__main__":
    WeatherDashboard().main()