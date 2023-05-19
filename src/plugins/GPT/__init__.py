import nonebot
from nonebot import on_regex, logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from . import GPT_request

GPT = on_regex(r"^z ", priority=2, block=True)


@GPT.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = str(event.get_message()).replace("x ", "")
    response = GPT_request.send_get_request(msg)
    msg = MessageSegment.reply(event.message_id) + MessageSegment.text(response)
    await GPT.finish(msg)
