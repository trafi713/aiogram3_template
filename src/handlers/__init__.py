from aiogram import Router

from .start import router as start


router = Router()

router.include_router(start)