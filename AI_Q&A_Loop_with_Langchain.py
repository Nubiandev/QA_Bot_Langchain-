from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#Defining my ssh key
api_key = "Will enter key for testing here"

#defining LLM
llm = OpenAI(api_ky=api_key)

#Prompt Template to instruct A.I
prompt_template = """
You are an AI assistant. Please provide a detailed and accurate answer.

Question: {user_question}
Answer:
"""

#Langchain Prompt
prompt = PromptTeemplate(
    input_variables=["user_question"],
    template=prompt_template
)

#LLM Chain
llm_chain = LLMChain(llm=llm, prompt=prompt)

def main():
    # Step 1: AI introduction
    print("Hello! I am Mother A.I\n's first AI assistant. I'm here to help you with your questions and tasks.")

    # Step 2: Prompt the user for their name
    user_name = input("What is your name? ")

    # Step 3: Greet the user
    print(f"Nice to meet you, {user_name}!")

if __name__ == "__main__":
    main()


#Loop continuous interaction
print("Welcome back to Mother AI\n's Q&A assistant. Ask me anything (type 'exit'to stop):")

while True:
    user_question = input("Your Question: ")

    if user_question.lower() == 'exit':
        print("Goodbye! Thank you for using tne AI assistant.")
        break

#Uses Langchain to return information to A.I  

    response = llm_chain.run(user_question)

    print("AI's answer:", response)
    print("\n-------------------------------\n")
