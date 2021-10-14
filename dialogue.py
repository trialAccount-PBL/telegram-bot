from datetime import datetime

API_KEY = "2052420657:AAHLqVzRPvBca74olM_7QjL6H8GQbljq3XY"

userGreetings = ["hello", "hey", "yo", "sup"]
userQuestions = ["who are you", "who are you ?", "who are you ??"]

facts = [
    "I am a bot",
    "I was created by a human",
    "The fastest gust of wind ever recorded on Earth was 253 miles per hour",
    "The average human lifespan is about 10.5 years",
    "The average lifespan of a dog is about 13.5 years",
    "The average lifespan of a cat is about 15 years",
    "The average lifespan of a rabbit is about 11 years",
    "The average lifespan of a horse is about 17 years",
    "The average lifespan of a cow is about 15 years",
    "The average lifespan of a snake is about 10 years",
    "The average lifespan of a spider is about 10 years",
    "The average lifespan of a bird is about 13 years",
]


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in userGreetings:
        return "Hello! Hope you are doing well!"
    elif user_message in userQuestions:
        return "I am a bot"
    else:
        return "I don't know what you mean"
