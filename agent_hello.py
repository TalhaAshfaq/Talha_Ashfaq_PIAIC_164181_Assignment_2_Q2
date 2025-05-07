from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel, set_tracing_disabled, set_default_openai_api 
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def my_first_agent():

    external_client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/",
        api_key=api_key               
    )

    set_default_openai_client(external_client)
    set_tracing_disabled(True)
    set_default_openai_api("chat_completions")

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )


    agent = Agent(name="Assistant", instructions="You are a helpful assistant", model=model)
    
    result = Runner.run_sync(agent, "Write a message Hello World From my first Agent")
    
    print(result.final_output)