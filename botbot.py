import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2090676535216-2073046477764-GiWLgsD1S2FLGvIh0XAUY4rl"
 
post_message(myToken,"#upbit","jocoding")
