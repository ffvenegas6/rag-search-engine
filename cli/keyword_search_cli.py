#!/usr/bin/env python3

import argparse
import json
import string


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    with open("data/movies.json", "r", encoding="utf-8") as file:
        movies_dict: dict = json.load(file)

    movies_list: list = movies_dict["movies"]
    results = []
    trans_table = create_trans_table()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
            
            for movie in movies_list:
                title = movie["title"]
                query = args.query.lower().translate(trans_table)
                query_tokens = query.split()
                title_tokens = title.lower().translate(trans_table).split()
                for q_token in query_tokens:
                    for t_token in title_tokens:
                        if q_token in t_token:
                            results.append(title)
                            break

            for i, title in enumerate(results):
                print(f"{i}. {title}")

        case _:
            parser.print_help()

def create_trans_table():
    d = {}
    for char in string.punctuation:
        d[char] = ""
    return str.maketrans(d)


if __name__ == "__main__":
    main()
