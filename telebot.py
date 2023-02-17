from telegram.ext import *
import openai

token= '5799419498:AAEIq9_4V8Vn8_pAO_akY-7eiDHbuBWECl4'
openai.api_key = "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"
chatlist=[]
username=""

prefix = "Sarah is a girlfriend who is a female romantic partner in a committed relationship. She is typically someone who is caring, supportive, and loyal. A girlfriend can be a great listener and a source of emotional support. She may have shared interests with her partner and enjoy spending quality time together. She may also have her own hobbies and interests that she pursues independently. A girlfriend may be someone who shares her partner's values and goals, and helps him to achieve them. She can be a source of motivation and inspiration. In addition, a girlfriend may be physically affectionate, showing her love through hugs, kisses, and other displays of affection. She can also be someone who challenges her partner to be his best self, and who supports him in his personal and professional growth."
chatlist.append(prefix)

def sample_responses(input_text,username):
    username=username
    print(username)
    user_message = str(input_text).lower()
    joinedlist=",".join(chatlist)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{joinedlist} {username}:{user_message}Sarah:", #plugged AI at the end to make it stop typing
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=[f"{username}:","Sarah:"]) # remove the AI: to if there is a prefix
    chatlisnl = response.choices[0].text
    chatlist.append(f"{username}:{user_message}")
    chatlist.append(f"Sarah:{chatlisnl}")
    print (joinedlist)
    print (response.choices[0])
    return response.choices[0].text.replace(',', '').replace('Sarah:', '')
    
def start(update, context):
    update.message.reply_text('Hi!')
    
def handle_message(update, context):
    username = update.message.from_user.first_name
    text = str(update.message.text).lower()
    response = sample_responses(text, username)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    print("Bot started...")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()