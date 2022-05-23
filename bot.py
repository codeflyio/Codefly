from random import randint
import json
from ibm_watson import AssistantV2, AssistantV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import keys

assistant = AssistantV2(
    version='2021-06-14',
    authenticator=IAMAuthenticator(keys.IAMValue)  # api key
)
assistant.set_service_url(keys.assistant_service_url)


def reply(user):

    # noinspection PyTypeChecker
    response = assistant.message_stateless(
        assistant_id=keys.assistant_id,
        input={
            'message_type': 'text',
            'text': user
        }
    ).get_result()
    # print(json.dumps(response, indent=2))

    return response["output"]["generic"][0]["text"]

# responses = {
#     "0": "It is certain.",
#     "1": "It is decidedly so.",
#     "2": "Without a doubt.",
#     "3": "Yes definitely!",
#     "4": "You may rely on it.",
#     "5": "As I see it, yes.",
#     "6": "Most likely.",
#     "7": "Outlook good.",
#     "8": "Yes!",
#     "9": "Signs point to yes!",
#     "10": "Reply hazy, try again.",
#     "11": "Ask again later.",
#     "12": "Better not tell you now.",
#     "13": "Cannot predict now.",
#     "14": "Concentrate and ask again!",
#     "15": "Don't count on it!",
#     "16": "My reply is no.",
#     "17": "My sources say no.",
#     "18": "Outlook not so good.",
#     "19": "Very doubtful."
# }
# return responses[str(randint(0, 19))]
