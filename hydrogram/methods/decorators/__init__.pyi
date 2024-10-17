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

from collections.abc import Awaitable, Callable, Iterable

from hydrogram import Client
from hydrogram.filters import Filter
from hydrogram.raw.types import Channel
from hydrogram.types import (
    CallbackQuery,
    Chat,
    ChatJoinRequest,
    ChatMemberUpdated,
    ChosenInlineResult,
    InlineQuery,
    Message,
    Poll,
    Update,
    User,
)

type Callback[**PT, RT] = Callable[PT, Awaitable[RT]]
type Decorate[T] = Callable[[T], T]

class OnCallbackQuery:
    def on_callback_query[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, CallbackQuery], T]]: ...

class OnChatJoinRequest:
    def on_chat_join_request[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, ChatJoinRequest], T]]: ...

class OnChatMemberUpdated:
    def on_chat_member_updated[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, ChatMemberUpdated], T]]: ...

class OnInlineQuery:
    def on_inline_query[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, InlineQuery], T]]: ...

class OnChosenInlineResult:
    def on_chosen_inline_result[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, ChosenInlineResult], T]]: ...

class OnMessage:
    def on_message[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, Message], T]]: ...

class OnDeletedMessages:
    def on_deleted_messages[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, Message], T]]: ...

class OnEditedMessage:
    def on_edited_message[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, Message], T]]: ...

class OnPoll:
    def on_poll[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, Poll], T]]: ...

class OnUserStatus:
    def on_user_status[T](
        self,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Decorate[Callback[[Client, User], T]]: ...

class OnRawUpdate:
    def on_raw_update[T](
        self, group: int = 0
    ) -> Decorate[Callback[[Client, Update, dict[int, User], dict[int, Chat | Channel]], T]]: ...

class OnError:
    def on_error[T](
        self,
        errors: type[Exception] | Iterable[type[Exception]] | None = None,
    ) -> Decorate[Callback[[Client, Exception, Update], T]]: ...

class OnDisconnect:
    def on_disconnect[T](self) -> Decorate[Callback[[Client], T]]: ...

class Decorators(  # noqa: N818 false-positive
    OnCallbackQuery,
    OnChatJoinRequest,
    OnChatMemberUpdated,
    OnChosenInlineResult,
    OnDeletedMessages,
    OnDisconnect,
    OnEditedMessage,
    OnError,
    OnInlineQuery,
    OnMessage,
    OnPoll,
    OnRawUpdate,
    OnUserStatus,
): ...
