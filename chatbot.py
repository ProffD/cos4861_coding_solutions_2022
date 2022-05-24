import datetime
from nltk.chat.util import Chat, reflections

date = datetime.date.today()

conversation = [
                    ['(Hello|Hi|Hey|Yho)', ['Hey']],
                    ["(Morning|Afternoon|Evening|Good (.*))", ["Good %1 to you too"]],
                    ["My name is (.*)", ["Hey %1, I am Tom, how can I help you?"]],
                    ["(Thanks|Thank you)", ["It's a pleasure my dear"]],
                    ['(How are you|How you doing)', ["I'm doing fine and you?"]],
                    ["(I'm fine|I am good)", ["Glad to hear, how may I help you?"]],
                    ["it is (.*)", ["Yes %1"]],
                    ["How old are you?", [f"I am {date.year - 2020} years old"]],
                    ["Where do you stay?", ["I stay inside the program"]],
                    ["Are you a (human|person)", ["No I am a bot"]]
                ]

chat = Chat(conversation, reflections)


def chat_bot():
    print('Hello my name is Tom, how may I help you?')
    print('Enter the word quit when you done')
    chat.converse()


chat_bot()
