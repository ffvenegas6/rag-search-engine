#!/usr/bin/env python3

import argparse
import json


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

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
            
            for movie in movies_list:
                title = movie["title"]
                if args.query in title:
                    results.append(title)

            for i, title in enumerate(results):
                print(f"{i}. {title}")
            
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
