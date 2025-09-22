import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(youtube_url, name):
    video_id_regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(video_id_regex, youtube_url)

    if match:
        video_id = match.group(1)
    else:
        print("ERROR: Could not find video ID")
        exit(1)

    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)

    text_list = [transcript[i].text for i in range(len(transcript))]
    transcript_text = '\n'.join(text_list)

    output = "./transcripts/" + name + ".txt"

    with open(output, "w", encoding='utf-8') as f:
        f.write(transcript_text)

    return transcript_text