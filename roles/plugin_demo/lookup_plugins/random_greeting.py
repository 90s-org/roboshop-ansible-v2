from ansible.plugins.lookup import LookupBase
import random

DOCUMENTATION = """
  name: random_greeting
  short_description: Returns a random greeting word
  description:
    - Picks a random greeting from a fixed list for each term passed in.
"""

GREETINGS = ["Hello", "Hi", "Hey", "Howdy", "Greetings"]


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        return [random.choice(GREETINGS) for _ in terms]
