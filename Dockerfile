FROM python:2.7
ADD . /DockerFlaskProject
WORKDIR /DockerFlaskProject
RUN pip install -r requirements.txt
