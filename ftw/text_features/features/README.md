# Features

String Features (32 features)

- n_words: Number of words.
- n_uq_word: Number of unique words.
- n_chars: Number of characters.
- n_uq_chars: Number of unique characters.
- n_digits: Number of digits.
- n_uq_digits: Number of unique digits.
- n_numbers: Number of numbers.
- n_uq_numbers: Number of unique numbers.
- n_hashtags: Number of hashtags.
- n_uq_hashtags: Number of unique hashtags.
- n_mentions: Number of mentions.
- n_uq_mentions: Number of unique mentions.
- n_commas: Number of commas.
- n_periods: Number of periods.
- n_exclaims: Number of exclamation points.
- n_extraspaces: Number of times more then 1 consecutive space have been used.
- n_uppers: Number of upper case characters.
- n_uq_uppers: Number of unique upper case characters.
- n_lowers: Number of lower case characters.
- n_uq_lowers: Number of unique lower case characters.
- n_emojis: Number of emojis.
- n_uq_emojis: Number of unique emojis.
- n_urls: Number of urls.
- n_uq_urls: Number of unique urls.
- n_nonasciis: Number of non ascii characters.
- n_uq_nonasciis: Number of unique non ascii characters.
- n_punctuations: Number of punctuations characters.
- n_uq_punctuations: Number of unique punctuations characters.
- ratio_lowers_chars: Ratio of lower case characters to all characters.
- ratio_uppers_chars: Ratio of upper case characters to all characters.
- ratio_digits_chars: Ratio of digits to all characters.
- ratio_chars_words: Ratio of all characters to all words.

Part of Speech (POS) Features (14 features)

- n_first_person: Number of first person pronouns.
- n_uq_first_person: Number of unique first person pronouns.
- n_first_personp: Number of first person plural pronouns.
- n_uq_first_personp: Number of unique first person plural pronouns.
- n_second_person: Number of second person pronouns.
- n_uq_second_person: Number of unique second person pronouns.
- n_second_personp: Number of second person plural pronouns.
- n_uq_second_personp: Number of unique second person plural pronouns.
- n_third_person: Number of third person pronouns.
- n_uq_third_person: Number of unique third person pronouns.
- n_tobe: Number of "to be".
- n_uq_tobe: Number of unique "to be".
- n_prepositions: Number of first person pronouns.
- n_uq_prepositions: Number of unique prepositions.

Sentiment Features (5 features)

- sent_afinn: Sentiment score, calculated by afinn method
- sent_bing: Sentiment score, calculated by bing method
- sent_syuzhet: Sentiment score, calculated by syuzhet method
- sent_vader: Sentiment score, calculated by vader method
- sent_politiness: Politiness score, (calculated by ? method)

Word2Vec Features (n feature)

- Features with LDA (TODO)


# Reproduce

- TextFeatures R package (TODO)