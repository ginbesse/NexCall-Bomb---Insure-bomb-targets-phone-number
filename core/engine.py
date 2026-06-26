import aiohttp
import asyncio

class RequestEngine:
    async def send_request(self, session, provider, target):
        data = {provider.payload_key: target}
        try:
            async with session.request(
                method=provider.method, 
                url=provider.url, 
                json=data, 
                headers=provider.headers,
                timeout=5
            ) as resp:
                return f"[{provider.name}] Durum: {resp.status}"
        except Exception as e:
            return f"[{provider.name}] Hata: {str(e)}"

    async def run(self, providers, target):
        async with aiohttp.ClientSession() as session:
            tasks = [self.send_request(session, p, target) for p in providers]
            return await asyncio.gather(*tasks)