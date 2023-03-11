import requests

#Load Txt Files
#script = open()

for i in range(5):
    aws_polly = requests.post()

    raw_audio = aws_polly.json()["Content"]

    audio_file = open(f"slide{int(i/10)}{i%10}.mp3", "x")
    audio_file.write("")
    audio_file.close()