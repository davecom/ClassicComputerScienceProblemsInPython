# governors.py
# From Classic Computer Science Problems in Python Chapter 6
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
from data_point import DataPoint
from kmeans import KMeans


class Governor(DataPoint):
    def __init__(self, longitude: float, age: float, state: str) -> None:
        super().__init__([longitude, age])
        self.longitude = longitude
        self.age = age
        self.state = state

    def __repr__(self) -> str:
        return f"{self.state}: (longitude: {self.longitude}, age: {self.age})"


if __name__ == "__main__":
    governors: List[Governor] = [Governor(-86.79113, 72, "Alabama"), Governor(-152.404419, 66, "Alaska"),
                 Governor(-111.431221, 53, "Arizona"), Governor(-92.373123, 66, "Arkansas"),
                 Governor(-119.681564, 79, "California"), Governor(-105.311104, 65, "Colorado"),
                 Governor(-72.755371, 61, "Connecticut"), Governor(-75.507141, 61, "Delaware"),
                 Governor(-81.686783, 64, "Florida"), Governor(-83.643074, 74, "Georgia"),
                 Governor(-157.498337, 60, "Hawaii"), Governor(-114.478828, 75, "Idaho"),
                 Governor(-88.986137, 60, "Illinois"), Governor(-86.258278, 49, "Indiana"),
                 Governor(-93.210526, 57, "Iowa"), Governor(-96.726486, 60, "Kansas"),
                 Governor(-84.670067, 50, "Kentucky"), Governor(-91.867805, 50, "Louisiana"),
                 Governor(-69.381927, 68, "Maine"), Governor(-76.802101, 61, "Maryland"),
                 Governor(-71.530106, 60, "Massachusetts"), Governor(-84.536095, 58, "Michigan"),
                 Governor(-93.900192, 70, "Minnesota"), Governor(-89.678696, 62, "Mississippi"),
                 Governor(-92.288368, 43, "Missouri"), Governor(-110.454353, 51, "Montana"),
                 Governor(-98.268082, 52, "Nebraska"), Governor(-117.055374, 53, "Nevada"),
                 Governor(-71.563896, 42, "New Hampshire"), Governor(-74.521011, 54, "New Jersey"),
                 Governor(-106.248482, 57, "New Mexico"), Governor(-74.948051, 59, "New York"),
                 Governor(-79.806419, 60, "North Carolina"), Governor(-99.784012, 60, "North Dakota"),
                 Governor(-82.764915, 65, "Ohio"), Governor(-96.928917, 62, "Oklahoma"),
                 Governor(-122.070938, 56, "Oregon"), Governor(-77.209755, 68, "Pennsylvania"),
                 Governor(-71.51178, 46, "Rhode Island"), Governor(-80.945007, 70, "South Carolina"),
                 Governor(-99.438828, 64, "South Dakota"), Governor(-86.692345, 58, "Tennessee"),
                 Governor(-97.563461, 59, "Texas"), Governor(-111.862434, 70, "Utah"),
                 Governor(-72.710686, 58, "Vermont"), Governor(-78.169968, 60, "Virginia"),
                 Governor(-121.490494, 66, "Washington"), Governor(-80.954453, 66, "West Virginia"),
                 Governor(-89.616508, 49, "Wisconsin"), Governor(-107.30249, 55, "Wyoming")]
    kmeans: KMeans[Governor] = KMeans(2, governors)
    gov_clusters: List[KMeans.Cluster] = kmeans.run()
    for index, cluster in enumerate(gov_clusters):
        print(f"Cluster {index}: {cluster.points}\n")
