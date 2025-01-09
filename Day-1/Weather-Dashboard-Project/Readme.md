Weather Dashboard Documentation


1. Project Structure
```
weather-dashboard/
├── src/
│   ├── app.py
│   ├── weather_dashboard.py
│   ├── static/
│   │   ├── style.css
│   │   └── dashboard.js
│   └── templates/
│       └── index.html
├── .env
├── requirements.txt
└── README.md
```

[Project flow](https://viewer.diagrams.net/index.html?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Weather%20Dashboard%20Architecture%22%20id%3D%22iO119n79LV6DqgID-4B6%22%3E5Vhdb5swFP01kbaHVoADSR%2BTtF07NVonJqV9dOASaB0cGVNgv36XYAKUfG2iSaU9Jfdc25hzju8FemSyTL8JuvKn3AXWMzQ37ZHrnmHoWt%2FAnxzJCsS0zAJYiMBVgyrADn5DOVOhceBC1BgoOWcyWDVBh4chOLKBUSF40hzmcda86oouoAXYDmVtdBa40i%2FQoalV%2BB0EC7%2B8sq6pzJKWgxUQ%2BdTlSQ0iNz0yEZzL4t8ynQDLySt5Kebd7shuNiYglMdM8MML5yd%2FiNN0nkzny5epnVxcqFXeKIvVDf9YQTgD3DwITIwe79XuZVZSIngcupCvqvfIOPEDCfaKOnk2QRMg5sslU2kvYGzCGRfrucSlMPQcxNV1QUhId96QvqEJ%2FQV8CVJkOKScYClmlbX0kumkEmqD%2BTWRynlUeWOxWbqiD%2F8oBv%2BCTaPFZsXkNY38OafC7RkWEoH%2BJuPHTPo8xOSE0SjqlmgThm6%2FG6LJpyOatIgezWwEbExo49h5Bdkpm54HltORbc1Px%2BZViytwsQiqkAs06YKHlN1U6LhiMzdyNeaB85Xi8AWkzFRFp7HkTYaRLZE95fMvzTJ8Vsutg%2Bu0EWUq8hhPRmGA5TXAo1OsVew%2F3%2FR%2BTfAeeSwc2MNFX%2FUYKhYg94wzt2ssgOHG3pr76Fywfsv%2Bt1hAXnPvU%2FR%2B6HZqftCxmAw%2BppQY%2FXObX9dbZP2%2F7jePdL%2BubVf5NPY3t7TZ%2BY4W%2B%2BXu1%2FQBr%2FId28PtxLa%2FdtwXPKOrvvD%2BaGziQ0fD%2FKijYbV4bh%2BV0B3lT9kYOfkzTOC883kayKfa%2F%2Bem5Z9Kk2OqcnwenMjw5SvFIcMb26WrSWPuUeY0x2JwlkK2W%2BCdmtaKn2aQRvm7tIwDFXAdPYIIkDQQp3GJcaRLyDmr4vCc8leSP9cyB%2BUfXg2a8mva4BPqT47Uv39O%2FcsvJrVyHUfrV8%2F7EJny8pa2u%2Fdp%2F%2F6GGUnBX6GWGRpzYlkddUWz2RVN7eMeGDGsPsesc7WPWuTmDw%3D%3D%3C%2Fdiagram%3E%3Cdiagram%20name%3D%22Page-2%22%20id%3D%22YR33m78PuCH7z2CU4jjq%22%3E7Zpdc6M2FIZ%2FDTPtRRmBEOBLx0l2t22m6dI27aViZMMEI4%2BQ13Z%2FfY9Awnw4H97FqbOxJ5OxXoF0pPOcgyRs4cli80HQZXLDY5ZZLoo3Fr60XJeELvxXwrYSXEIqYS7SuJKcnRCl%2FzItIq2u0pgVrQsl55lMl21xyvOcTWVLo0LwdfuyGc%2FavS7pnPWEaEqzvnqXxjKp1JCgnf6RpfPE9OwgXbOg5mItFAmN%2Bboh4SvL9S0Xb6iFLyylPfeHJ4Jz%2BRU3thtZbCYsU14yHqgsvB6%2B4Xr2BMvlkfuS97%2FPLq6imFz9NU5%2BKYLs8%2Bebn7QBX2i20g79bcnyOwbOYQIqxreftHfk1rhc8FUeM9WqA6atk1SyaEmnqnYNjIOWyEWmq2dplk14xkV5L45DhAKsdJ7Lhj4rP6AXUvAH1qgZE4Q8VM5BaSkTkm0enT3n68B5aho%2FML5gUmyhbPo1yOqYDXVxvQuA%2BpKkAb%2BvNapjbl63PIjHoQ3t9Ndhx%2B2xs%2BPmkhbJPacirgxxlANvtzLhOVROMloUg2JFXYRccghW%2FjWCz0lhhc9YKaxwD6vxXQRCBBXoYjV9YHJQdhAKaUnCi9lBiAQnxg45s6PY8XrsXEOueVDgUAAnjwclxwduSkJeTA4GbiaTkyKnm3Vcs0B7Z%2BiQPU%2Bze2v%2Fk%2ByHj3%2Fc%2FAoG%2Fgx56XoSRT9%2BG1anC0Ndfmcw%2BD0Yeh6GZDJW%2BycoTdV6Jp22nco2qfy78f0f%2BI5stUYBl4qtqkK66nLTLGx14bFk83hSmWV8Pc5T2FmlsM5qssXi3i6uQxaMja%2FElD2%2FV5BUzJl8bl14NFIbJJpNZhNEowmWwTR8aY%2F6O6HT7P2bNIKDI13Mec72s4iaLDbh80iTPhhCVbplIoWJYsJcX5NrYycwgia73NaVwo7nsrRtlrpNfguzR2PsxfAMZ0HXmluewljrxOwFI9sLAuQT4mHieE4rTTvIsxEs%2BrATOo7njYjbNrkKbd3kAMgfYvjItx2iTBuhMIBhdAwnNgzJJz4ehQSsJ23Dq1xzHMN13NZuf3NZoH92870%2FpN7MQ%2BX1wstDnYAa2eRkgr%2B7K91j3TnCn4jw%2FgnbwRE%2BTIDWCwgb%2BUEjVzg2IvjJBLFvGTHgmhSf08K%2BwMPm%2FMcE3gidTFLAo7Zt9YHDa6SEtm0QOXTb6Hmp%2BiyO56nnZiboeE2XjzcB0HY1B%2BekWyfd%2Fvnz%2F5R0z6uiFxt9aIo5ofTnuR3b3m%2F668yMOXw8p7%2FXTH%2F9c%2FA%2Fi%2FKV7qccVnAzdYY95DuUwPdRSA95h%2BJh95IEp3Vsjtvkeqb8ho%2FNy7sP%2BDmNAX%2F3Kyd89R8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E#%7B%22pageId%22%3A%22iO119n79LV6DqgID-4B6%22%7D)

## 2. Setup Instructions

# Weather Dashboard Project

Real-time weather monitoring system with AWS S3 integration and web dashboard.

## Prerequisites
- Python 3.8+
- AWS CLI configured
- OpenWeather API key

## Installation
```bash
git clone <repository-url>
cd weather-dashboard
pip install -r requirements.txt
```
Environment Setup

create `.env` file :
```
OPENWEATHER_API=your_api_key
AWS_BUCKET_NAME=your_bucket_name
```

Running an application `python src/app.py`

Access at `http://localhost:5000`


#### 3. Dependencies
```python
flask==2.0.1
boto3==1.26.137
python-dotenv==1.0.0
requests==2.31.0
```
## 4. Features
Real-time weather monitoring
AWS S3 data storage
Web dashboard with charts
Multi-city support
Background data collection


#### 6. Architecture
```markdown
# System Architecture

## Components
1. Weather Data Collector (weather_dashboard.py)
   - Fetches data from OpenWeather API
   - Stores data in AWS S3
   
2. Web Dashboard (app.py)
   - Flask web server
   - Real-time updates
   - Data visualization

## Data Flow
1. Background thread fetches weather data
2. Data stored in S3 bucket
3. Frontend polls API endpoint
4. Chart.js visualizes data


#### 8. Deployment
```markdown
# Deployment Guide

## AWS Setup
1. Configure AWS CLI
2. Create S3 bucket
3. Set appropriate permissions

## Production Deployment
```bash
# Set environment variables
export FLASK_ENV=production
export FLASK_APP=src/app.py


#### 9. Maintenance
```markdown
# Maintenance Guide

## Log Monitoring
Check AWS CloudWatch for S3 operations

## Data Cleanup
Implement data retention policy:

```python
def cleanup_old_data():
    # Delete data older than 30 days
    pass
```


[openweathermap api website](https://openweathermap.org/api)


![alt text](Images/image-5.png)

![alt text](Images/image-6.png)

![alt text](Images/image-7.png)

![alt text](Images/image-2.png)

![alt text](Images/image.png)

![alt text](Images/image-1.png)

![alt text](Images/image-3.png)

![alt text](Images/image-4.png)
