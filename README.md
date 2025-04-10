# Build del contenedor
docker build -t whisper-large-service .

# Run
docker run -p 5000:5000 whisper-large-service

# Test with postman importing curl:
```
curl -X POST -F "file=@path/to/audio.wav" http://localhost:5000/transcribe
```