import asyncio import os import re from typing import Union import httpx

from pyrogram.enums import MessageEntityType from pyrogram.types import Message from SHUKLAMUSIC.utils.formatters import time_to_seconds

class YouTubeAPI: def init(self): self.base = "https://www.youtube.com/watch?v=" self.regex = r"(?:youtube\.com|youtu\.be)" self.api_url = "http://46.250.243.87:1470/youtube" self.api_key = "1a873582a7c83342f961cc0a177b2b26"

async def exists(self, link: str, videoid: Union[bool, str] = None):
    if videoid:
        link = self.base + link
    return bool(re.search(self.regex, link))

async def url(self, message_1: Message) -> Union[str, None]:
    messages = [message_1]
    if message_1.reply_to_message:
        messages.append(message_1.reply_to_message)
    text = ""
    offset = None
    length = None
    for message in messages:
        if offset:
            break
        if message.entities:
            for entity in message.entities:
                if entity.type == MessageEntityType.URL:
                    text = message.text or message.caption
                    offset, length = entity.offset, entity.length
                    break
        elif message.caption_entities:
            for entity in message.caption_entities:
                if entity.type == MessageEntityType.TEXT_LINK:
                    return entity.url
    if offset in (None,):
        return None
    return text[offset : offset + length]

async def get_stream_info(self, query, streamtype):
    video = True if streamtype.lower() == "video" else False
    params = {"query": query, "video": video, "api_key": self.api_key}
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.get(self.api_url, params=params)
            response.raise_for_status()
            return response.json()
    except Exception:
        return {}

async def details(self, query: str, videoid: Union[bool, str] = None):
    result = await self.get_stream_info(query, "audio")
    if not result or "title" not in result:
        return None, None, None, None, None
    title = result["title"]
    duration_min = result["duration"]
    duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
    thumbnail = result["thumb"]
    vidid = result["id"]
    return title, duration_min, duration_sec, thumbnail, vidid

async def track(self, query: str, videoid: Union[bool, str] = None):
    result = await self.get_stream_info(query, "audio")
    if not result or "title" not in result:
        return {}, None
    track_details = {
        "title": result["title"],
        "link": result["link"],
        "vidid": result["id"],
        "duration_min": result["duration"],
        "thumb": result["thumb"],
    }
    return track_details, result["id"]

