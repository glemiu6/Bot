import requests 
ollama_url="http://localhost:11434/api/chat"

def send_message(message,model='llama3.2',history=[]):
    history.append({"role":'user',
                   'content':message})
    response=requests.post(ollama_url,json={
        "model": model,
        "message":history
    })
    data=requests.json()
    history.append({"role":"assistant","content":data["message"]["content"]})
    return data['message']['content'],history

if __name__=="__main__":
    history=[]
    print("chatbot(scrie exit data vrei sa iesi)")
    while True:
        user_input=input("tu:")
        if user_input.lower()=="exit":
            break
        reply,history=send_message(user_input,history=history)
        print("bot:",reply)