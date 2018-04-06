#!/bin/python

import random

fortune = ['Good things are being said about you',
'Your charm has inspired a secret admirer',
'Put up with small annoyances to gain great results',
'Share your happiness with others today',
'Good news will come to you by mail',
'Advice given to you will be well worth following',
'A romantic mystery will add interest to your life',
'At this moment, someone is thinking good thoughts of you',
'New finacial resources will soon become available to you',
'If given a penny for every kind act, you\'d be a millionaire',
'Be cautious in your financial dealings',
'You set your sights high, and enjoy striving for the best things in life',
'How you look depends on where you go',
'The road before you is long. Drive safely',
'You are only starting on your path to success',
'You are compassionate and fun-loving.',
'Many possibilities are open to you - work a little harder',
'You are a classic',
'The strengths in your character wil bring you serenity',
'There is much to be learned by listening to others',
'You are bright and witty',
'Your dearest wish will come true',
'Any doubts you have will soon disappear',
'Look in the right places and you will find good fortune',
'You will inherit a large sum of money',
'You will soon receive help from an unexpected source',
'Someone from your past will happily re-enter your life soon',
'Many people are seeking you for your sound advice',
'Learn to broaden your horizons, day by day',
'A friend will soon bring you a gift',
'Happiness is a direction, not a destination',
'Revel in the spotlight',
'You will soon honored by someone you respect',
'If you want something, you must earn it',
'You will overcome difficult times',
'Your mind is creative, original, and alert',
'Past inspirations and experiences will be helpful in your job',
'Share joy',
'You are an artist - let your colors show',
'Your opportunities are many',
'Versatility is one of your outstanding traits',
'Your good nature will bring you happiness',
'Everything will soon come your way',
'Avenues of good fortune are ahead for you',
'You may have a fantastic opportunity soon - be open to it',
'Your golden years will be happy and fulfilling',
'People in your background will be more cooperative than usual',
'You are humorous and cheerful with good friends',
'Your ability to love will help a child in need',
'You have the ability to excel in untried areas',
'You will find hidden treasures where least expected',
'Now is the time to set your sights high and go for it',
'You desire to discover new frontiers. It\'s time to travel',
'Now is the time to fulfill your dream of traveling abroad',
'Be tactful: Do not overlook your own opportunities',
'Now is a good time to try something new',
'Don\'t be tempted by shortcuts - They\'re never worth it in the end',
'Work on ideas that are creative and can bring fine results',
'It is best to consult others before taking unusual actions',
'You are able to do what others say you can\'t do',
'Wise man is slow in choosing friends, slower in changing',
'Everyone feels lucky for having you as a friend',
'A partner can help you in your efforts to get ahead',
'Your careful nature will bring you financial success',
'There will always be delightful mysteries in your life',
'Avoid unchallenging occupations - they waste your talents',
'A partnership shall prove successful for you',
'Trust others, but not blindly',
'Before an evening of romance, turn off the cell phone',
'You will make many changes before happily settling',
'You will place your trust in others and be rewarded',
'A friend\'s advice is invaluable',
'Yes. Do it with confidence',
'This is a prosperous time of life for you',
'You are refreshingly levelheaded and others can relate to you',
'Lavish spending may be disasterous - be careful',
'Nurture your passions',
'You have the makings of a leader - take charge',
'If your dreams don\'t scare you, they are not big enough',
'Your kindness will find new homes this year',
'Seek friendship and you will find it',
'Hold tight to your dreams',
'Any troubles you may have will pass very shortly',
'Age is a matter of feelings, not years',
'You will soon find new adventure in life',
'An admirer is concealing affection for you',
'You will soon change your present line of work',
'Go confidently in the direction of your dreams',
'The skies above will rain success onto you',
'Your difficult path will be rewarding',
'Give your business interests top priority next month',
'When in doubt, let your instincts guide you',
'Following inner promptings brings quiet accomplishment',
'Impulsiveness where money is concerned, is not your style',
'Indulge your ambitious nature',
'There is a gradual improvement. Feelings are sweet and tender',
'Opportunity knocks on your door every day - answer it',
'From error to error, one discovers the entire truth',
'Your dreams will become a reality',
'Luck will soon come your way',
'Take that chance you\'ve been considering',
'The sky\'s the limit this month',
'A long time admirer thinks highly of you',
'I am fortunate for: _______________',
'Soon, a visitor shall delight you',
'You thrive on adventure, try something new',
'You would be wise not to seek too much from others',
'An unexpected event will soon make your life more exciting',
'Don\'t waste time on what might have been',
'You will be showered with good luck',
'Prosperity will soon knock on your door']

print(fortune[random.randint(0, len(fortune))])