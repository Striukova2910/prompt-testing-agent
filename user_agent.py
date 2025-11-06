from dotenv import load_dotenv
import random as rnd
from langchain_openai import ChatOpenAI
load_dotenv()
import openai

def user_simulator(prompt, main_question, user_agent_mode, temperature, followups=3):
    """
    Генерирует основной вопрос + follow-up вопросы по одной теме.
    main_question: основной вопрос из тест-кейсов
    followups: сколько уточняющих вопросов юзер задаёт по теме
    """


    """all_questions = [main_question]  # начнём с основного вопроса

    previous_q = main_question
    for _ in range(followups):
        # Генерируем follow-up вопрос через API GPT
        system_prompt = prompt + "\nYour task: ask a follow-up question on the same topic, based on previous question."
        response = openai.ChatCompletion.create(
            model=user_agent_mode,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Previous question: {previous_q}"}
            ],
            temperature=temperature,
            max_tokens=60  # короткий уточняющий вопрос
        )
        followup_q = response.choices[0].message["content"].strip()
        all_questions.append(followup_q)
        previous_q = followup_q  # следующий follow-up строится на предыдущем
    return all_questions"""










#-------------previous-------------------------------
def user_simulator(user_agent_prompt:str, questionlines:str, llm_model:str, temperature_user_agent:float, followups:int = 3):
    llm = ChatOpenAI(model=llm_model, temperature = temperature_user_agent)
    user_inputs = []
    prompt = (
            f"{user_agent_prompt}\n\n"
            f"Based on the topic: «{questionlines}», generate {followups} related questions.\n"
            f"The questions should form a connected dialogue. Each question is a natural follow-up, clarification, or request for more details on the topic.\n"
            f"Do not explain. Do not answer. Just return {followups} questions, one per line."
        )
    result = llm.invoke(prompt).content.strip()
    user_inputs = []
    for line in result.split("\n"):
        stripped_line = line.strip()
        if stripped_line:
            user_inputs.append(stripped_line)
    return user_inputs














    #-------------------------old---------------------------
    # user_agent_prompt = ChatPromptTemplate.from_messages([
#     ('system', "you are user who needs help"),
#     ("user", '{input}')
# ])
# @tool
# def user_agent_tool(user_agent_replica:str) -> str:
#     """Reply to user_agent"""
#     return llm.invoke(f"user_message:{user_agent_replica}").content
#
# agent = AgentExecutor(
#             agent=create_tool_calling_agent(llm=llm, tools=[user_agent_tool], prompt=user_agent_prompt),
#             tools=[user_agent_tool],
#             verbose = False)