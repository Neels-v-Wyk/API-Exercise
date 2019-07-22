FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY titanic.csv ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .
RUN ls -la .

RUN python ./models.py
CMD [ "python", "app.py" ]
