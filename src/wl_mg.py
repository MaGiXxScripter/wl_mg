import json
import aiohttp

class WhitelistMaGixx:
    url = 'http://127.0.0.1:8000/'

    def __init__(self, api_key) -> None:
        self.api_key = api_key

    async def add_whitelist(self, id) -> json or None:
        async with aiohttp.ClientSession() as session:
            response = await session.get(f'{self.url}api/v1/add/whitelist/{self.api_key}/{self.id}')
            response = await response.json()

            if response.get('status') == 200:
                return response
            
            return False

    async def del_whitelist(self, id) -> json or None:
        async with aiohttp.ClientSession() as session:
            response = await session.get(f'{self.url}api/v1/del/whitelist/{self.api_key}/{self.id}')
            response = await response.json()

            if response.get('status') == 200:
                return response
            
            return False

    async def reset_hwid(self, id) -> json or None:
        async with aiohttp.ClientSession() as session:
            response = await session.get(f'{self.url}api/v1/whitelist/reset-hwid/{self.api_key}/{self.id}')
            response = await response.json()

            if response.get('status') == 200:
                return response
            
            return False

    async def reset_key(self, id) -> json or None:
        async with aiohttp.ClientSession() as session:
            response = await session.get(f'{self.url}api/v1/whitelist/reset-key/{self.api_key}/{self.id}')
            response = await response.json()

            if response.get('status') == 200:
                return response
            
            return False
