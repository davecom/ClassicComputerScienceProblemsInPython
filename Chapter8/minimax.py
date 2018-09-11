# minimax.py
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
from board import Piece, Board, Move


# Find the best possible outcome for original player
def minimax(board: Board, maximizing: bool, original_player: Piece) -> float:
    # Base case - evaluate the position if it is a win or a draw
    if board.is_win or board.is_draw:
        return board.evaluate(original_player)

    # Recursive case - maximize your gains or minimize the opponent's gains
    if maximizing:
        best_eval: float = float("-inf") # arbitrarily low starting point
        for move in board.legal_moves:
            result: float = minimax(board.move(move), False, original_player)
            best_eval = max(result, best_eval)
        return best_eval
    else: # minimizing
        worst_eval: float = float("inf")
        for move in board.legal_moves:
            result = minimax(board.move(move), True, original_player)
            worst_eval = min(result, worst_eval)
        return worst_eval


# Run minimax() on every possible move to find the best one
def find_best_move(board: Board) -> Move:
    best_eval: float = float("-inf")
    best_move: Move = Move(-1)
    for move in board.legal_moves:
        result: float = minimax(board.move(move), False, board.turn)
        if result > best_eval:
            best_eval = result
            best_move = move
    return best_move