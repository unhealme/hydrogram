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

from collections.abc import AsyncIterator
from datetime import datetime

from hydrogram import Client, types, utils

async def get_chunk(
    *,
    client: Client,
    chat_id: int | str,
    limit: int = 0,
    offset: int = 0,
    from_message_id: int = 0,
    from_date: datetime = utils.zero_datetime(),
) -> list[types.Message]: ...

class GetChatHistory:
    async def get_chat_history(
        self,
        chat_id: int | str,
        limit: int = 0,
        offset: int = 0,
        offset_id: int = 0,
        offset_date: datetime = utils.zero_datetime(),
    ) -> AsyncIterator[types.Message]: ...
