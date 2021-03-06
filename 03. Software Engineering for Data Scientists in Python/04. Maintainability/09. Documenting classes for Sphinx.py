'''
Documenting classes for Sphinx
sphinx is a great tool for rendering documentation as HTML. In this exercise, you'll write a docstring for a class that can be taken advantage of by sphinx.

Note that your docstring submission must match the solution exactly. If you find yourself getting it wrong several times, it may be a good idea to refresh the sample code and start over.

Instructions
100 XP
import the Document class from the text_analyzer package for use in the class definition.
Complete the line of the docstring dealing with the parameters of the __init__ method.
Complete the docstring by filling out the documentation for the attributes or 'instance variables' of the SocialMedia class.
'''
SOLUTION

from text_analyzer import Document

class SocialMedia(Document):
    """Analyze text data from social media
    
    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
