# Installation
## clone repo go to the directory:
```
git clone https://github.com/comradexlight/geo_data
cd geo_data
```
## setup virtualenvironment:
```
python -m venv .venv
```
## activate virtualenvironment:
- linux:
```
. .venv/bin/activate
```
- windows:
```
.venv\Scripts\activate
```
## install dependencies from requirements.txt
```
pip install -r requirements.txt
```
# Usage
## run main.py with uvicorn:
```
uvicorn main:app --reload
```
# Technology stack
+ python
+ fastapi
+ uvicorn
+ folium
+ rosreestr2coord

