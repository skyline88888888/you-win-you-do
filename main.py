import openai

# 设置OpenAI API的访问密钥
openai.api_key = 'YOUR_API_KEY'

# 设置GPT模型的引导提示（Prompts）
prompts = [
    "手淫会对我的身体和心理产生负面影响，例如减弱性欲、自卑感等。",
    "不手淫的好处是可以集中精力在更有意义的事情上，提高自我控制能力。",
    "手淫并不是一个积极健康的习惯，我应该努力改变它。"
]

# 辩论函数
def debate_with_gpt(user_input, celebrity_tone=None):
    # 构建完整的输入文本
    input_text = '我打算手淫，但我需要和你进行辩论。\n' + user_input + '\nGPT:'

    if celebrity_tone:
        input_text = f'[{celebrity_tone}] ' + input_text

    # 发送请求给OpenAI GPT模型生成回复
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )

    # 解析并返回GPT的回复
    reply = response.choices[0].text.strip().replace('GPT:', '')
    return reply

# 主程序
def main():
    celebrity_tone = "像明星X一样"
    while True:
        user_input = input("请输入您的观点：")
        if user_input.lower() == '退出':
            break
        reply = debate_with_gpt(user_input, celebrity_tone)
        print(reply)

if __name__ == '__main__':
    main()
