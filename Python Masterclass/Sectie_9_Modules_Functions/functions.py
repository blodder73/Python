def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' ', end_char='\n', centered_file=None, flush_me=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end_char, file=centered_file, flush=flush_me)


# call the function
center_text("Spam and eggs")
center_text("Spam, spam and eggs")
center_text(12)
center_text("Spam, spam, spam, spam and eggs")
center_text("first", "second", 3, 4, "spam", sep=';')
