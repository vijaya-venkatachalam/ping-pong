# Test web-app to use with Pluralsight courses and Docker Deep Dive book
FROM python:3.12-slim

COPY ponger.py ./
COPY responder ./responder

EXPOSE 8001
CMD ["python", "-u", "./ponger.py"]
