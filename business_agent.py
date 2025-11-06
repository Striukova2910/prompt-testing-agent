from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()
def replies(prompt_document:str, model: str, temperature_business_agent:float):
    llm = ChatOpenAI(model=model, temperature = temperature_business_agent, max_tokens=200, stop_sequences=None)
    business_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', "you are business agent"),
        ("user", '{input}'),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    @tool
    def business_tool(user_agent_replica:str) -> str:
        """Reply to user_agent"""
        return llm.invoke(f"user_message:{user_agent_replica}").content

    return AgentExecutor(
                agent=create_tool_calling_agent(llm=llm, tools=[business_tool], prompt=business_agent_prompt),
                tools=[business_tool],
                verbose = False)