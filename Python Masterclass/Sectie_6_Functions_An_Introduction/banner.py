def banner_text(text: str = " ", screen_width: int = 80) -> None:
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Nothing will come from nothing, ya know what they say")
banner_text("Cheer up ya old bugga c'mon give us a grin")
banner_text("There ya are, see")
banner_text("It's the end of the film")
banner_text("Incidentally this record's available in the foyer")
banner_text(screen_width=80)
banner_text("Some of us got to live as well, you know")
banner_text("(Always look on the right side of life)")
banner_text("Who do you think pays for all this rubbish")
banner_text("(Always look on the right side of life)")
banner_text("They're not gonna make their money back, you know")
banner_text("*")
