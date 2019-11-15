FROM python:3.7.5

RUN apt-get -y update

# Install necessary deps for SSL/Websocket
RUN apt-get install -y libssl-dev libpcre3 libpcre3-dev

# set working directory
WORKDIR /usr/src/flask_app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

# Add PYTHONPATH
ENV PYTHONPATH=/usr/src/flask_app

RUN chmod +x ./start.sh

EXPOSE 8080

CMD ["./start.sh"]