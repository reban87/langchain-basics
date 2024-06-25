from decouple import config
import openai

openai.api_key = config("OPENAI_API_KEY")

# response = openai.Completion.create(
#     model="GPT-3.5 Turbo", prompt="Say this is a test", temperature=0, max_tokens=7
# )

print(openai.api_key)
