import openai
openai.api_key = "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"
audio_path = 'sample-0.mp3'
audio_file = open(audio_path,'rb')
response = openai.Audio.transcribe("whisper-1",audio_file)
print(response)