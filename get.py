def get(coll, index, default=None):
    if index >= len(coll) or index < 0:
        if default is not None:
            return default
        return None

    return coll[index]

if __name__ == '__main__':
    get(coll, index, default)