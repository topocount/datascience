The purpose of this project was to conduct string analysis and test some hyptheses about Jeopardy preparation strategies using previous questions. 

As shown in the notebook, the strings of the questions and corresponding answers and values were parsed into lists and the low-value word "the" was removed from the lists. the question and answer lists were compared and only 5.8% of the words in the questions were within the answer. This showed that jeopardy answers decidedly did not include the same words as the question.

Next, the possibility of recycling questions was examined. Only high-value words were examined, where the word contains more than 5 letters. When comparing individual words, 69% were used more than once. However, comparison of word groupings and phrases would provide a more accurate measure of question recycling, since it would account for context.

Lastly, a very small sample of words were tested to see if studying mostly high-value questions (where the value is greater than $800) is a worthwhile endeavor.  This is accomplished by running a chi-squared test and seeing if their use is signficantly different in high vs low valued questions. The differnces were significant for some words, more more words need to be tested to determine the utility of this method. (Only 5 words were tested in this exercise).

To Do:

* Create list of low-value words like "than", "the", "and" etc
* Find a list of stopwords to use also
* Remove words that occur in more than 5% of questions
* Perform the chi-squared test on more terms
* Perform some analysis on the Category column: category probabilities of appearing, etc.
* Look at phrases in question recycling
