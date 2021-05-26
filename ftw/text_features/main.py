from features import get_all_text_features_in_bulk_df

inputs = [
    "this is A!\t sEntence https://github.com about #rstats @github",
    "and another sentence here",
    "THe following list:\n- one\n- two\n- three\nOkay!?!",
]

df = get_all_text_features_in_bulk_df(
    inputs,
    pos=True,
    sentiment=True,
    word_dims=None,
    verbose=True,
)

print(df)
