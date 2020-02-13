FROM python:3



WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get upgrade -y



COPY hello_app.py .
RUN mkdir -p /usr/src/app/static
COPY static/hello.html .
RUN cp hello.html static/




COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



CMD  ["python", "./hello_app.py"] 
 






