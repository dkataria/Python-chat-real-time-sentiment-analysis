
__author__ = "Deep Katariya"



from nltk.classify import NaiveBayesClassifier
from nltk.corpus import sentence_polarity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

''' Training, testing and evaluation code'''
# def another():
#     # print('IMport passed')
#     n_instances = 5000
#     pos_docs = [(sent, 'pos') for sent in sentence_polarity.sents(categories='pos')[:n_instances]]
#     neg_docs = [(sent, 'neg') for sent in sentence_polarity.sents(categories='neg')[:n_instances]]
#     # print(len(pos_docs)), print(len(neg_docs))
#
#     train_pos_docs = pos_docs[:4000]
#     test_pos_docs = pos_docs[4000:5000]
#     train_neg_docs = neg_docs[:4000]
#     test_neg_docs = neg_docs[4000:5000]
#     training_docs = train_pos_docs + train_neg_docs
#     testing_docs = test_pos_docs + test_neg_docs
#
#     sentim_analyzer = SentimentAnalyzer()
#     all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
#     # print(all_words_neg)
#     unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=2)
#     sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
#
#     training_set = sentim_analyzer.apply_features(training_docs)
#     test_set = sentim_analyzer.apply_features(testing_docs)
#     # print(type(test_set))
#
#     trainer = NaiveBayesClassifier.train
#     classifier = sentim_analyzer.train(trainer, training_set)
#     for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
#         print('{0}: {1}'.format(key, value))

def polarity_score(message):
    # sentences = ["VADER is smart, handsome, and funny.", # positive sentence example
    #     "VADER is smart, handsome, and funny!", # punctuation emphasis handled correctly (sentiment intensity adjusted)
    #     "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
    #     "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
    #     "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
    #     "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",# booster words & punctuation make this close to ceiling for score
    #     "The book was good.",         # positive sentence
    #     "The book was kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
    #     "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
    #     "A really bad, horrible book.",       # negative sentence with booster words
    #     "At least it isn't a horrible book.", # negated negative sentence with contraction
    #     ":) and :D",     # emoticons handled
    #     "",              # an empty string is correctly handled
    #     "Today sux",     #  negative slang handled
    #     "Today sux!",    #  negative slang with punctuation emphasis handled
    #     "Today SUX!",    #  negative slang with capitalization emphasis
    #     "Today kinda sux! But I'll get by, lol" # mixed sentiment example with slang and constrastive conjunction "but"
    # ]
    #
    # tricky_sentences = [
    #     "Most automated sentiment analysis tools are shit.",
    #     "VADER sentiment analysis is the shit.",
    #     "Sentiment analysis has never been good.",
    #     "Sentiment analysis with VADER has never been this good.",
    #     "Warren Beatty has never been so entertaining.",
    #     "I won't say that the movie is astounding and I wouldn't claim that \
    #     the movie is too banal either.",
    #     "I like to hate Michael Bay films, but I couldn't fault this one",
    #     "It's one thing to watch an Uwe Boll film, but another thing entirely \
    #     to pay for it",
    #     "The movie was too good",
    #     "This movie was actually neither that funny, nor super witty.",
    #     "This movie doesn't care about cleverness, wit or any other kind of \
    #     intelligent humor.",
    #     "Those who find ugly meanings in beautiful things are corrupt without \
    #     being charming.",
    #     "There are slow and repetitive parts, BUT it has just enough spice to \
    #     keep it interesting.",
    #     "The script is not fantastic, but the acting is decent and the cinematography \
    #     is EXCELLENT!",
    #     "Roger Dodger is one of the most compelling variations on this theme.",
    #     "Roger Dodger is one of the least compelling variations on this theme.",
    #     "Roger Dodger is at least compelling as a variation on the theme.",
    #     "they fall in love with the product",
    #     "but then it breaks",
    #     "usually around the time the 90 day warranty expires",
    #     "the twin towers collapsed today",
    #     "However, Mr. Carter solemnly argues, his client carried out the kidnapping \
    #     under orders and in the ''least offensive way possible.''"
    #  ]
    # sentences.extend(tricky_sentences)

    polarityCalc = SentimentIntensityAnalyzer()
    return polarityCalc.polarity_scores(message)



    # {'neu': 0.465, 'pos': 0.0, 'neg': 0.535, 'compound': -0.3182}

    # for sentence in sentences:
    #     print(sentence)
    #     ss = sid.polarity_scores(sentence)
    #     for k in sorted(ss):
    #         print('{0}: {1}, '.format(k, ss[k]), end='')
