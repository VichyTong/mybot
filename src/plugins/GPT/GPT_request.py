import openai
import nonebot

openai.api_key = nonebot.get_driver().config.openai_api_key


def send_get_request(msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant. Please answer the user's question with imagination. The output language is determined by the user's question."},
            {"role": "user", "content": msg}
        ],
        max_tokens=2000,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["END"]
    )
    return response['choices'][0]['message']['content'].strip()
