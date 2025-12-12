def response(hey_bob):
    stripped_hey_bob = hey_bob.strip()
    is_question = stripped_hey_bob.endswith('?')
    is_yelling = stripped_hey_bob.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    elif is_question:
        return "Sure."

    elif is_yelling:
        return "Whoa, chill out!"

    elif not stripped_hey_bob:
        return "Fine. Be that way!"

    else:
        return "Whatever."
