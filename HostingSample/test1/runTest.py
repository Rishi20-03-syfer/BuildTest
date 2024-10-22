from dotenv import dotenv_values

api_key = dotenv_values(".env")
print(api_key.get('GEMINI_API_KEY'))