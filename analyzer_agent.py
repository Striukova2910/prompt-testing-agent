from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()


def analyze(dialogue_business_and_user:list, checklist:str, model:str):
    llm = ChatOpenAI(model=model, temperature =0)
    prompt = (
        f"You are an LLM analyst. Check whether the business agent’s responses were relevant to the prompt.\n"
        f"Use the checklist for evaluation:\n{checklist}\n\n"
        f"Dialogue:\n{dialogue_business_and_user}\n\n"
        f"Rate on a scale from 1 to 10 and specify any issues (if there are any)."
        f"Present the analysis results in bullet points, each starting on a new line."
    )
    return llm.invoke(prompt).content