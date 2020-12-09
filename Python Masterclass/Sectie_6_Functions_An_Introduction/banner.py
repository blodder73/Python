def banner_text(text, screen_width):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 50)
banner_text("Nothing will come from nothing, ya know what they say", 80)
banner_text("Cheer up ya old bugga c'mon give us a grin", 80)
banner_text("There ya are, see", 80)
banner_text("It's the end of the film", 80)
banner_text("Incidentally this record's available in the foyer", 55)
banner_text(" ", 80)
banner_text("Some of us got to live as well, you know", 80)
banner_text("(Always look on the right side of life)", 80)
banner_text("Who do you think pays for all this rubbish", 80)
banner_text("(Always look on the right side of life)", 80)
banner_text("They're not gonna make their money back, you know", 80)
banner_text("*", 33)
