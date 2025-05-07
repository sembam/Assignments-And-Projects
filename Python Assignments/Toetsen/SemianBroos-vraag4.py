import random
import string

def maak_wachtwoord( aantal_karakters ):
    '''
    maakt een willekeurig wachtwoord aan van karakters die meegegeven zijn in de parameters.
    '''
    characters = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(characters) for i in range(8))
    print('random password is', result)

    return

maak_wachtwoord( aantal_karakters='' )