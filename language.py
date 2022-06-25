from cgitb import text
from playsound import playsound as PS  
import speech_recognition as s_r   
from googletrans import Translator as Trans   
from gtts import gTTS   
import os  

dic_language = ('afrikaans', 'af', 'albanian', 'sq',
	'amharic', 'am', 'arabic', 'ar',
	'armenian', 'hy', 'azerbaijani', 'az',
	'basque', 'eu', 'belarusian', 'be',
	'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
	'bg', 'catalan', 'ca', 'cebuano',
	'ceb', 'chichewa', 'ny', 'chinese (simplified)',
	'zh-cn', 'chinese (traditional)',
	'zh-tw', 'corsican', 'co', 'croatian', 'hr',
	'czech', 'cs', 'danish', 'da', 'dutch',
	'nl', 'english', 'en', 'esperanto', 'eo',
	'estonian', 'et', 'filipino', 'tl', 'finnish',
	'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
	'gl', 'georgian', 'ka', 'german',
	'de', 'greek', 'el', 'gujarati', 'gu',
	'haitian creole', 'ht', 'hausa', 'ha',
	'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
	'hi', 'hmong', 'hmn', 'hungarian',
	'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
	'id', 'irish', 'ga', 'italian',
	'it', 'japanese', 'ja', 'javanese', 'jw',
	'kannada', 'kn', 'kazakh', 'kk', 'khmer',
	'km', 'korean', 'ko', 'kurdish (kurmanji)',
	'ku', 'kyrgyz', 'ky', 'lao', 'lo',
	'latin', 'la', 'latvian', 'lv', 'lithuanian',
	'lt', 'luxembourgish', 'lb',
	'macedonian', 'mk', 'malagasy', 'mg', 'malay',
	'ms', 'malayalam', 'ml', 'maltese',
	'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
	'mn', 'myanmar (burmese)', 'my',
	'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
	'pashto', 'ps', 'persian', 'fa',
	'polish', 'pl', 'portuguese', 'pt', 'punjabi',
	'pa', 'romanian', 'ro', 'russian',
	'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
	'serbian', 'sr', 'sesotho', 'st',
	'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
	'slovak', 'sk', 'slovenian', 'sl',
	'somali', 'so', 'spanish', 'es', 'sundanese',
	'su', 'swahili', 'sw', 'swedish',
	'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
	'te', 'thai', 'th', 'turkish',
	'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
	'ug', 'uzbek', 'uz',
	'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
	'yiddish', 'yi', 'yoruba',
	'yo', 'zulu', 'zu')


def take_command():  
    r1 = s_r.Recognizer()  
    with s_r.Microphone() as source:  
        print ("listening to the voice...")  
        r1.pause_threshold = 1  
        audio1 = r1.listen(source)  
    
    try:  
        print ("Recognizing the voice...")  
        query_1 = r1.recognize_google(audio1, language = 'en-in')  
        print (f" user said? {query_1}\n")  
    except Exception as ep:  

        print ("The user is requested to please say that again...")  
        return "None"  
    return query_1  
 

query_1 = take_command()
while (query_1 == "None"):
	query_1 = take_command()

def destination_language():  
    print("Please enter the language in which you want to convert the above input \  : Ex. English, Hindi, German, French etc.")  
    print()  
    to_language = take_command()  
    while (to_language == "None"):  
        to_language = take_command()  
    to_language = to_language.lower()  
    return to_language  
    
to_language = destination_language()  
    
while (to_language not in dic_language):  
    print ("The language in which the user wants to convertthe voice command\ is currently not available, the user is requested to input some other language")  
    print()  
    to_language = destination_language()  
    
to_language = dic_language[dic_language.index(to_language)+1]  
translator1 = Trans()   
text_to_translate_1 = translator1.translate(query_1, dest = to_language)  
text1 = text_to_translate_1.text   
speak = gTTS(text = text1, lang= to_language)  
speak.save("captured_JTP_voice.mp3")  
PS('captured_JTP_voice.mp3')  
os.remove('captured_JTP_voice.mp3')  
print(text)  
