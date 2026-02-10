from db import engine
import models
from fastapi import FastAPI 
from routeres import blog
from routeres import user
from routeres import aouthantication
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(aouthantication.router)






