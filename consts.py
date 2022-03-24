# block width: 25px
# block height: 25px

# Grass pixel 1 = (162, 209, 73)
# Grass pixel 2 = (185, 221, 119)

# Flag = (242, 54, 7)

START_X = 665
START_Y = 370

MAX_X = 1255
MAX_Y = 745

GRASS = set({(162, 209, 73), (185, 221, 119), (191, 225, 125), (170, 215, 81)})

IGNORE = set(
    {
        (162, 209, 73),
        (185, 221, 119),
        (191, 225, 125),
        (170, 215, 81),
        (215, 184, 153),
        (229, 194, 159),
        (242, 54, 7),
    }
)

DIRT = set({(215, 184, 153), (229, 194, 159), (242, 54, 7)})

FLAG_COLORS = set({(242, 54, 7), (230, 51, 7)})

FLAG = (242, 54, 7)
FLAG_POLE = (230, 51, 7)

COLORS = {
    (25, 118, 210): 1,
    (56, 142, 60): 2,
    (211, 47, 47): 3,
    (123, 31, 162): 4,
    (255, 143, 0): 5,
    (0, 151, 167): 6,
    (65, 65, 65): 7,
    (158, 158, 158): 8,
}

ALL_GAME_COLORS = set(
    {
        (162, 209, 73),
        (185, 221, 119),
        (191, 225, 125),
        (170, 215, 81),
        (215, 184, 153),
        (229, 194, 159),
        (242, 54, 7),
        (25, 118, 210),
        (56, 142, 60),
        (211, 47, 47),
        (123, 31, 162),
        (255, 143, 0),
        (0, 151, 167),
        (65, 65, 65),
        (158, 158, 158),
        (242, 54, 7),
        (230, 51, 7),
    }
)

TO_SEARCH = [
    [-25, -25],
    [0, -25],
    [25, -25],
    [-25, 0],
    [25, 0],
    [-25, 25],
    [0, 25],
    [25, 25],
]

