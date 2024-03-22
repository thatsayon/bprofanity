from bprofanity import ProfanityChecker
import os

profanity_checker = ProfanityChecker(
    os.path.abspath(os.path.dirname(__file__)))

profanity_checker.load_words()

print(profanity_checker.contains_profanity("r game"))
print(profanity_checker.get_words())
