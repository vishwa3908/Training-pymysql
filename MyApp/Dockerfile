FROM python:alpine
EXPOSE 5000
WORKDIR /MyApp
COPY / /MyApp
RUN pip install -r requirement.txt
CMD python src/app.py