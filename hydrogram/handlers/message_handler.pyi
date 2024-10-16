#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2023 Dan <https://github.com/delivrance>
#  Copyright (C) 2023-present Hydrogram <https://hydrogram.org>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from collections.abc import Awaitable, Callable
from typing import Any

from hydrogram import Client
from hydrogram.types import Listener, Message

from .handler import Handler

type Callback = Callable[[Client, Message], Awaitable[Any]]

class MessageHandler(Handler):
    def __init__(self, callback: Callback, filters=None):
        self.original_callback = callback
        super().__init__(self.resolve_future_or_callback, filters)

    @staticmethod
    async def check_if_has_matching_listener(
        client: Client,
        message: Message,
    ) -> tuple[bool, Listener | None]: ...
    async def check(self, client: Client, message: Message) -> bool: ...
    async def resolve_future_or_callback(
        self,
        client: Client,
        message: Message,
        *args: Any,
    ) -> None: ...
