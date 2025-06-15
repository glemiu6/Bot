import ollama
system=input('system:')
messages=[{'role':'system', 'content':system}]
while True:
    prompt=input("user:")
    if prompt in ["exit","quit"]:
        break
    messages.append({'role':"user", 'content':prompt})
    response=ollama.chat(model='llama3.2',messages=messages)
    reply=response['message']['content']
    print("Bot: "+reply)
    messages.append({'role':'assistant',"content":reply})