import openai
import os
import argparse
import transcript_extractor


def main():
    parser = argparse.ArgumentParser(description='Summarize a YouTube video using AI')

    parser.add_argument('--link', '-l', help='Link of the YouTube video')
    parser.add_argument('--name', '-n', help='Name of the video(or your custom choice)')

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it by running: set OPENAI_API_KEY=your_api_key_here")
        exit(1)

    name = parser.parse_args().name
    url = parser.parse_args().link

    transcript = transcript_extractor.get_transcript(url, name)

    prompt = f"""
            I have the transcript of a YouTube video.\
            Please summarize it into the key points, keeping it clear while also keeping key aspects.
            Highlight the main ideas, any arguments or steps explained, and the overall conclusion.
            If possible, also provide a short bullet-point version for quick reference.
        
            Here’s the transcript:\
            {transcript}
            """


    client = openai.OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt}
            ]
        )

        summary = response.choices[0].message.content
        print(summary)

        output_path = "./summaries/" + name + ".txt"
        with open(output_path, "w", encoding='utf-8') as f:
            f.write(summary)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()