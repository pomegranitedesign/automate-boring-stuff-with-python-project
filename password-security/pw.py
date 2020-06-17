#! python3
# pw.py - Unsafe password storage
import sys
import pyperclip

PASSWORDS = {
    'email': '5i3uit2ewjgsiguisguwew',
    'blog': 'eiwqiruq1rq3uwjs9v989389184',
    'luggage': '921irofeius38q090'
}

if len(sys.argv) == 1:
    print("Using: python pw.py [USER_NAME] - copying account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' was sent to buffer')
else:
    print('Account ' + account + ' is not found...')
