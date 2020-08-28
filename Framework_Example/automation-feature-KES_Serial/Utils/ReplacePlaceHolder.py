import random
import string


def randomNumber(last_number=999999999):
    return random.randrange(last_number)


def randomNumbersChars(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TestingUtils:

    @staticmethod
    def replacePlaceholder(text_with_place_holder):
        """
        Replace placeholder to some text, depend on placeholder type
        :<UniqueValue>: Replaced with 9 digits random unique number
        :<UniquePasswordValue>: Replace placeholder with random chars and digits string to create unique password
        """
        if "<UniqueValue>" in text_with_place_holder:
            return text_with_place_holder.replace("<UniqueValue>", str(randomNumber()))
        elif "<UniquePasswordValue>" in text_with_place_holder:
            return text_with_place_holder.replace("<UniquePasswordValue>", str(randomNumbersChars()) + str(1))
