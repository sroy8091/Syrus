from chatterbot import ChatBot
from gtts import gTTS
import os
import speech_recognition
#from chatterbot.training.trainers import ChatterBotCorpusTrainer


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speech_engine.say("Say something!")
        audio = r.listen(source)

bot = ChatBot("Syrus", 
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter", 
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",  
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter",
        "chatterbot.adapters.logic.ClosestMeaningAdapter",
        
    ],
    database='chatterbot-database',
    read_only=True
    )

#bot.set_trainer(ChatterBotCorpusTrainer)


bot.train(
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english"
    )

while True:
    try:
        text = (bot.get_response(None))
        tts = gTTS(text= text, lang="en")
        tts.save("bot.mp3")
        os.system("mpg321 bot.mp3")
        
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
