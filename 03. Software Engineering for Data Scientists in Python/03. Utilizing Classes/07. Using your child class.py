'''
Using your child class
Thanks to the power of inheritance you were able to create a feature-rich, SocialMedia class based on its parent, Document. Let's see some of these features in action.

Below is the full definition of SocialMedia for reference. Additionally, SocialMedia has been added to __init__.py for ease of use.

class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')
Instructions
100 XP
import your text_analyzer custom package.
Define dc_tweets as an instance of SocialMedia with the preloaded datacamp_tweets object as the text.
print the 5 most_common mentioned users in the data using the appropriate dc_tweets attribute.
Use text_analyzer's plot_counter() method to plot the most used hashtags in the data using the appropriate dc_tweets attribute.
'''
SOLUTION

# Import custom text_analyzer package
import text_analyzer

# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.word_counts)
