#Need Api Key and store the Chat history of human/AI to build free flow conversation

from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate

# Initialize an empty list to store the conversation
conversation_history = []

# Define the system message
system_message = SystemMessagePromptTemplate.from_template("You are a helpful assistant.")
print( system_message.prompt.template)
conversation_history.append(("system", system_message.prompt.template))

# Define the human message
human_message = HumanMessagePromptTemplate.from_template("My name is Shilpa and I live in New York?")
conversation_history.append(("human", human_message.prompt.template))

# Define the AI message
ai_message = AIMessagePromptTemplate.from_template("New York is beautiful state and New York city is happening place.")
conversation_history.append(("ai", ai_message.prompt.template))
print(conversation_history)



while True:
    user_input = input("Enter something (or type 'done' to finish): ")
    human_message = HumanMessagePromptTemplate.from_template(user_input)
    conversation_history.append(("human", human_message.prompt.template))
    print("conversation_history  :" + str(conversation_history))
    # Processing the input through the chain and converting to uppercase
    chat_prompt_template = ChatPromptTemplate(messages =conversation_history)
    chain = chat_prompt_template | chat_llm | output_parser | RunnableLambda(lambda x: x.upper())
    response = chain.invoke({})  # Invoke the chain
    conversation_history.append(("ai", response))
    
    print("Processed response:", response)
    
    if user_input.lower() == "done":
        break  # Exit the loop when 'done' is entered
