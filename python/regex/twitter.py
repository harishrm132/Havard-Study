import re

url = input("URL: ").strip()

# username = re.sub("^(https?://)?(www\.)?twitter.com/", "", url)
# https://www.twitter.com/davidjmalan
# Validate, Cleanup and extarct data


if matches := re.search("^https?://(?:www\.)?twitter.com/(.+)$", url, re.IGNORECASE):
    print(matches.group(1))


