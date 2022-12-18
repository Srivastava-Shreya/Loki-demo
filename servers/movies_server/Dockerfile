FROM python:3.9.1-alpine3.12

RUN pip install flask

WORKDIR /app
COPY server.py .
RUN chmod u+x server.py
RUN chown xfs server.py

USER xfs 
CMD [ "python", "./server.py"]