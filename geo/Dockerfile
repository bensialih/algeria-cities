FROM python:3.9.19-bullseye

RUn apt update && apt install binutils libproj-dev gdal-bin -y

ADD ./geo /app
ADD ./json/algeria_cities.json /app
WORKDIR /app

RUN pip install -r requirements.txt


