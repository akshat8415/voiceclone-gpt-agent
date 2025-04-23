from tqdm import tqdm

def progbar(i, total):
    return tqdm(total=total, initial=i, ncols=70)

def simple_table(table):
    """
    Prints a formatted table of key-value pairs.
    """
    max_key_len = max(len(str(k)) for k, _ in table)
    for key, value in table:
        print(f"{key.ljust(max_key_len)} : {value}")

