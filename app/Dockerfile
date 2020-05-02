## Base Python Image for App
FROM python:3.9-rc-buster

# Setting up Docker environment 
# Setting Work directory for RUN CMD commands
WORKDIR /code



# #Copy requirements file from current directory to file in 
# #containers code directory we have just created.
COPY requirements.txt requirements.txt

# #Run and install all required modules in container
RUN pip3 install -r requirements.txt

# #Copy current directory files to containers code directory
COPY . .

# RUN app.
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]