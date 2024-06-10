import chainlit as cl
from crew import JJMCrew

@cl.on_message
async def main(message: cl.Message):
    
    query = message.content
    print("******Agent Started Working**********")

    response = JJMCrew(query)
    answer = response.run()

    print("******Agent finished Task************")

    msg = cl.Message(content = answer)
    await msg.send()