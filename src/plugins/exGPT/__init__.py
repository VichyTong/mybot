import nonebot
from nonebot import on_regex, logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from . import exGPT_request

exGPT = on_regex(r"^x ", priority=2, block=True)


@exGPT.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = str(event.get_message()).replace("x ", "")
    uuid = str(event.get_user_id())
    mode = "web"
    response = exGPT_request.send_get_request(mode, msg, uuid)
    msg = MessageSegment.reply(event.message_id) + MessageSegment.text(response)
    await exGPT.finish(msg)
