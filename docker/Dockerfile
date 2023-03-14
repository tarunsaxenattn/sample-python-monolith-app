FROM python:3.7.16
COPY . /opt/
RUN pip3 install flask healthcheck requests six python-bandsintown
EXPOSE 80
CMD ["python","/opt/app.py"]