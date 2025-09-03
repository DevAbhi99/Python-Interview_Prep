from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZIPMiddleware
import time

api=FastAPI()

#Logging request middleware
@api.middleware('http')
async def logRequest(request:Request, call_next):
    start_time=time.time()

    response=await call_next(request)

    process_time=time.time()-start_time

    print(f'{request.url}, {request.method} processed in {process_time:.2f}s')

    return response


#CORS - Cross origin Resource Sharing
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Gzip - Compresses the response

api.add_middleware(
    GZIPMiddleware, minimum_size=1000
)


#Error handling using try and response

