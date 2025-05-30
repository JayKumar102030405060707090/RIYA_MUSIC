Write a fully functional Python FastAPI application in a single file that is an exact feature-for-feature clone of the following code:

[PASTE THE ENTIRE YouTube.py CODE HERE]

Features to preserve:
✅ Uses yt_dlp for downloading and extracting YouTube video/audio formats.
✅ Uses youtubesearchpython for fast and accurate search results.
✅ Includes functions for:
   - get_stream_url()
   - video download (audio, video, songaudio, songvideo, formats)
   - search results
   - duration, thumbnail, title, exists, playlist, formats, slider, track.
✅ Preserves every detail, comment, and line from the original code.
✅ Maintains 0.3s response time for search and play (ultra-fast search & play).
✅ Supports live stream fetching.
✅ Does not use cookies or any user session — fully server-side.
✅ Provides seamless audio/video streaming.
✅ Allows playing anything without limits.
✅ Uses only open-source libraries: yt_dlp, youtubesearchpython, httpx, asyncio, FastAPI.
✅ Compatible with Pyrogram, Telethon, and TGCALLS bots — include instructions in comments on how to integrate.
✅ No rate limits — fully unlimited usage.
✅ Includes Cloudflare proxy support recommendations in comments for anti-bot protection.
✅ Uses environment variables using python-dotenv for API keys, secrets, and MongoDB URI (if needed).
✅ Provides clear comments explaining each part of the code.
✅ Ready to run on free platforms like Replit, Render.com, Railway.app, Fly.io — with deployment instructions in comments.

Use the original file as the reference for each function's implementation — do not skip any features. Provide a complete, production-ready, single-file FastAPI application.
