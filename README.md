# PYYTDownloader

**PYYTDownloader** is a simple command-line tool for downloading YouTube videos. It utilizes the Python library `pytube` to fetch and download videos from YouTube. This README will guide you through the installation, usage, and dependencies of the tool.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

## Dependencies

Before using **PYYTDownloader**, ensure that you have the following dependencies installed:

1. **Python**: The tool relies on Python to run. Make sure Python is installed on your system.

2. **pytube Library**: This tool uses the `pytube` library to interact with YouTube. If you don't have it installed, the tool will attempt to install it for you during the first run.

## Installation

1. Clone this Git repository to your local machine:

   ```bash
   git clone https://github.com/FTCentral/PYYTDownloader.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PYYTDownloader
   ```

3. You may need to make the Launch.bat file executable:

   ```bash
   chmod +x Launch.bat
   ```

That's it! You have successfully installed **PYYTDownloader**.

## Usage

To download a YouTube video using **PYYTDownloader**, follow these steps:

1. Open a command prompt or terminal window.

2. Navigate to the project directory if you haven't already:

   ```bash
   cd path/to/PYYTDownloader
   ```

3. Run the tool using the Launch.bat file:

   ```bash
   ./Launch.bat
   ```

   This will execute the batch file, which in turn launches the Python script.

4. Follow the on-screen instructions:
   - You will be prompted to enter the YouTube URL of the video you want to download.
   - The tool will display available video resolutions.
   - Enter the desired resolution (e.g., '720p', '1080p', etc.).
   - The video will be downloaded and saved in a folder named 'downloaded_content' within the project directory.

## Disclaimer

Please note that downloading copyrighted material without the permission of the content owner may infringe upon their rights and could lead to legal consequences. Ensure you have the necessary rights or permissions to download the videos you intend to use with this tool. The tool's author takes no responsibility for any misuse or legal issues arising from its use.