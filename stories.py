"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["noun", "adjective", "verb", "adjective", "noun"],
    """The year was 1744 and {noun} was {adjective}. 
    He {verb} a {adjective} life. 
    Until one day he was murdered by the {noun}."""
)

story3 = Story(
    ["adjective", "adjective", "noun", "verb", "noun"],
    """Johnny was a very {adjective} boy. Others said he was too {adjective}.
    But his brother knew that if he was stranded on a {noun} with Johnny,
    and there sun was {verb} down on them. Johnny would get them
    back to the {noun} safely. """
)