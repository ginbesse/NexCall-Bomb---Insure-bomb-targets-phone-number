class Provider:
    def __init__(self, data):
        self.name = data.get('name', 'Unknown')
        self.url = data.get('url', '')
        self.method = data.get('method', 'POST')
        self.payload_key = data.get('payload_key', 'phone')
        self.headers = data.get('headers', {"User-Agent": "Mozilla/5.0"})

def load_services(config):
    return [Provider(s) for s in config['services']]