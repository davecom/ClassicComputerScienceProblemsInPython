# tictactoe.py
# From Classic Computer Science Problems in Python Chapter 8
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations
from typing import List
from dataclasses import dataclass
from enum import Enum
from board import Piece, Board, Move


class TTTPiece(Piece, Enum):
    X = "X"
    O = "O"
    E = "E" # stand-in for empty

    @property
    def opposite(self) -> Piece:
        if self == TTTPiece.X:
            return TTTPiece.O
        elif self == TTTPiece.O:
            return TTTPiece.X
        else:
            return TTTPiece.E


@dataclass(frozen=True)
class TTTBoard(Board):
    position: List[TTTPiece]
    my_turn: TTTPiece

    @property
    def turn(self) -> Piece:
        return self.my_turn

    def move(self, location: Move) -> Board:
        temp_position: List[TTTPiece] = self.position.copy()
        temp_position[location] = self.turn
        return TTTBoard(temp_position, self.turn.opposite)

    @property
    def legal_moves(self) -> List[Move]:
        return [Move(l) for l in range(len(self.position)) if self.position[l] == TTTPiece.E]

    @property
    def is_win(self) -> bool:
        # three row, three column, and then two diagonal checks
        return self.position[0] == self.position[1] and self.position[0] == self.position[2] and self.position[0] != TTTPiece.E or \
        self.position[3] == self.position[4] and self.position[3] == self.position[5] and self.position[3] != TTTPiece.E or \
        self.position[6] == self.position[7] and self.position[6] == self.position[8] and self.position[6] != TTTPiece.E or \
        self.position[0] == self.position[3] and self.position[0] == self.position[6] and self.position[0] != TTTPiece.E or \
        self.position[1] == self.position[4] and self.position[1] == self.position[7] and self.position[1] != TTTPiece.E or \
        self.position[2] == self.position[5] and self.position[2] == self.position[8] and self.position[2] != TTTPiece.E or \
        self.position[0] == self.position[4] and self.position[0] == self.position[8] and self.position[0] != TTTPiece.E or \
        self.position[2] == self.position[4] and self.position[2] == self.position[6] and self.position[2] != TTTPiece.E

    def evaluate(self, player: Piece) -> float:
        if self.is_win and self.turn == player:
            return -1
        elif self.is_win and self.turn != player:
            return 1
        else:
            return 0


if __name__ == "__main__":
    from minimax import find_best_move
    # win in 1 move
    to_win_easy_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.O, TTTPiece.X,
                                            TTTPiece.X, TTTPiece.E, TTTPiece.O,
                                            TTTPiece.E, TTTPiece.E, TTTPiece.O]
    test_board1: TTTBoard = TTTBoard(to_win_easy_position, TTTPiece.X)
    answer1: Move = find_best_move(test_board1)
    print(answer1)

    # must block O's win
    to_block_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                         TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                         TTTPiece.E, TTTPiece.X, TTTPiece.O]
    test_board2: TTTBoard = TTTBoard(to_block_position, TTTPiece.X)
    answer2: Move = find_best_move(test_board2)
    print(answer2)

    # find the best move to win 2 moves
    to_win_hard_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                            TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                            TTTPiece.O, TTTPiece.X, TTTPiece.E]
    test_board3: TTTBoard = TTTBoard(to_win_hard_position, TTTPiece.X)
    answer3: Move = find_best_move(test_board3)
    print(answer3)