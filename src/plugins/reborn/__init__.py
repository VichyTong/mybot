import json
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from . import reborn

make_reborn = on_command("remake", priority=5, block=True)
dataset = {}
cnt = {}


@make_reborn.handle()
async def _(bot: Bot, event: MessageEvent):
    user_id = str(event.get_user_id())
    response = reborn.send_get_request()
    data = json.loads(response)
    country = data["country"]["cn"]
    continent = data["continent"]["cn"]
    if user_id not in dataset:
        dataset[user_id] = {"亚洲": 0, "欧洲": 0, "北美洲": 0, "南美洲": 0, "非洲": 0, "大洋洲": 0}
    if user_id not in cnt:
        cnt[user_id] = 0
    dataset[user_id][continent] += 1
    cnt[user_id] += 1
    msg = MessageSegment.reply(event.message_id) + MessageSegment.text("似咯，remake到了" + continent + "，" + country + "\nremake了" + str(cnt[user_id]) + "次\n" + "亚洲: " + str(dataset[user_id]["亚洲"]) + "\n欧洲: " + str(dataset[user_id]["欧洲"]) + "\n北美洲: " + str(dataset[user_id]["北美洲"]) + "\n南美洲: " + str(dataset[user_id]["南美洲"]) + "\n非洲: " + str(dataset[user_id]["非洲"]) + "\n大洋洲: " + str(dataset[user_id]["大洋洲"]) + "\n")
    await make_reborn.finish(msg)
