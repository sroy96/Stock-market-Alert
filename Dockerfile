#Dockerfile
FROM python:3.8.5
MAINTAINER Saurav Roy
WORKDIR /app
COPY cache_server_up.sh .
COPY confidential.py .
COPY requirement.txt .
COPY /src .
COPY /models .
COPY /utils .
COPY /service .
COPY /interfaces .
RUN pip install -r requirement.txt
ADD src/main.py $PWD/market-notification/src/
ADD models/user_stock_relation.py $PWD/market-notification/models/

CMD ["python3 -m","src.main"]
