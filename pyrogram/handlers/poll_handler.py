#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Any, Callable, Union

import pyrogram
from pyrogram.filters import Filter
from .handler import Handler

CallbackFunc: Callable = Callable[
    [
        "pyrogram.Client",
        Union[
            pyrogram.types.Poll,
            pyrogram.types.PollAnswer
        ]
    ],
    Any
]


class PollHandler(Handler):
    """The Poll handler class. Used to handle polls updates.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_poll` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new poll update arrives. It takes *(client, poll)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filter`):
            Pass one or more filters to allow only a subset of polls to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the poll handler.

        poll (:obj:`~pyrogram.types.Poll` | :obj:`~pyrogram.types.PollAnswer`):
            New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot.
            A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.

    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
