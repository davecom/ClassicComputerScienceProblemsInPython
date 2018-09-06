# wine_test.py
# From Classic Computer Science Problems in Python Chapter 7
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
import csv
from typing import List
from util import normalize_by_feature_scaling
from network import Network
from random import shuffle

if __name__ == "__main__":
    wine_parameters: List[List[float]] = []
    wine_classifications: List[List[float]] = []
    wine_species: List[int] = []
    with open('wine.csv', mode='r') as wine_file:
        wines: List = list(csv.reader(wine_file, quoting=csv.QUOTE_NONNUMERIC))
        shuffle(wines) # get our lines of data in random order
        for wine in wines:
            parameters: List[float] = [float(n) for n in wine[1:14]]
            wine_parameters.append(parameters)
            species: int = int(wine[0])
            if species == 1:
                wine_classifications.append([1.0, 0.0, 0.0])
            elif species == 2:
                wine_classifications.append([0.0, 1.0, 0.0])
            else:
                wine_classifications.append([0.0, 0.0, 1.0])
            wine_species.append(species)
    normalize_by_feature_scaling(wine_parameters)

    wine_network: Network = Network([13, 7, 3], 0.9)

    def wine_interpret_output(output: List[float]) -> int:
        if max(output) == output[0]:
            return 1
        elif max(output) == output[1]:
            return 2
        else:
            return 3

    # train over the first 150 wines 10 times
    wine_trainers: List[List[float]] = wine_parameters[0:150]
    wine_trainers_corrects: List[List[float]] = wine_classifications[0:150]
    for _ in range(10):
        wine_network.train(wine_trainers, wine_trainers_corrects)

    # test over the last 28 of the wines in the data set
    wine_testers: List[List[float]] = wine_parameters[150:178]
    wine_testers_corrects: List[int] = wine_species[150:178]
    wine_results = wine_network.validate(wine_testers, wine_testers_corrects, wine_interpret_output)
    print(f"{wine_results[0]} correct of {wine_results[1]} = {wine_results[2] * 100}%")


