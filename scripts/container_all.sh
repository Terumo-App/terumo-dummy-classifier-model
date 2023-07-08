image_name=terumo-model-hipercellularity-classifier
# image_name=terumo-model-noemal-classifier
# image_name=terumo-model-membranous-classifier
# image_name=terumo-model-sclerosis-classifier

REM Run Python files
call pipenv requirements > requirements.txt
call docker build -t %image_name% .
call docker tag %image_name% terumoapp/%image_name%:latest
call docker push terumoapp/%image_name%:latest



