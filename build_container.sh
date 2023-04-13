pipenv requirements > requirements.txt
docker build -t terumo-model-dummy-classifier .

docker tag terumo-model-dummy-classifier terumoapp/terumo-model-dummy-classifier:latest