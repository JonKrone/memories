from src import load_conversations


# 2. Parse conversations, build them into a simpler, less normalized format.
#   - can we do this in a lazy way?
# 3. Construct and run prompt to pluck out memories
#   - cache conversation <> query mappings
# 4. Group and deduplicate memories
#   - future: coalesce memories that are part of a whole


def main():
    print("Hello, world!")
    load_conversations("data/conversations.json")


if __name__ == "__main__":
    main()
