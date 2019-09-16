FROM python:3.7-stretch

LABEL maintainer="Trinh Nguyen <dangtrinhnt@gmail.com>"

WORKDIR /keycloak_flask

COPY . /keycloak_flask

ENV FLASK_APP=keycloak_flask.user
ENV FLASK_DEBUG=1
ENV KEYCLOAK_FLASK_SETTINGS=local_settings.py

RUN pip install -r requirements.txt

ENTRYPOINT ["flask"]

CMD ["run", "--host=0.0.0.0"]
