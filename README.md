# ReroCore Python gRPC Examples
This repo contains examples for connecting to the [ReroCore Server](https://github.com/reverbrobotics/rero_core_dist) directly using [gRPC](https://grpc.io/). 

## Dependencies
The code in this repo requires gRPC which can be installed using pip as follows:
```
pip install grpcio
```

The audio playback example also requires PyAudio, which can be installed using pip:
```
pip install PyAudio
```

## Usage

A ReroCore server must be running in order to use these example python clients. Binaries for the server can be downloaded [here](https://github.com/reverbrobotics/rero_core_dist).

The following example files are currently in the repo.

### Raw Audio Playback
An example that plays audio frames over the system speaker using PyAudio. raw_audio_playback_example.py.

### Speech Recognition
An example demonstrating usage of speech recognition. speech_recognition_example.py.

### NLU
An example demonstrating usage of speech recognition and NLU together. nlu_example.py.

### Text to Speech
An example demonstrating Text to Speech. text_to_speech_example.py. 

## Licence
This code is licenced under the [MIT License](https://github.com/reverbrobotics/rero_core_python_example/blob/master/LICENSE). 
