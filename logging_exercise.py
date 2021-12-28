'''
Exercises of logging, testing and debugging

Author: Theilon Macêdo
Date: 2021-12-27
'''


import logging

logging.basicConfig(
    filename='logging_exercise.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s: %(message)s'
)


def sum_vals(first_num, second_num):
    '''
    Args:
        first_num: (int)
        second_num: (int)
    Return:
        sum_result (int)
    '''
    try:
        logging.info(first_num, second_num)
        assert isinstance(first_num, int)
        assert isinstance(second_num, int)
        logging.info('SUCESS: Both args are numbers')
        return first_num + second_num
    except AssertionError:
        logging.error('ERROR: At least one arg is not a number')


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
