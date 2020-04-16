def parse_comments(text):
    out_text = ""
    open_comments = 0
    i = 0
    while i < len(text):
        if text[i] == '/' and i < len(text) - 1 and text[i + 1] == '*':
            open_comments += 1
            i += 2
            continue
        if text[i] == '*' and i < len(text) - 1 and text[i + 1] == '/' and open_comments > 0:
            open_comments -= 1
            i += 2
            continue
        if open_comments == 0:
            out_text += text[i]
        i += 1
    return out_text
