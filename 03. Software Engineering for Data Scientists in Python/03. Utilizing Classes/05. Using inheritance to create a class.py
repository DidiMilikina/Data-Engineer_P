'''
Using inheritance to create a class
You've previously written a Document class for text analysis, but your NLP project will now have a focus on Social Media data. Your general Document class might be useful later so it's best not destroy it while your focus shifts to tweets.

Instead of copy-pasting the already written functionality, you will use the principles of 'DRY' and inheritance to quickly create your new SocialMedia class.

Instructions
100 XP
Document has been preloaded in the session.
Complete the class statement to create a SocialMedia class that inherits from Document.
Define SocialMedia's __init__() method that initializes a Document.
'''
SOLUTION

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
