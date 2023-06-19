FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN set -eux && \
    chmod +x docker-cmd.sh

CMD ["./docker-cmd.sh"]