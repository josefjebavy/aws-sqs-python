# aws-sqs-python
Python example using AWS SQS 





### manual build ###
docker build -t aws-sqs-example-app .

### manual run with mount local source ###

docker run -it --rm -v $PWD:/usr/src/app --name aws-sqs-example-app-run aws-sqs-example-app /bin/bash 

### run ###
docker-compose up
