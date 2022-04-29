from fastapi import FastAPI, File, UploadFile
from pydantic.fields import T
import uvicorn
import shutil
from main import main
from serial import serial_run

app = FastAPI()


@app.post("/post_image/", status_code=201)
async def root(file: UploadFile = File('image')):
    with open(r'files_upload/check.jpg',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    path = r'files_upload/check.jpg'
    ret = main(path)

    return {"results": ret}
    
@app.post("/post_image_serial/", status_code=201)
async def root(file: UploadFile = File('image')):
    with open(r'files_upload/check.jpg',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    path = r'files_upload/check.jpg'
    ret = serial_run(path)

    return {"results": ret}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')