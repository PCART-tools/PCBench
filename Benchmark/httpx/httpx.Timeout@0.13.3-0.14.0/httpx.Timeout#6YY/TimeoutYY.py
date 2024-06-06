import httpx
timeout = httpx.Timeout(connect_timeout=5.0, read_timeout=5.0)
