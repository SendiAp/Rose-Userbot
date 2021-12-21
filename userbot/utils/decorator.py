import inspect
import re
from pathlib import Path

from telethon import events

from userbot import (
    BL_CHAT,
    CMD_HANDLER,
    CMD_LIST,
    SUDO_HANDLER,
    bot,
)


def rose_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global rose_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            rose_reg = sudo_reg = re.compile(pattern)
        else:
            rose_ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            re.compile(rose_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = rose_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (rose_ +
                     pattern).replace(
                        "$",
                        "").replace(
                        "\\",
                        "").replace(
                        "^",
                        ""))
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})


def rose_handler(
    **args,
):
    def decorator(func):
        bot.add_event_handler(func, events.NewMessage(**args, incoming=True))
        return func

    return decorator
