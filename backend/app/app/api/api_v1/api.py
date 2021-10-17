from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, dublin_meta, dublin_points, dublin_model
# , transformer

api_router = APIRouter()
#api_router.include_router(login.router, tags=["login"])
#api_router.include_router(users.router, prefix="/users", tags=["users"])
#api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
#api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(dublin_meta.router, prefix="/dublin_meta", tags=["dublin_meta"])
api_router.include_router(dublin_points.router, prefix="/dublin_points", tags=["dublin_points"])
api_router.include_router(dublin_model.router, prefix="/dublin_model", tags=["dublin_model"])
#api_router.include_router(transformer.router, prefix="/transformer", tags=["Models"])
