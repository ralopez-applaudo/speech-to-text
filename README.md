# Build del contenedor
docker build -t deepspeech-service .

# Run
docker run -p 5000:5000 deepspeech-service

# Test with postman importing curl:
```
curl -X POST -F "file=@path/to/audio.wav" http://localhost:5000/transcribe
```