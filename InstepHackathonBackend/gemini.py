import google.generativeai as genai
from dotenv import load_dotenv
import os
from fastapi import FastAPI
app = FastAPI()
load_dotenv()
import uvicorn
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
async def getCompletion(prompt):
    response = genai.generate_text(prompt= prompt)
    return response.result


def getRecommendationPrompt(skills,projects,availableCourses):
    return f'''
There is an employee who has these skills {skills} and has worked on these projects {projects}. I want you to recommend the best 5 courses for the employee from the list courses don't include more than 5 courses: {availableCourses}
Make sure to give the output as a json with the following format:
{{
  recommendation: [Courses recommendation]
}}
'''

from pydantic import BaseModel
class Recommendation(BaseModel):
    skills:dict
    projects:dict
    availableCourses:dict
@app.post("/recommendations")
async def getRecommendation(request:Recommendation):
    skills=request.skills
    projects=request.projects
    availableCourses=request.availableCourses
    prompt = getRecommendationPrompt(skills, projects, availableCourses)
    response = await getCompletion(prompt)
    return response

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)