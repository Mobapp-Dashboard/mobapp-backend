from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    anomaly_detection_models,
    gps_points,
    trajectory_metadata,
)

api_router = APIRouter()

api_router.include_router(
    trajectory_metadata.router,
    prefix="/trajectory_metadata",
    tags=["trajectory metadata"],
)

api_router.include_router(gps_points.router, prefix="/gps_points", tags=["gps points"])

api_router.include_router(
    anomaly_detection_models.router,
    prefix="/anomaly_detection_models",
    tags=["anomaly detection models"],
)
