import sys
from pytube import YouTube

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python your_script.py <YouTube_URL>")
    sys.exit(1)

# Get the YouTube URL from the command-line argument
video_url = sys.argv[1]

try:
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get all streams with both video and audio, sorted by resolution in descending order
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    # Display available resolutions
    print("Available Resolutions:")
    for stream in streams:
        print(f"{stream.resolution} - {stream.mime_type}")

    # Prompt the user to select a resolution
    selected_resolution = input("Enter the desired resolution (e.g., '720p', '1080p', etc.): ")

    # Find the selected stream based on user input
    selected_stream = streams.filter(resolution=selected_resolution, mime_type='video/mp4').first()

    if selected_stream:
        # Set the output file path (change to your desired location)
        output_path = 'downloaded_content'

        # Download the video
        selected_stream.download(output_path=output_path)

        print(f"Video downloaded to {output_path}")
    else:
        print("Selected resolution not found.")

except Exception as e:
    print(f"An error occurred: {e}")