TILES = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0],
    [8, 0],
    [9, 0],
    [10, 0],
    [11, 0],
    [12, 0],
    [13, 0],
    [14, 0],
    [15, 0],
    [16, 0],
    [17, 0],
    [18, 0],
    [19, 0],
    [20, 0],
    [21, 0],
    [22, 0],
    [0, 1],
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
    [5, 1],
    [6, 1],
    [7, 1],
    [8, 1],
    [9, 1],
    [10, 1],
    [11, 1],
    [12, 1],
    [13, 1],
    [14, 1],
    [15, 1],
    [16, 1],
    [17, 1],
    [18, 1],
    [19, 1],
    [20, 1],
    [21, 1],
    [22, 1],
    [0, 2],
    [1, 2],
    [2, 2],
    [3, 2],
    [4, 2],
    [5, 2],
    [6, 2],
    [7, 2],
    [8, 2],
    [9, 2],
    [10, 2],
    [11, 2],
    [12, 2],
    [13, 2],
    [14, 2],
    [15, 2],
    [16, 2],
    [17, 2],
    [18, 2],
    [19, 2],
    [20, 2],
    [21, 2],
    [22, 2],
    [0, 3],
    [1, 3],
    [2, 3],
    [3, 3],
    [4, 3],
    [5, 3],
    [6, 3],
    [7, 3],
    [8, 3],
    [9, 3],
    [10, 3],
    [11, 3],
    [12, 3],
    [13, 3],
    [14, 3],
    [15, 3],
    [16, 3],
    [17, 3],
    [18, 3],
    [19, 3],
    [20, 3],
    [21, 3],
    [22, 3],
    [0, 4],
    [1, 4],
    [2, 4],
    [3, 4],
    [4, 4],
    [5, 4],
    [6, 4],
    [7, 4],
    [8, 4],
    [9, 4],
    [10, 4],
    [11, 4],
    [12, 4],
    [13, 4],
    [14, 4],
    [15, 4],
    [16, 4],
    [17, 4],
    [18, 4],
    [19, 4],
    [20, 4],
    [21, 4],
    [22, 4],
    [0, 5],
    [1, 5],
    [2, 5],
    [3, 5],
    [4, 5],
    [5, 5],
    [6, 5],
    [7, 5],
    [8, 5],
    [9, 5],
    [10, 5],
    [11, 5],
    [12, 5],
    [13, 5],
    [14, 5],
    [15, 5],
    [16, 5],
    [17, 5],
    [18, 5],
    [19, 5],
    [20, 5],
    [21, 5],
    [22, 5],
    [0, 6],
    [1, 6],
    [2, 6],
    [3, 6],
    [4, 6],
    [5, 6],
    [6, 6],
    [7, 6],
    [8, 6],
    [9, 6],
    [10, 6],
    [11, 6],
    [12, 6],
    [13, 6],
    [14, 6],
    [15, 6],
    [16, 6],
    [17, 6],
    [18, 6],
    [19, 6],
    [20, 6],
    [21, 6],
    [22, 6],
    [0, 7],
    [1, 7],
    [2, 7],
    [3, 7],
    [4, 7],
    [5, 7],
    [6, 7],
    [7, 7],
    [8, 7],
    [9, 7],
    [10, 7],
    [11, 7],
    [12, 7],
    [13, 7],
    [14, 7],
    [15, 7],
    [16, 7],
    [17, 7],
    [18, 7],
    [19, 7],
    [20, 7],
    [21, 7],
    [22, 7],
    [0, 8],
    [1, 8],
    [2, 8],
    [3, 8],
    [4, 8],
    [5, 8],
    [6, 8],
    [7, 8],
    [8, 8],
    [9, 8],
    [10, 8],
    [11, 8],
    [12, 8],
    [13, 8],
    [14, 8],
    [15, 8],
    [16, 8],
    [17, 8],
    [18, 8],
    [19, 8],
    [20, 8],
    [21, 8],
    [22, 8],
    [0, 9],
    [1, 9],
    [2, 9],
    [3, 9],
    [4, 9],
    [5, 9],
    [6, 9],
    [7, 9],
    [8, 9],
    [9, 9],
    [10, 9],
    [11, 9],
    [12, 9],
    [13, 9],
    [14, 9],
    [15, 9],
    [16, 9],
    [17, 9],
    [18, 9],
    [19, 9],
    [20, 9],
    [21, 9],
    [22, 9],
    [0, 10],
    [1, 10],
    [2, 10],
    [3, 10],
    [4, 10],
    [5, 10],
    [6, 10],
    [7, 10],
    [8, 10],
    [9, 10],
    [10, 10],
    [11, 10],
    [12, 10],
    [13, 10],
    [14, 10],
    [15, 10],
    [16, 10],
    [17, 10],
    [18, 10],
    [19, 10],
    [20, 10],
    [21, 10],
    [22, 10],
    [0, 11],
    [1, 11],
    [2, 11],
    [3, 11],
    [4, 11],
    [5, 11],
    [6, 11],
    [7, 11],
    [8, 11],
    [9, 11],
    [10, 11],
    [11, 11],
    [12, 11],
    [13, 11],
    [14, 11],
    [15, 11],
    [16, 11],
    [17, 11],
    [18, 11],
    [19, 11],
    [20, 11],
    [21, 11],
    [22, 11],
    [0, 12],
    [1, 12],
    [2, 12],
    [3, 12],
    [4, 12],
    [5, 12],
    [6, 12],
    [7, 12],
    [8, 12],
    [9, 12],
    [10, 12],
    [11, 12],
    [12, 12],
    [13, 12],
    [14, 12],
    [15, 12],
    [16, 12],
    [17, 12],
    [18, 12],
    [19, 12],
    [20, 12],
    [21, 12],
    [22, 12],
    [0, 13],
    [1, 13],
    [2, 13],
    [3, 13],
    [4, 13],
    [5, 13],
    [6, 13],
    [7, 13],
    [8, 13],
    [9, 13],
    [10, 13],
    [11, 13],
    [12, 13],
    [13, 13],
    [14, 13],
    [15, 13],
    [16, 13],
    [17, 13],
    [18, 13],
    [19, 13],
    [20, 13],
    [21, 13],
    [22, 13],
    [0, 14],
    [1, 14],
    [2, 14],
    [3, 14],
    [4, 14],
    [5, 14],
    [6, 14],
    [7, 14],
    [8, 14],
    [9, 14],
    [10, 14],
    [11, 14],
    [12, 14],
    [13, 14],
    [14, 14],
    [15, 14],
    [16, 14],
    [17, 14],
    [18, 14],
    [19, 14],
    [20, 14],
    [21, 14],
    [22, 14],
    [0, 15],
    [1, 15],
    [2, 15],
    [3, 15],
    [4, 15],
    [5, 15],
    [6, 15],
    [7, 15],
    [8, 15],
    [9, 15],
    [10, 15],
    [11, 15],
    [12, 15],
    [13, 15],
    [14, 15],
    [15, 15],
    [16, 15],
    [17, 15],
    [18, 15],
    [19, 15],
    [20, 15],
    [21, 15],
    [22, 15],
    [0, 16],
    [1, 16],
    [2, 16],
    [3, 16],
    [4, 16],
    [5, 16],
    [6, 16],
    [7, 16],
    [8, 16],
    [9, 16],
    [10, 16],
    [11, 16],
    [12, 16],
    [13, 16],
    [14, 16],
    [15, 16],
    [16, 16],
    [17, 16],
    [18, 16],
    [19, 16],
    [20, 16],
    [21, 16],
    [22, 16],
    [0, 17],
    [1, 17],
    [2, 17],
    [3, 17],
    [4, 17],
    [5, 17],
    [6, 17],
    [7, 17],
    [8, 17],
    [9, 17],
    [10, 17],
    [11, 17],
    [12, 17],
    [13, 17],
    [14, 17],
    [15, 17],
    [16, 17],
    [17, 17],
    [18, 17],
    [19, 17],
    [20, 17],
    [21, 17],
    [22, 17],
    [0, 18],
    [1, 18],
    [2, 18],
    [3, 18],
    [4, 18],
    [5, 18],
    [6, 18],
    [7, 18],
    [8, 18],
    [9, 18],
    [10, 18],
    [11, 18],
    [12, 18],
    [13, 18],
    [14, 18],
    [15, 18],
    [16, 18],
    [17, 18],
    [18, 18],
    [19, 18],
    [20, 18],
    [21, 18],
    [22, 18],
    [0, 19],
    [1, 19],
    [2, 19],
    [3, 19],
    [4, 19],
    [5, 19],
    [6, 19],
    [7, 19],
    [8, 19],
    [9, 19],
    [10, 19],
    [11, 19],
    [12, 19],
    [13, 19],
    [14, 19],
    [15, 19],
    [16, 19],
    [17, 19],
    [18, 19],
    [19, 19],
    [20, 19],
    [21, 19],
    [22, 19],
]
