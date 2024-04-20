import requests

url = r"https://discord.com/api/v9/channels/1130465960038514778/messages"

header = {
    'authorization' : 'MTA3NjcwMzUxODQ3MzMzMDczMQ.G0vQAy.tEhxlHcXwJt7WWX6rpdWsJXN8HfhfE5hHQe52g'
}

payload = {
    'content' : 'TEST : DISCORD SPAM BOT'
}

r = requests.post(url=url, data=payload, headers=header)
