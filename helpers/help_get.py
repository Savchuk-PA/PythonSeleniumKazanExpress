def get_num_in_str(text: str):
    arr = []
    for i in text:
        if i.isdigit():
            arr.append(i)
    return "".join(arr)