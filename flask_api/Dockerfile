FROM python:3.9
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask","run","--host","0.0.0.0"]