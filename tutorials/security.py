"""セキュリティ入門
ref https://fastapi.tiangolo.com/ja/tutorial/security/
"""

from fastapi import APIRouter

from .security_ import first_steps, get_current_user, simple_oauth2, oauth2_jwt

router = APIRouter(
    prefix="/security",
    tags=["セキュリティ入門"],
)


router.include_router(first_steps.router)
router.include_router(get_current_user.router)
router.include_router(simple_oauth2.router)
router.include_router(oauth2_jwt.router)
