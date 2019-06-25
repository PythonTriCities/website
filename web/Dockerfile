FROM python:3.7.2-slim-stretch

COPY ./ /web
WORKDIR /web

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
