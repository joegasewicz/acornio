import asyncio

from flask import Flask
from acornio import AcornIO


app = Flask(__name__)

@app.route("/")
async def home():
    return "<h1>Home...<h1>"



if __name__ == "__main__":
    server = AcornIO(application=app)
    asyncio.run(server.serve())
