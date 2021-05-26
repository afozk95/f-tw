import emoji
import regex
import string


FIRST_PERSON = [
    "i",
    "me",
    "myself",
    "my",
    "mine",
    "this",
]

FIRST_PERSONP = [
    "we", "us", "our", "ours", "these"
]

SECOND_PERSON = [
    "you", "yours", "your", "yourself"
]

SECOND_PERSONP = [
    "he", "she", "it", "its", "his", "hers"
]

THIRD_PERSON = [
    "they", "them", "theirs", "their", "they're", "their's", "those", "that"
]

TOBE = [
    "am", "is", "are", "was", "were", "being", "been", "be", "were", "be"
]

PREPOSITION = [
    "about", "below", "excepting", "off", "toward", "above", "beneath",
    "on", "under", "across", "from", "onto", "underneath", "after", "between",
    "in", "out", "until", "against", "beyond", "outside", "up", "along", "but",
    "inside", "over", "upon", "among", "by", "past", "around", "concerning",
    "regarding", "with", "at", "despite", "into", "since", "within", "down",
    "like", "through", "without", "before", "during", "near", "throughout",
    "behind", "except", "of", "to", "for"
]

DIGIT_PATTERN = r"[0-9]"
NUMBER_PATTERN = r"[0-9]+"
HASHTAG_PATTERN = r"#\w+"
MENTION_PATTERN = r"@\w+"
COMMA_PATTERN = r","
PERIOD_PATTERN = r"\."
EXCLAIM_PATTERN = r"\!"
EXTRASPACE_PATTERN = r"\s{2}|\t|\n"
UPPER_PATTERN = r"[A-Z]"
LOWER_PATTERN = r"[a-z]"
EMOJI_PATTERN = r"|".join([regex.escape(x) for x in emoji.UNICODE_EMOJI])
URL_PATTERN = r"https?"
NONASCII_PATTERN = r"\\N{[\w\s_-]*}"
PUNCTUATION_PATTERN = r"|".join([regex.escape(x) for x in string.punctuation])

FIRST_PERSON_PATTERN = r"|".join([regex.escape(x) for x in FIRST_PERSON])
FIRST_PERSONP_PATTERN = r"|".join([regex.escape(x) for x in FIRST_PERSONP])
SECOND_PERSON_PATTERN = r"|".join([regex.escape(x) for x in SECOND_PERSON])
SECOND_PERSONP_PATTERN = r"|".join([regex.escape(x) for x in SECOND_PERSONP])
THIRD_PERSON_PATTERN = r"|".join([regex.escape(x) for x in THIRD_PERSON])
TOBE_PATTERN = r"|".join([regex.escape(x) for x in TOBE])
PREPOSITION_PATTERN = r"|".join([regex.escape(x) for x in PREPOSITION])
