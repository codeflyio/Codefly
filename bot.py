from random import randint
import json

import requests
from flask import request
from ibm_watson import AssistantV2, AssistantV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import keys

assistant = AssistantV2(
    version='2021-06-14',
    authenticator=IAMAuthenticator(keys.IAMValue)  # api key
)
assistant.set_service_url(keys.assistant_service_url)


def reply(user):

    if "!8ball".lower() in user:
        return eight_ball()
    if "!word" in user:
        return word_of_the_day()

    # noinspection PyTypeChecker
    response = assistant.message_stateless(
        assistant_id=keys.assistant_id,
        input={
            'message_type': 'text',
            'text': user
        }
    ).get_result()

    try:
        intent = response['output']['intents'][0]['intent']
    except (IndexError, KeyError, Exception) as e:
        intent = None

    try:
        entity = response['output']['entities'][0]['value']
    except (IndexError, KeyError, Exception) as e:
        entity = None

    try:
        spelling = f'Did you mean: {response["output"]["spelling"]["text"]} ?'
    except (IndexError, KeyError, Exception) as e:
        spelling = None

    text = response["output"]["generic"][0]["text"]
    # print(json.dumps(response, indent=2))

    if intent == "Definition":
        return definitions(entity)

    return text


def definitions(entity):
    with open('static/dictionary.json', 'r') as dictionary:
        data = json.load(dictionary)
    word = data[entity]
    return word


def word_of_the_day():
    data = requests.get(f'https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={keys.wordnik}').json()
    result = f"{data['word']}:  {data['definitions'][0]['text']}  https://www.wordnik.com/words/{data['word']}"
    return result


def eight_ball():
    response = {
        "0": "It is certain.",
        "1": "It is decidedly so.",
        "2": "Without a doubt.",
        "3": "Yes definitely!",
        "4": "You may rely on it.",
        "5": "As I see it, yes.",
        "6": "Most likely.",
        "7": "Outlook good.",
        "8": "Yes!",
        "9": "Signs point to yes!",
        "10": "Reply hazy, try again.",
        "11": "Ask again later.",
        "12": "Better not tell you now.",
        "13": "Cannot predict now.",
        "14": "Concentrate and ask again!",
        "15": "Don't count on it!",
        "16": "My reply is no.",
        "17": "My sources say no.",
        "18": "Outlook not so good.",
        "19": "Very doubtful."
    }
    return response[str(randint(0, 19))]
