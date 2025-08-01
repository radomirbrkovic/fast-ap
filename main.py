from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import os
from routers.admin.auth import router as admin_auth_router
from routers.admin.dashboard import router as admin_dashboard_router
from routers.admin.users import router as admin_users_router

app = FastAPI()

app.add_middleware(SessionMiddleware, os.getenv('ADMIN_SECRET_KEY', ''))
app.include_router(admin_auth_router)
app.include_router(admin_dashboard_router)
app.include_router(admin_users_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def welcome():
    return {"message": "Welcome to FastAp, Admin panel developed in FastAPI."}