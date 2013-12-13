__author__ = 'stafi'
import chess, strategy

def king_positive_test():
    size_x = 5
    size_y = 5
    brd = chess.create_empty_board(size_y, size_y)
    brd[0][0] = "Q"
    return strategy.check_bishop_place_allowed(brd, 2, 2, size_x, size_y)

def king_strategy_tests():
    assert king_positive_test() == 1

king_strategy_tests