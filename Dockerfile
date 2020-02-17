FROM grpc/python:1.4

RUN mkdir -p /usr/src/auth_service
WORKDIR /usr/src/auth_service

COPY requirements.txt /usr/src/auth_service/
COPY auth_service_pb2.py /usr/src/auth_service/
COPY auth_service_pb2_grpc.py /usr/src/auth_service/
COPY authorization_server.py /usr/src/auth_service/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/usr/src/auth_service

ONBUILD COPY . /usr/src/auth_service
WORKDIR /usr/src
CMD pwd; ls; python auth_service/authorization_server.py
