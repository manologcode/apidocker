import uvicorn
import docker
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=os.getenv('allow_origins'),
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = docker.from_env()

@app.get("/list")
def list():
  dockers = list_dockers()
  return dockers

@app.get("/toggle/{docker_name}")
def toggle(docker_name):
  container = get_container(docker_name)
  if container:
    if container.status == "running":
      container.stop()
      response = "exited"
    else:
      container.start()
      response = "running"
    # response =  container.status
  else:
    response = "error"
  return response

@app.get("/status/{docker_name}")
def status(docker_name):
  container = get_container(docker_name)
  return container.status if container else "error"

def get_container(docker_name):
  try:
    response = client.containers.get(docker_name)
  except:
    response= False
  return response

def list_dockers():
    response = []
    for container in client.containers.list(all=True):
        if container.ports == {}:
           port=""
        else:
          first_port=next(iter(container.ports.values()))[0]
          port = first_port['HostPort']
        data = {
            'name': container.name,
            'port_app': f':{port}/',
            'url_logo': f"images/{container.name}.png",
        }
        response.append(data)
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")