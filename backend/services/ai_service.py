import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_channel_review(
    channel_data
):
    prompt = f"""
You are a YouTube growth consultant.

Analyze this channel:

Channel Name: {channel_data['channel_name']}
Genre: {channel_data['genre']}
Health Score: {channel_data['health_score']}
Growth Score: {channel_data['growth_score']}
Creator Segment: {channel_data['creator_segment']}
Channel Age: {channel_data['channel_age']}

Provide:

1. Strengths
2. Weaknesses
3. Growth Opportunities
4. Action Plan

Keep the response practical and concise.
"""

    response = model.generate_content(
        prompt
    )

    return response.text


def generate_competitor_review(
    channel1,
    channel2
):
    prompt = f"""
You are an expert YouTube growth consultant.

Compare these two channels.

Channel 1:
Name: {channel1['channel_name']}
Genre: {channel1['genre']}
Health Score: {channel1['health_score']}
Growth Score: {channel1['growth_score']}
Creator Segment: {channel1['creator_segment']}

Channel 2:
Name: {channel2['channel_name']}
Genre: {channel2['genre']}
Health Score: {channel2['health_score']}
Growth Score: {channel2['growth_score']}
Creator Segment: {channel2['creator_segment']}

Provide:

1. Winner Analysis
2. Strengths of Channel 1
3. Strengths of Channel 2
4. What Channel 1 Can Learn
5. What Channel 2 Can Learn
6. Growth Recommendations

Keep the response concise and actionable.
"""

    response = model.generate_content(prompt)

    return response.text




def generate_growth_strategy(
    channel_data
):
    prompt = f"""
You are an expert YouTube Growth Strategist.

Analyze this channel:

Channel Name: {channel_data['channel_name']}
Genre: {channel_data['genre']}
Health Score: {channel_data['health_score']}
Growth Score: {channel_data['growth_score']}
Creator Segment: {channel_data['creator_segment']}
Channel Age: {channel_data['channel_age']}

Provide:

1. Current Channel Assessment
2. 30-Day Growth Plan
3. Content Ideas (10 ideas)
4. Thumbnail Strategy
5. SEO Recommendations
6. Upload Schedule
7. Growth Opportunities

Keep the response actionable and professional.
"""

    response = model.generate_content(
        prompt
    )

    return response.text