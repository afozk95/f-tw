from .utils import UserMetadata


def f_screen_name(metadata: UserMetadata) -> str:
    return metadata.get_usermetadata_attr("screen_name", "")


def f_description(metadata: UserMetadata) -> str:
    return metadata.get_usermetadata_attr("description", "")


def f_name(metadata: UserMetadata) -> str:
    return metadata.get_usermetadata_attr("name", "")


def f_statuses_count(metadata: UserMetadata) -> int:
    return metadata.get_usermetadata_attr("statuses_count", 0)


def f_followers_count(metadata: UserMetadata) -> int:
    return metadata.get_usermetadata_attr("followers_count", 0)


def f_friends_count(metadata: UserMetadata) -> int:
    return metadata.get_usermetadata_attr("friends_count", 0)


def f_favourites_count(metadata: UserMetadata) -> int:
    return metadata.get_usermetadata_attr("favourites_count", 0)


def f_listed_count(metadata: UserMetadata) -> int:
    return metadata.get_usermetadata_attr("listed_count", 0)


def f_is_default_profile(metadata: UserMetadata) -> bool:
    return metadata.get_usermetadata_attr("default_profile", False)


def f_is_default_profile_image(metadata: UserMetadata) -> bool:
    return metadata.get_usermetadata_attr("is_default_profile_image", False)


def f_is_profile_use_background_image(metadata: UserMetadata) -> bool:
    return metadata.get_usermetadata_attr("profile_use_background_image", False)


def f_is_verified(metadata: UserMetadata) -> bool:
    return metadata.get_usermetadata_attr("verified", False)


def f_is_protected(metadata: UserMetadata) -> bool:
    return metadata.get_usermetadata_attr("protected", False)


def f_tweet_freq(metadata: UserMetadata) -> float:
    return f_statuses_count(metadata) / metadata.account_age


def f_followers_growth_rate(metadata: UserMetadata) -> float:
    return f_followers_count(metadata) / metadata.account_age


def f_friends_growth_rate(metadata: UserMetadata) -> float:
    return f_friends_count(metadata) / metadata.account_age


def f_favourites_growth_rate(metadata: UserMetadata) -> float:
    return f_favourites_count(metadata) / metadata.account_age


def f_listed_growth_rate(metadata: UserMetadata) -> float:
    return f_listed_count(metadata) / metadata.account_age


def f_followers_friends_ratio(metadata: UserMetadata) -> float:
    return f_followers_count(metadata) / max(1, f_friends_count(metadata))


def f_screen_name_length(metadata: UserMetadata) -> int:
    return len(metadata.get_usermetadata_attr("screen_name", ""))


def f_num_digits_in_screen_name(metadata: UserMetadata) -> int:
    return sum(map(str.isdigit, metadata.get_usermetadata_attr("screen_name", "")))


def f_name_length(metadata: UserMetadata) -> int:
    return len(metadata.get_usermetadata_attr("name", ""))


def f_num_digits_in_name(metadata: UserMetadata) -> int:
    return sum(map(str.isdigit, metadata.get_usermetadata_attr("name", "")))


def f_description_length(metadata: UserMetadata) -> int:
    return len(metadata.get_usermetadata_attr("description", ""))


def f_account_age_in_days(metadata: UserMetadata) -> float:
    return metadata.get_account_age(time_frame="day")


def f_has_description(metadata: UserMetadata) -> bool:
    description = metadata.get_usermetadata_attr("description", None)
    return isinstance(description, str) and len(description) > 0


def f_has_location(metadata: UserMetadata) -> bool:
    location = metadata.get_usermetadata_attr("location", None)
    return isinstance(location, str) and len(location) > 0


def f_has_url(metadata: UserMetadata) -> bool:
    url = metadata.get_usermetadata_attr("url", None)
    return isinstance(url, str) and len(url) > 0


def f_has_profile_banner_url(metadata: UserMetadata) -> bool:
    profile_banner_url = metadata.get_usermetadata_attr("profile_banner_url", None)
    return isinstance(profile_banner_url, str) and len(profile_banner_url) > 0


def f_has_profile_background_image_url(metadata: UserMetadata) -> bool:
    profile_background_image_url = metadata.get_usermetadata_attr("profile_background_image_url", None)
    return isinstance(profile_background_image_url, str) and len(profile_background_image_url) > 0


FUNCS = {
    "screen_name": f_screen_name,
    "description": f_description,
    "name": f_name,
    "statuses_count": f_statuses_count,
    "followers_count": f_followers_count,
    "friends_count": f_friends_count,
    "favourites_count": f_favourites_count,
    "listed_count": f_listed_count,
    "is_default_profile": f_is_default_profile,
    "is_default_profile_image": f_is_default_profile_image,
    "is_profile_use_background_image": f_is_profile_use_background_image,
    "is_verified": f_is_verified,
    "is_protected": f_is_protected,
    "tweet_freq": f_tweet_freq,
    "followers_growth_rate": f_followers_growth_rate,
    "friends_growth_rate": f_friends_growth_rate,
    "favourites_growth_rate": f_favourites_growth_rate,
    "listed_growth_rate": f_listed_growth_rate,
    "followers_friends_ratio": f_followers_friends_ratio,
    "screen_name_length": f_screen_name_length,
    "num_digits_in_screen_name": f_num_digits_in_screen_name,
    "name_length": f_name_length,
    "num_digits_in_name": f_num_digits_in_name,
    "description_length": f_description_length,
    "account_age_in_days": f_account_age_in_days,
    "has_description": f_has_description,
    "has_location": f_has_location,
    "has_url": f_has_url,
    "has_profile_banner_url": f_has_profile_banner_url,
    "has_profile_background_image_url": f_has_profile_background_image_url,
}
