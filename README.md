# Build del contenedor
docker build -t deepspeech-service .

# Run
docker run -p 5000:5000 deepspeech-service



