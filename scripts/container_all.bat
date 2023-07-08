set image_name=terumo-model-hipercellularity-classifier
@REM set image_name=terumo-model-noemal-classifier
@REM set image_name=terumo-model-membranous-classifier
@REM set image_name=terumo-model-sclerosis-classifier

REM Run Python files
call pipenv requirements > requirements.txt
call docker build -t %image_name% .
@REM call docker tag %image_name% terumoapp/%image_name%:latest
@REM call docker push terumoapp/%image_name%:latest



