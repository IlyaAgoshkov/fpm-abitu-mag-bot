from typing import Any, Awaitable, Callable, Dict

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message

from config.conf import ADMINISTRATORS


class AdminAuthorizationMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id in ADMINISTRATORS:
            await handler(event, data)
        else:
            await event.answer('Эта команда разрешена только для администраторов')
