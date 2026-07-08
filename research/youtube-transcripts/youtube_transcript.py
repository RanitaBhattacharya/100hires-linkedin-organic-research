from youtube_transcript_api import YouTubeTranscriptApi

video_id = "VIDEO_ID"

transcript = YouTubeTranscriptApi.get_transcript(video_id)

for line in transcript:
    print(line["text"])