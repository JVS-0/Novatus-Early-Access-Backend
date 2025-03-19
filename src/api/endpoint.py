from fastapi import APIRouter

from src.api.routes.api_health import router as api_health_router
from src.api.routes.early_access import router as early_access_router

router = APIRouter()

router.include_router(router=api_health_router)
router.include_router(router=early_access_router)
