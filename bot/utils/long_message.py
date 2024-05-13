def long_message_control(text: str, max_length: int = 4096) -> list:
    splited_text = text.split()
    str_build = ''
    result = []
    for word in splited_text:
        if len(str_build + f' {word}') > max_length:
            result.append(str_build)
            str_build = ''
        else:
            str_build += f' {word}'
    result.append(str_build)
    return result
