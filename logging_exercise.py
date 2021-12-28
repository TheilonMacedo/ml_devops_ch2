import logging

logging.basicConfig(filename='results.log', level=logging.DEBUG)


def sum_vals(first_num, second_num):
    '''
    Args:
        first_num: (int or float)
        second_num: (int or float)
    Return:
        sum_result (float)
    '''
    try:
        first_num = float(first_num)
        second_num = float(second_num)
        sum_result = first_num + second_num
        logging.info('SUCESS: Both args are numbers')
        return sum_result
    except ValueError:
        logging.error('ERROR: At least one arg is not a number')
        return None


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
