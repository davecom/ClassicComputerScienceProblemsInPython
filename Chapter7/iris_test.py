# iris_test.py
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
    iris_parameters: List[List[float]] = []
    iris_classifications: List[List[float]] = []
    iris_species: List[str] = []
    with open('iris.csv', mode='r') as iris_file:
        irises: List = list(csv.reader(iris_file))
        shuffle(irises) # get our lines of data in random order
        for iris in irises:
            parameters: List[float] = [float(n) for n in iris[0:4]]
            iris_parameters.append(parameters)
            species: str = iris[4]
            if species == "Iris-setosa":
                iris_classifications.append([1.0, 0.0, 0.0])
            elif species == "Iris-versicolor":
                iris_classifications.append([0.0, 1.0, 0.0])
            else:
                iris_classifications.append([0.0, 0.0, 1.0])
            iris_species.append(species)
    normalize_by_feature_scaling(iris_parameters)

    iris_network: Network = Network([4, 6, 3], 0.3)

    def iris_interpret_output(output: List[float]) -> str:
        if max(output) == output[0]:
            return "Iris-setosa"
        elif max(output) == output[1]:
            return "Iris-versicolor"
        else:
            return "Iris-virginica"

    # train over the first 140 irises in the data set 50 times
    iris_trainers: List[List[float]] = iris_parameters[0:140]
    iris_trainers_corrects: List[List[float]] = iris_classifications[0:140]
    for _ in range(50):
        iris_network.train(iris_trainers, iris_trainers_corrects)

    # test over the last 10 of the irises in the data set
    iris_testers: List[List[float]] = iris_parameters[140:150]
    iris_testers_corrects: List[str] = iris_species[140:150]
    iris_results = iris_network.validate(iris_testers, iris_testers_corrects, iris_interpret_output)
    print(f"{iris_results[0]} correct of {iris_results[1]} = {iris_results[2] * 100}%")


