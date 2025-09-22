# YouTube Video Summarizer

A Python application that extracts transcripts from YouTube videos and generates AI-powered summaries using OpenAI's GPT model.

## Features

- 🔗 Extract video transcripts from YouTube URLs
- 🤖 Generate intelligent summaries using OpenAI's GPT-4o-mini model
- 📁 Organize transcripts and summaries in separate folders
- 💻 Simple command-line interface
- 🎯 Focus on key points, arguments, and conclusions

## How It Works

1. **URL Processing**: Takes a YouTube video URL and extracts the video ID using regex pattern matching
2. **Transcript Extraction**: Uses the `youtube_transcript_api` library to fetch the video's transcript
3. **AI Summarization**: Sends the transcript to OpenAI's GPT-4o-mini model with a carefully crafted prompt
4. **File Organization**: Saves both the raw transcript and AI-generated summary in separate folders

## Prerequisites

- Python 3.6+
- OpenAI API key
- Internet connection

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install openai youtube-transcript-api
   ```

3. Set up your OpenAI API key as an environment variable:
   
   **Windows:**
   ```cmd
   set OPENAI_API_KEY=your_api_key_here
   ```
   
   **macOS/Linux:**
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the script with the following command-line arguments:

```bash
python summarizer.py --link "https://www.youtube.com/watch?v=VIDEO_ID" --name "video_name"
```

### Parameters

- `--link` or `-l`: The YouTube video URL
- `--name` or `-n`: A custom name for the video (used for file naming)

### Example

```bash
python summarizer.py --link "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --name "rick_roll"
```

This will:
1. Extract the transcript and save it as `transcripts/rick_roll.txt`
2. Generate a summary and save it as `summaries/rick_roll.txt`
3. Display the summary in the console

## Project Structure

```
ytVideoSummarizer/
├── summarizer.py          # Main script
├── transcript_extractor.py # Transcript extraction module
├── transcripts/           # Folder for raw transcripts
├── summaries/            # Folder for AI-generated summaries
└── README.md            # This file
```

## File Outputs

- **Transcripts**: Raw video transcripts saved in the `transcripts/` folder
- **Summaries**: AI-generated summaries saved in the `summaries/` folder
- Both files use UTF-8 encoding and are named according to your custom name parameter

## Dependencies

- `openai`: For AI-powered summarization
- `youtube-transcript-api`: For extracting YouTube video transcripts

## Error Handling

The application includes error handling for:
- Missing OpenAI API key
- Invalid YouTube URLs (cannot extract video ID)
- API errors during summarization
- File writing errors

## Notes

- The application uses OpenAI's `gpt-4o-mini` model for cost-effective summarization
- Transcripts are automatically formatted and cleaned before being sent to the AI
- The AI prompt is designed to extract key points, arguments, and conclusions
- Both bullet-point and paragraph summaries are generated for comprehensive coverage

## Troubleshooting

1. **"OPENAI_API_KEY environment variable is not set"**: Make sure you've set your OpenAI API key as an environment variable
2. **"ERROR: Could not find video ID"**: Ensure the YouTube URL is valid and contains a video ID
3. **API errors**: Check your OpenAI account balance and API key validity

## License

This project is open source and available under the MIT License.
