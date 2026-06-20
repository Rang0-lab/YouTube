# YouTube Bulk Uploader

A Python tool for uploading videos to YouTube **in bulk** through the [YouTube Data API v3](https://developers.google.com/youtube/v3). Drop a folder of videos in, set your metadata once, and the script uploads each one — handling OAuth 2.0 authentication and resumable uploads with automatic retry on transient errors.

Built to solve a real annoyance: titling, describing, and tagging every video by hand in the YouTube Studio UI is slow when you're publishing a batch.

---

## Features

- **Batch upload** — uploads every video found in a configured folder.
- **Shared metadata** — apply a title, description, tags, category, and privacy status from one place.
- **Resumable uploads** — large files upload in a resumable session so a dropped connection doesn't restart the transfer.
- **Automatic retries** — retries on retriable HTTP status codes (`500`, `502`, `503`, `504`) and transient network errors, up to a configurable maximum.

## Roadmap

- [ ] Graphical user interface
- [ ] Scheduled uploads with configurable intervals
- [ ] Auto-suggested trending tags based on category and title
- [ ] Thumbnail upload support
- [ ] Bulk delete / update videos on a channel
- [ ] Add videos to a target playlist

---

## Tech stack

- **Python 3**
- `google-api-python-client`, `google-auth-oauthlib`, `oauth2client` — YouTube Data API v3 + OAuth 2.0

---

## Setup

1. **Create a Google Cloud project** and enable the **YouTube Data API v3** in the [Google Cloud Console](https://console.cloud.google.com/).
2. **Create an OAuth 2.0 Client ID** (application type: *Desktop app*) and download it as **`client_secrets.json`** into the project root.
   > ⚠️ **Never commit `client_secrets.json` or `credentials.json`.** They contain secrets that grant access to your YouTube account. They are listed in [`.gitignore`](.gitignore) — keep it that way.
3. **Install dependencies:**
   ```bash
   pip install google-api-python-client google-auth-oauthlib oauth2client httplib2
   ```

## Usage

1. Put the videos you want to upload in a folder (default: `./videos`, or set the `VIDEO_DIR` environment variable).
2. Edit the metadata in [`videoDetails.py`](videoDetails.py):
   ```python
   class Video:
       title         = "My video title"
       description    = "My video description"
       category       = "22"          # 22 = People & Blogs
       keywords       = "tag1,tag2"   # comma-separated
       privacyStatus  = "private"     # public | private | unlisted
   ```
3. Run it:
   ```bash
   python youtubeUpload.py
   ```
   The first run opens a browser for you to authorize the app; the resulting token is cached locally in `credentials.json` for subsequent runs.

---

## Disclaimer

This project was built for **educational use** to explore the YouTube Data API. If you use it to publish content, you are responsible for complying with the [YouTube API Services Terms of Service](https://developers.google.com/youtube/terms/api-services-terms-of-service) and YouTube's policies on spam and bulk uploads.
