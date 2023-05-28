import openai
# if you are in china, you should open proxy
proxies = {
'http': "http://127.0.0.1:4780",
'https': "http://127.0.0.1:4780"}
openai.proxy = proxies

# 设置OpenAI API的访问密钥
openai.api_key = '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'

# 设置GPT模型的引导提示（Prompts）
prompts = [
    "手淫会对我的身体和心理产生负面影响，例如减弱性欲、自卑感等。",
    "不手淫的好处是可以集中精力在更有意义的事情上，提高自我控制能力。",
    "手淫并不是一个积极健康的习惯，我应该努力改变它。",
]

theory = ''
for p in prompts:
    theory += p
# 辩论函数
def debate_with_gpt(user_input, celebrity_tone=None):
    # 构建完整的输入文本
    input_text = '我有手淫的欲望，你要和我进行辩论，让我打消这个念头\n' + user_input + '\nGPT:'

    if celebrity_tone:
        input_text = f'[{celebrity_tone}] ' + input_text

    # 构建消息列表
    messages = [
        {"role": "system", "content": "你是反对手淫的一方, 你要尽可能遵循理论依据，多引用理论依据方面去争辩，少去关注你的知识, 你的理论依据是： "+ theory},
        {"role": "user", "content": user_input}
    ]

    # 发送请求给OpenAI的Chat模型生成回复
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=messages,
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None
    )

    # 解析并返回GPT的回复
    reply = response.choices[0].message.content.strip()
    return reply

# 主程序
def main():
    celebrity_tone = "像tarloy swift一样语气性格回答"
    while True:
        user_input = input("请输入您的观点：")
        if user_input.lower() == 'exit':
            break
        reply = debate_with_gpt(user_input, celebrity_tone)
        print(reply)

if __name__ == '__main__':
    main()
