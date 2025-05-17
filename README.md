
# aws-practice
some aws practice for interview purposes.
should have installed brew for installing act for testing purposes.


# Install kubectl or else we won't be able to work with the .yaml

brew install kubectl

# In order to apply changes ->
kubectl apply -k k8s/overlays/qa1
kubectl apply -k k8s/overlays/staging
kubectl apply -k k8s/overlays/prod

# set up minicube in your local environment

brew install minikube

minikube start



como aplicar cambios k8
# QA1
kubectl apply -k k8s/overlays/qa1

# Staging
kubectl apply -k k8s/overlays/staging

# Prod
kubectl apply -k k8s/overlays/prod



# user "act" to run github actions localy
might need to create the secrets again since I forgot to copy them localy

# you can run with the user and token, create your own token if you've cloned this, that's it.
act -s DOCKER_USERNAME=tu_usuario -s DOCKER_TOKEN=tu_token 

# or use the secret-file .secrets, don't have one yet, might come around this later
act --secret-file .secrets


# DOCKER
   sudo docker build -t muratsuky/auth:latest .  # to copy everything
   sudo docker push muratsuky/auth:latest   # to push it
   sudo docker login -u muratsuky
   sudo docker push muratsuky/auth:latest