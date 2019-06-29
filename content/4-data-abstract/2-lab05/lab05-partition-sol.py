def partition_options(total, bignum):

    '''
    >>> partition_options(2, 1)
    [[1, 1]]
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    '''

    if total == 1:
        return [[1]]
    elif total <= 0:
        return [[]]
    elif bignum == 1:
        return [[1 for x in range(total)]]
    else:
        without_big = partition_options(total,bignum-1)
        with_big = partition_options(total-bignum,bignum)
        if with_big == [[]]:
            with_big = [[bignum]]
        else:
            with_big = [ele + [bignum] for ele in with_big]
    return with_big + without_big

print(partition_options(4, 3))