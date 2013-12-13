__author__ = 'stafi'
import chess, strategy

def n_test1_check_bishop_place_allowed():
    size_x = 5
    size_y = 5
    brd = chess.create_empty_board(size_y, size_y)
    brd[0][0] = "Q"
    return strategy.check_bishop_place_allowed(brd, 2, 2, size_x, size_y)

def n_test2_check_bishop_place_allowed():
    size_x = 4
    size_y = 4
    brd = chess.create_empty_board(size_y, size_y)
    brd[0][0] = "Q"
    return strategy.check_bishop_place_allowed(brd, 2, 2, size_x, size_y)

def p_test1_check_bishop_place_allowed():
    size_x = 4
    size_y = 4
    brd = chess.create_empty_board(size_y, size_y)
    brd[0][2] = "Q"
    return strategy.check_bishop_place_allowed(brd, 2, 2, size_x, size_y)

def n_test3_check_bishop_place_allowed():
    size_x = 5
    size_y = 5
    brd = chess.create_empty_board(size_y, size_y)
    brd[0][2] = "Q"
    return strategy.check_bishop_place_allowed(brd, 1, 3, size_x, size_y)

def bishop_strategy_tests():
    assert n_test1_check_bishop_place_allowed() == 0
    assert n_test2_check_bishop_place_allowed() == 0
    assert p_test1_check_bishop_place_allowed() == 1
    assert n_test3_check_bishop_place_allowed() == 0

bishop_strategy_tests