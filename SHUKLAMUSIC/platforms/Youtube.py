import httpx
from typing import Union

class YouTubeAPI: def init(self): self.api_url = "http://46.250.243.87:1470/youtube" self.api_key = "1a873582a7c83342f961cc0a177b2b26"

async def search_video(self, query: str):
    params = {
        "query": query,
        "video": False,
        "api_key": self.api_key,
    }
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.get(self.api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "title": data.get("title"),
                "url": data.get("url"),
                "duration": data.get("duration"),
                "thumbnail": data.get("thumbnail"),
                "video_id": data.get("url").split("v=")[-1],
            }
        else:
            return None

async def track(self, query: str):
    data = await self.search_video(query)
    if not data:
        return None, None
    return {
        "title": data["title"],
        "link": data["url"],
        "vidid": data["video_id"],
        "duration_min": data["duration"],
        "thumb": data["thumbnail"],
    }, data["video_id"]

async def title(self, query: str) -> Union[str, None]:
    data = await self.search_video(query)
    return data["title"] if data else None

async def duration(self, query: str) -> Union[str, None]:
    data = await self.search_video(query)
    return data["duration"] if data else None

async def thumbnail(self, query: str) -> Union[str, None]:
    data = await self.search_video(query)
    return data["thumbnail"] if data else None

async def video_url(self, query: str):
    data = await self.search_video(query)
    if not data:
        return 0, "Video not found"
    return 1, data["url"]

