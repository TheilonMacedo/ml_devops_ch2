'''
Exercise with testing, logging, and assertions

Author: Theilon Macêdo
Date: 2021-12-27

'''

import logging

logging.basicConfig(
    filename='test_results.log',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(levelname)s: %(message)s'
)


def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        assert denominator != 0
        assert isinstance(numerator, float)
        assert isinstance(denominator, float)
        fraction_val = numerator / denominator
        logging.info(
            'SUCCESS: Denominator is not zero and both values are floats')
        return fraction_val
    except AssertionError:
        logging.error(
            'ERROR: Denominator is zero or one of the values is not a float')


def word_count(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        assert isinstance(text, str)
        num_words = len(text.split())
        logging.info('SUCCESS: Text is a string')
        return num_words
    except AssertionError:
        logging.error('ERROR: Text is not a string')


if __name__ == "__main__":
    divide_vals(3.4, 0)
    divide_vals(4.5, 2.7)
    divide_vals(-3.8, 2.1)
    divide_vals(1, 2)
    word_count(5)
    word_count('This is the best string')
    word_count('one')
