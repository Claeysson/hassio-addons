ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3
WORKDIR /

# Copy data for add-on
COPY script.py /

RUN pip3 install requests

CMD ["python3", "-u", "./script.py" ]
