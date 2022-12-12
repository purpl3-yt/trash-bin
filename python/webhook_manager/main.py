from discord_webhook import DiscordWebhook
import requests
print('Webhook Manager by Purpl3\n')

webhook_url = input('Enter an webhook (url): ')

while True:
    
    action = input('Enter an action for help enter "help": ');action = action.lower()

    if action in ['help','hlp']:
        print('''
Actions: 
1) Send Message
2) Spam
3) Get info of webhook
Utils:
8) Change webhook url
9) Exit''')

    elif action in ['send','1','sendmessage']:
        webhook_content = input('Enter an message: ')

        DiscordWebhook(webhook_url,content=webhook_content).execute()

        print('Done!')

    elif action in ['spam','2','massspam']:
        webhook_content = input('Enter an message: ')
        spam_count = str(input('Enter an count of spam (int): '))
        if spam_count.isdigit():
            for c in range(int(spam_count)):
                DiscordWebhook(webhook_url,content=webhook_content).execute()
                print('Spam')

        else:
            print('Enter an digits!')

    elif action in ['3','info','getinfo']:
        
        info = requests.get(webhook_url).json()

        for j in info:
            print(str(j)+': '+str(info[j]))

    elif action in ['changeurl','url','8']:
        webhook_url = input('Enter an webhook (url): ')

    elif action in ['exit','9']:
        quit()