### Whisper App

Whisper App is a Python tool that leverages the OpenAI Whisper ASR (Automatic Speech Recognition) system to transcribe audio files. This README provides instructions on setting up the tool and using it effectively.

#### Setup

1. Install the OpenAI Whisper Python package:
   ```
   pip install openai-whisper
   ```

   Note: This will install the GPU version of PyTorch with CUDA support.

2. Install NVIDIA cuDNN library:
   ```
   sudo apt install nvidia-cudnn
   ```

3. Install FFmpeg:
   ```
   sudo apt install ffmpeg
   ```

#### Usage

To transcribe audio files, use the `whisperApp.py` script with the following command:

```bash
python3 whisperApp.py -f <input_filename_or_directory> [options]
```

##### Arguments

- `-f`: Specify an audio file or a directory of audio files. Directories should be flat, not nested.

- `-o`: (Optional) Specify the output directory. If not specified, the output will be in the same directory as the input.

- `-t`: (Optional) Include timestamps along with transcription. Use this flag if you need timestamp information.

- `-m`: (Optional) Select the Whisper model to use. The default is the base model.

- `-l`: (Optional) Select the language for transcription. The default is English.

#### Examples

Transcribe a single audio file:

```bash
python3 whisperApp.py -f audio_file.wav
```

Transcribe all audio files in a directory without timestamps:

```bash
python3 whisperApp.py -f audio_directory -t
```

Transcribe using a specific Whisper model:

```bash
python3 whisperApp.py -f audio_file.wav -m large
```

#### Note

Make sure you have the necessary permissions to read the input files and write to the output directory.

For more information on the available Whisper models and languages, refer to the OpenAI Whisper documentation.

Happy transcription!


To know more about us, visit our website: https://www.cognimuse.com