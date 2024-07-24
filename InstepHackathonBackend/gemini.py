import google.generativeai as genai
GOOGLE_API_KEY="AIzaSyCqCDRg0WqwSzDDzrWmhoBHPuQ7jSvWjdY"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def getCompletion(prompt):
    response = model.generate_content(prompt)
    return response.candidates[0].content.parts[0].text