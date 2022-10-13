import random
import string


class RandomString:
    def get_random_string() -> str:
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        return result_str
