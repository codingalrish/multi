from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# The 'host' matches the Service name or container name in your deployment
# These are usually passed as environment variables for flexibility
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", 6379)

redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    # Increment the counter in the Redis container
    count = redis.incr('hits')
    return f'<h1>AKS Multi-Container Demo</h1><p>This page has been viewed {count} times.</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
