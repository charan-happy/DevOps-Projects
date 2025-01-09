Here are the some of the challenges that i faced while executing the project and how i overcome them

```
$ python3 src/weather_dashboard.py 

Traceback (most recent call last): File "C:\Users\Documents\cozecloud crew\DevOps-Projects\Day-1\Weather-Dashboard-Project\src\weather_dashboard.py", line 89, in <module> WeatherDashboard().main() ^^^^^^^^^^^^^^^^^^ File "C:\Users\Documents\cozecloud crew\DevOps-Projects\Day-1\Weather-Dashboard-Project\src\weather_dashboard.py", line 18, in init raise ValueError("Missing required environment variables") ValueError: Missing required environment variables
```
solution :

```
Environmental variable mismatch with .env file and weather_dashboard.py file
```
```
python3 src/weather_dashboard.py 

Error creating bucket: An error occurred (BucketAlreadyOwnedByYou) when calling the CreateBucket operation: Your previous request to create the named bucket succeeded and you already own it. Main execution failed: An error occurred (BucketAlreadyOwnedByYou) when calling the CreateBucket operation: Your previous request to create the named bucket succeeded and you already own it.
```
solution :

```
Add bucket existence check before creation
Update error handling for BucketAlreadyOwnedByYou error
Fix main() method to avoid creating new instance

def bucket_exists(self):
        try:
            self.s3_client.head_bucket(Bucket=self.AWS_BUCKET_NAME)
            return True
        except:
            return False
```

```
git add Day-1/* 

error: 'Day-1/Weather-Dashboard-Project/' does not have a commit checked out fatal: adding files failed
```
solution :

# Remove any submodule reference
rm -rf "Day-1/Weather-Dashboard-Project/.git"

# Then add files again
git add "Day-1/Weather-Dashboard-Project/"

- This error typically occurs when there's a nested .git directory or submodule reference. The steps above should resolve the issue