def count_candles(candle_number, make_new):
    total_burned = candle_number
    leftovers = candle_number

    while leftovers >= make_new:
        new_candles = leftovers // make_new
        total_burned += new_candles
        leftovers = new_candles + (leftovers % make_new)

    return total_burned
