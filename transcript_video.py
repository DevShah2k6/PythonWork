from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
def video_transcript():
    video_id = "Gfr50f6ZBvo"  # only the ID, not full URL

    try:
        # Fetch the transcript
        api = YouTubeTranscriptApi()
        transcript_list = api.fetch(video_id, languages=["en"])

        # Convert transcript to plain text
        transcript = " ".join(chunk.text for chunk in transcript_list)

        return transcript

    except TranscriptsDisabled:
        print("No captions available for this video.")
