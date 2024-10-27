FROM python
WORKDIR /docker/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5010
CMD [ "python" , "app.py" ]