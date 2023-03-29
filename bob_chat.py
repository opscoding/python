def response(hey_bob) -> str:
    """
    """
    if hey_bob == "How are you?":
        return "Sure"
    if hey_bob == hey_bob.upper() and "?" not in hey_bob and hey_bob != '':
        return "Whoa, chill out!"
    if hey_bob == hey_bob.upper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing"
    if hey_bob == '':
        return "Fine. Be that way!"
    return 'Whatever.'

if __name__ == '__main__':
    print(response("How are you?"))
    print(response("HOW ARE YOU"))
    print(response("HOW ARE YOU?"))
    print(response(''))
    print(response("Does this cryogenic chamber make me look fat?"))