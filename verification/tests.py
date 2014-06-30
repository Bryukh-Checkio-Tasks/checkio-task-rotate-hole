"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "1. Small": [
        {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [0, 1, 2]
            ],
            "answer": []
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [7, 3]
            ],
            "answer": [3, 8]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [4, 4, 9, 1, 9, 1, 2, 9, 4, 8, 4]
            ],
            "answer": [9]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [8, 9, 4, 9]
            ],
            "answer": [4, 9]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [4, 10, 6, 10]
            ],
            "answer": [11]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [2, 9]
            ],
            "answer": [
                2, 9, 10
            ]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [3]
            ],
            "answer": [3, 4, 8, 10, 11]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [10, 3, 3, 4, 6]
            ],
            "answer": [11]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [1, 9, 9]
            ],
            "answer": [
                2, 9
            ]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [3, 4, 10, 4]
            ],
            "answer": [
                11
            ]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [0, 1]
            ],
            "answer": [
                1, 8
            ]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [9, 2, 8, 8, 9, 4]
            ],
            "answer": [9]
        }, {
            "input": [
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [9, 9, 7, 7]
            ],
            "answer": [2]
        }
    ],
    "2. Medium": [
        {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [1, 4, 24, 25, 11, 7]
            ],
            "answer": [28]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [11, 24, 19]
            ],
            "answer": [12, 18, 29]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [19, 4, 20]
            ],
            "answer": [7, 14, 27]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [9, 5, 29, 24, 22, 15, 7, 25, 7, 27, 24, 7, 22, 28, 8, 29, 28, 8, 25, 18, 22, 8, 14]
            ],
            "answer": [2]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [19, 3, 2, 1, 9, 3, 11]
            ],
            "answer": [6]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [2, 8, 21, 7, 7, 17, 28, 1, 2, 24, 4, 0, 17, 20, 2, 17, 26, 24, 2, 22, 17, 8, 11, 22, 28, 4, 0, 2]
            ],
            "answer": [25]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [2, 17]
            ],
            "answer": [1, 5, 10, 12, 16, 20, 25, 27]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [13, 20, 5, 27, 13, 23, 13, 13, 12, 3, 25, 7, 3, 6, 1, 23, 6, 29, 1, 22]
            ],
            "answer": [0]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [24, 22, 8, 8, 8, 15, 19, 2, 6, 0, 28, 0, 2, 6, 25, 8, 4, 22, 2, 5, 4, 6, 6, 4, 2, 22]
            ],
            "answer": [29]
        }, {
            "input": [
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                [15, 19, 15, 27]
            ],
            "answer": [14, 18, 20, 22]
        }
    ], "3. Large": [
    {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [86, 46, 91]
        ],
        "answer": [2, 13, 21, 26, 39, 41, 50, 55, 72, 84, 89]
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 25, 10, 97, 89, 66, 67, 99, 48, 89, 97, 97, 97, 16, 44, 24, 6, 97, 72, 56, 3, 3, 66, 78, 73, 12, 73,
             73, 55, 41, 89, 78, 10, 35, 50, 42, 37, 31, 18, 37, 25, 31, 55, 72, 98, 36, 56, 0, 36, 23, 56, 93, 0,
             58, 92, 98, 5, 59, 25, 25, 3, 37, 78, 13, 3]
        ],
        "answer": [53]
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [83, 74, 26, 85, 86, 56, 64, 95, 53, 77, 15, 96, 17, 9, 14, 45, 80, 77, 82, 14, 0, 14, 84, 31, 17, 32,
             18, 80, 34, 59, 75, 77, 83, 34, 25, 3, 59, 3, 90, 82, 94, 45, 53, 96, 19, 65, 25, 15, 77, 82, 56, 95, 3,
             84, 62, 26, 82, 94, 51, 85, 45, 52, 48, 1, 9, 83, 82]
        ],
        "answer": [12]
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [14, 51, 14, 66, 24, 3, 60, 66, 92, 28, 38, 14, 51, 49, 46, 92]
        ],
        "answer": [78]
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [89, 24, 48, 29, 79, 41, 53, 5, 26, 8, 1, 3, 36, 83, 26, 70, 58, 65, 57, 37, 58, 46, 34, 43, 43, 60, 90,
             21, 11, 71, 51, 60, 24, 30, 40, 72, 26, 10, 30, 10, 67, 57, 84, 74, 29, 79, 94, 19, 16, 70, 68, 63, 95,
             45, 66, 91, 33, 64, 70, 61, 6, 9, 12, 35, 49, 91, 83, 22]
        ],
        "answer": []
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [15, 82, 28, 20, 76, 16, 31, 22, 35, 22, 66, 66, 76, 46, 77, 83, 28, 77, 47, 4, 20, 23, 83, 68, 58, 35,
             92, 37, 76, 2, 35, 33, 65, 33, 3, 45, 54, 77, 23, 77, 76, 36, 76, 76, 58, 68, 9, 94, 59, 7, 16, 15, 13,
             23, 54, 31, 4, 47, 7, 96, 94, 8, 60, 77, 45, 45, 52]
        ],
        "answer": [63]
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [13, 49, 40, 85, 60, 0, 9, 68, 79, 18, 0, 74, 48, 75, 75, 40, 71, 26, 98, 42, 8, 30, 55, 30, 49, 9, 94,
             75, 95, 8, 80, 0, 74, 8, 74, 41, 74, 0, 0, 40, 8, 55, 23, 66, 82, 40, 30, 19, 97, 0, 37, 49, 67, 32, 31,
             5, 24, 67, 3, 37, 40, 19, 54, 26, 98, 60, 13, 57, 17, 41, 0]
        ],
        "answer": [35]
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [90, 74, 4, 89, 3, 13, 38, 53, 10, 5, 70, 3, 99, 99, 25, 21, 91, 14, 53, 15, 50, 75, 92, 85, 64, 70, 7,
             20, 24, 40, 65, 94, 92, 27, 51, 97, 43, 60, 50, 25, 28, 33, 12, 86, 20, 71, 97, 37, 15, 88, 62, 61, 46,
             47, 3, 20, 65, 70, 44, 64, 90, 86, 26, 54, 5, 36, 34, 97, 33, 94, 97, 5, 78, 57, 62, 31, 57, 60, 19, 79,
             21, 92, 25, 22, 42]
        ],
        "answer": []
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [77, 94, 37, 85, 21, 87, 95]
        ],
        "answer": []
    }, {
        "input": [
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
             0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [17, 43, 34, 89, 28, 54]
        ],
        "answer": [21, 84]
    }
]
}
