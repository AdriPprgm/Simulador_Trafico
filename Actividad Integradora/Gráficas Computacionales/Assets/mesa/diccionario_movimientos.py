# type: ignore
import pprint
# Del -11 al 36 en x y y: ciudad completa (centro y periferia)
# Del 1 al 24: centro de la ciudad (actividad integradora - DEFINIDO)
# Del -11 al 0 y del 25 al 36: periferia (PLACEHOLDER - por definir)
movimientos_posibles = {
    -11: {
        -11: [(-11, -10)],  # Solo abajo
        -10: [(-11, -9)],  # Solo abajo
        -9: [(-11, -8), (-10, -9)],  # Abajo y derecha
        -8: [(-11, -7), (-10, -8)],  # Abajo y derecha
        -7: [(-11, -6), (-10, -7)],  # Abajo y derecha
        -6: [(-11, -5), (-10, -6)],  # Abajo y derecha
        -5: [(-11, -4), (-10, -5)],  # Abajo y derecha
        -4: [(-11, -3), (-10, -4)],  # Abajo y derecha
        -3: [(-11, -2), (-10, -3)],  # Abajo y derecha
        -2: [(-11, -1), (-10, -2)],  # Abajo y derecha
        -1: [(-11, 0), (-10, -1)],  # Abajo y derecha
        0: [(-11, 1), (-10, 0)],  # Abajo y derecha
        1: [(-11, 2), (-10, 1)],  # Abajo y derecha
        2: [(-11, 3), (-10, 2)],  # Abajo y derecha
        3: [(-11, 4), (-10, 3)],  # Abajo y derecha
        4: [(-11, 5), (-10, 4)],  # Abajo y derecha
        5: [(-11, 6), (-10, 5)],  # Abajo y derecha
        6: [(-11, 7), (-10, 6)],  # Abajo y derecha
        7: [(-11, 8), (-10, 7)],  # Abajo y derecha
        8: [(-11, 9), (-10, 8)],  # Abajo y derecha
        9: [(-11, 10), (-10, 9)],  # Abajo y derecha
        10: [(-11, 11), (-10, 10)],  # Abajo y derecha
        11: [(-11, 12), (-10, 11)],  # Abajo y derecha
        12: [(-11, 13), (-10, 12)],  # Abajo y derecha
        13: [(-11, 14), (-10, 13)],  # Abajo y derecha
        14: [(-11, 15), (-10, 14)],  # Abajo y derecha
        15: [(-11, 16), (-10, 15)],  # Abajo y derecha
        16: [(-11, 17), (-10, 16)],  # Abajo y derecha
        17: [(-11, 18), (-10, 17)],  # Abajo y derecha
        18: [(-11, 19), (-10, 18)],  # Abajo y derecha
        19: [(-11, 20), (-10, 19)],  # Abajo y derecha
        20: [(-11, 21), (-10, 20)],  # Abajo y derecha
        21: [(-11, 22), (-10, 21)],  # Abajo y derecha
        22: [(-11, 23), (-10, 22)],  # Abajo y derecha
        23: [(-11, 24), (-10, 23)],  # Abajo y derecha
        24: [(-11, 25), (-10, 24)],  # Abajo y derecha
        25: [(-11, 26), (-10, 25)],  # Abajo y derecha
        26: [(-11, 27), (-10, 26)],  # Abajo y derecha
        27: [(-11, 28), (-10, 27)],  # Abajo y derecha
        28: [(-11, 29), (-10, 28)],  # Abajo y derecha
        29: [(-11, 30), (-10, 29)],  # Abajo y derecha
        30: [(-11, 31), (-10, 30)],  # Abajo y derecha
        31: [(-11, 32), (-10, 31)],  # Abajo y derecha
        32: [(-11, 33), (-10, 32)],  # Abajo y derecha
        33: [(-11, 34), (-10, 33)],  # Abajo y derecha
        34: [(-11, 35), (-10, 34)],  # Abajo y derecha
        35: [(-11, 36), (-10, 35)],  # Abajo y derecha
        36: [(-10, 36)]  # Solo derecha
    },
    -10: {
        -11: [(-10, -10), (-11, -11)],  # Abajo e izquierda
        -10: [(-10, -9)],  # Solo abajo
        -9: [(-10, -8), (-11, -9)],  # Abajo e izquierda
        -8: [(-10, -7), (-11, -8)],  # Abajo e izquierda
        -7: [(-10, -6), (-11, -7)],  # Abajo e izquierda
        -6: [(-10, -5), (-11, -6)],  # Abajo e izquierda
        -5: [(-10, -4), (-11, -5)],  # Abajo e izquierda
        -4: [(-10, -3), (-11, -4)],  # Abajo e izquierda
        -3: [(-10, -2), (-11, -3)],  # Abajo e izquierda
        -2: [(-10, -1), (-11, -2)],  # Abajo e izquierda
        -1: [(-10, 0), (-11, -1)],  # Abajo e izquierda
        0: [(-10, 1), (-11, 0)],  # Abajo e izquierda
        1: [(-10, 2), (-11, 1)],  # Abajo e izquierda
        2: [(-10, 3), (-11, 2)],  # Abajo e izquierda
        3: [(-10, 4), (-11, 3)],  # Abajo e izquierda
        4: [(-10, 5), (-11, 4)],  # Abajo e izquierda
        5: [(-10, 6), (-11, 5)],  # Abajo e izquierda
        6: [(-10, 7), (-11, 6)],  # Abajo e izquierda
        7: [(-10, 8), (-11, 7)],  # Abajo e izquierda
        8: [(-10, 9), (-11, 8)],  # Abajo e izquierda
        9: [(-10, 10), (-11, 9)],  # Abajo e izquierda
        10: [(-10, 11), (-11, 10)],  # Abajo e izquierda
        11: [(-10, 12), (-11, 11), (-9, 11)],  # Abajo, izquierda y derecha
        12: [(-10, 13), (-11, 12), (-9, 12)],  # Abajo, izquierda y derecha
        13: [(-10, 14), (-11, 13)],  # Abajo e izquierda
        14: [(-10, 15), (-11, 14)],  # Abajo e izquierda
        15: [(-10, 16), (-11, 15)],  # Abajo e izquierda
        16: [(-10, 17), (-11, 16)],  # Abajo e izquierda
        17: [(-10, 18), (-11, 17)],  # Abajo e izquierda
        18: [(-10, 19), (-11, 18)],  # Abajo e izquierda
        19: [(-10, 20), (-11, 19)],  # Abajo e izquierda
        20: [(-10, 21), (-11, 20)],  # Abajo e izquierda
        21: [(-10, 22), (-11, 21)],  # Abajo e izquierda
        22: [(-10, 23), (-11, 22)],  # Abajo e izquierda
        23: [(-10, 24), (-11, 23)],  # Abajo e izquierda
        24: [(-10, 25), (-11, 24)],  # Abajo e izquierda
        25: [(-10, 26), (-11, 25)],  # Abajo e izquierda
        26: [(-10, 27), (-11, 26)],  # Abajo e izquierda
        27: [(-10, 28), (-11, 27)],  # Abajo e izquierda
        28: [(-10, 29), (-11, 28)],  # Abajo e izquierda
        29: [(-10, 30), (-11, 29)],  # Abajo e izquierda
        30: [(-10, 31), (-11, 30)],  # Abajo e izquierda
        31: [(-10, 32), (-11, 31)],  # Abajo e izquierda
        32: [(-10, 33), (-11, 32)],  # Abajo e izquierda
        33: [(-10, 34), (-11, 33)],  # Abajo e izquierda
        34: [(-10, 35), (-11, 34)],  # Abajo e izquierda
        35: [(-10, 36), (-9, 35)],  # Abajo y derecha
        36: [(-9, 36)]  # Solo derecha
    },
    -9: {
        -11: [(-10, -11), (-9, -10)],  # Izquierda y abajo
        -10: [(-10, -10), (-9, -11)],  # Izquierda y arriba
        2: [(-10, 2), (-9, 3)],  # Izquierda y abajo
        3: [(-10, 3), (-9, 2)],  # Izquierda y arriba
        9: [(-10, 9), (-9, 10)],  # Izquierda y abajo
        10: [(-10, 10), (-9, 9)],  # Izquierda y arriba
        11: [(-8, 11), (-9, 12)],  # Derecha y abajo
        12: [(-8, 12), (-9, 11)],  # Derecha y arriba
        35: [(-8, 35), (-9, 36)],  # Derecha y abajo
        36: [(-8, 36), (-9, 35)]  # Derecha y arriba
    },
    -8: {
        -11: [(-9, -11), (-8, -10)],  # Izquierda y abajo
        -10: [(-9, -10), (-8, -11)],  # Izquierda y arriba
        2: [(-9, 2), (-8, 3)],  # Izquierda y abajo
        3: [(-9, 3), (-8, 2)],  # Izquierda y arriba
        9: [(-9, 9), (-8, 10)],  # Izquierda y abajo
        10: [(-9, 10), (-8, 9)],  # Izquierda y arriba
        11: [(-7, 11), (-8, 12)],  # Derecha y abajo
        12: [(-7, 12), (-8, 11)],  # Derecha y arriba
        35: [(-7, 35), (-8, 36)],  # Derecha y abajo
        36: [(-7, 36), (-8, 35)]  # Derecha y arriba
    },
    -7: {
        -11: [(-8, -11), (-7, -10)],  # Izquierda y abajo
        -10: [(-8, -10), (-7, -11)],  # Izquierda y arriba
        2: [(-8, 2), (-7, 3)],  # Izquierda y abajo
        3: [(-8, 3), (-7, 2)],  # Izquierda y arriba
        9: [(-8, 9), (-7, 10)],  # Izquierda y abajo
        10: [(-8, 10), (-7, 9)],  # Izquierda y arriba
        11: [(-6, 11), (-7, 12)],  # Derecha y abajo
        12: [(-6, 12), (-7, 11)],  # Arriba y derecha
        13: [(-6, 13), (-7, 12)],  # Arriba y derecha
        14: [(-6, 14), (-7, 13)],  # Arriba y derecha
        15: [(-6, 15), (-7, 14)],  # Arriba y derecha
        16: [(-6, 16), (-7, 15)],  # Arriba y derecha
        17: [(-6, 17), (-7, 16)],  # Arriba y derecha
        18: [(-6, 18), (-7, 17)],  # Arriba y derecha
        19: [(-6, 19), (-7, 18)],  # Arriba y derecha
        20: [(-6, 20), (-7, 19)],  # Arriba y derecha
        21: [(-6, 21), (-7, 20)],  # Arriba y derecha
        22: [(-6, 22), (-7, 21)],  # Arriba y derecha
        23: [(-6, 23), (-7, 22)],  # Arriba y derecha
        24: [(-6, 24), (-7, 23)],  # Arriba y derecha
        25: [(-6, 25), (-7, 24)],  # Arriba y derecha
        26: [(-6, 26), (-7, 25)],  # Arriba y derecha
        27: [(-6, 27), (-7, 26)],  # Arriba y derecha
        28: [(-6, 28), (-7, 27)],  # Arriba y derecha
        29: [(-6, 29), (-7, 28)],  # Arriba y derecha
        30: [(-6, 30), (-7, 29)],  # Arriba y derecha
        31: [(-6, 31), (-7, 30)],  # Arriba y derecha
        32: [(-6, 32), (-7, 31)],  # Arriba y derecha
        33: [(-6, 33), (-7, 32)],  # Arriba y derecha
        34: [(-6, 34), (-7, 33)],  # Arriba y derecha
        35: [(-6, 35), (-7, 36), (-7, 34)],  # Derecha, abajo y arriba
        36: [(-6, 36), (-7, 35)]  # Arriba y derecha
    },
    -6: {
        -11: [(-7, -11), (-6, -10)],  # Izquierda y abajo
        -10: [(-7, -10), (-6, -11)],  # Arriba e izquierda
        2: [(-7, 2), (-6, 3)],  # Izquierda y abajo
        3: [(-7, 3), (-6, 2)],  # Arriba e izquierda
        9: [(-7, 9), (-6, 10)],  # Izquierda y abajo
        10: [(-7, 10), (-6, 9)],  # Arriba e izquierda
        11: [(-5, 11), (-6, 12)],  # Derecha y abajo
        12: [(-5, 12), (-6, 11)],  # Derecha y arriba
        13: [(-7, 13), (-6, 12)],  # Arriba e izquierda
        14: [(-7, 14), (-6, 13)],  # Arriba e izquierda
        15: [(-7, 15), (-6, 14)],  # Arriba e izquierda
        16: [(-7, 16), (-6, 15)],  # Arriba e izquierda
        17: [(-7, 17), (-6, 16)],  # Arriba e izquierda
        18: [(-7, 18), (-6, 17)],  # Arriba e izquierda
        19: [(-7, 19), (-6, 18)],  # Arriba e izquierda
        20: [(-7, 20), (-6, 19)],  # Arriba e izquierda
        21: [(-7, 21), (-6, 20)],  # Arriba e izquierda
        22: [(-7, 22), (-6, 21)],  # Arriba e izquierda
        23: [(-7, 23), (-6, 22)],  # Arriba e izquierda
        24: [(-7, 24), (-6, 23)],  # Arriba e izquierda
        25: [(-7, 25), (-6, 24)],  # Arriba e izquierda
        26: [(-7, 26), (-6, 25)],  # Arriba e izquierda
        27: [(-7, 27), (-6, 26)],  # Arriba e izquierda
        28: [(-7, 28), (-6, 27)],  # Arriba e izquierda
        29: [(-7, 29), (-6, 28)],  # Arriba e izquierda
        30: [(-7, 30), (-6, 29)],  # Arriba e izquierda
        31: [(-7, 31), (-6, 30)],  # Arriba e izquierda
        32: [(-7, 32), (-6, 31)],  # Arriba e izquierda
        33: [(-7, 33), (-6, 32)],  # Arriba e izquierda
        34: [(-7, 34), (-6, 33)],  # Arriba e izquierda
        35: [(-5, 35), (-6, 36), (-6, 34)],  # Derecha, abajo y arriba
        36: [(-5, 36), (-6, 35)]  # Derecha y arriba
    },
    -5: {
        -11: [(-6, -11), (-5, -10)],  # Izquierda y abajo
        -10: [(-6, -10), (-5, -11)],  # Izquierda y arriba
        2: [(-6, 2), (-5, 3)],  # Izquierda y abajo
        3: [(-6, 3), (-5, 2)],  # Izquierda y arriba
        9: [(-6, 9), (-5, 10)],  # Izquierda y abajo
        10: [(-6, 10), (-5, 9)],  # Izquierda y arriba
        11: [(-4, 11), (-5, 12)],  # Derecha y abajo
        12: [(-4, 12), (-5, 11)],  # Derecha y arriba
        30: [(-6, 30), (-5, 31)],  # Izquierda y abajo
        31: [(-6, 31), (-5, 30)],  # Izquierda y arriba
        35: [(-4, 35), (-5, 36)],  # Derecha y abajo
        36: [(-4, 36), (-5, 35)]  # Derecha y arriba
    },
    -4: {
        -11: [(-5, -11), (-4, -10)],  # Abajo e izquierda
        -10: [(-5, -10), (-4, -11), (-4, -9)],  # Izquierda, arriba y abajo
        -9: [(-3, -9), (-4, -8)],  # Abajo y derecha
        -8: [(-3, -8), (-4, -7)],  # Abajo y derecha
        -7: [(-3, -7), (-4, -6)],  # Abajo y derecha
        -6: [(-3, -6), (-4, -5)],  # Abajo y derecha
        -5: [(-3, -5), (-4, -4)],  # Abajo y derecha
        -4: [(-3, -4), (-4, -3)],  # Abajo y derecha
        -3: [(-3, -3), (-4, -2)],  # Abajo y derecha
        -2: [(-3, -2), (-4, -1)],  # Abajo y derecha
        -1: [(-3, -1), (-4, 0)],  # Abajo y derecha
        0: [(-3, 0), (-4, 1)],  # Abajo y derecha
        1: [(-3, 1), (-4, 2)],  # Abajo y derecha
        2: [(-5, 2), (-4, 3)],  # Abajo e izquierda
        3: [(-5, 3), (-4, 2)],  # Arriba e izquierda
        9: [(-5, 9), (-4, 10)],  # Abajo e izquierda
        10: [(-5, 10), (-4, 9)],  # Arriba e izquierda
        11: [(-3, 11), (-4, 12)],  # Abajo y derecha
        12: [(-3, 12), (-4, 11)],  # Arriba y derecha
        30: [(-5, 30), (-4, 31)],  # Abajo e izquierda
        31: [(-5, 31), (-4, 30)],  # Arriba e izquierda
        35: [(-3, 35), (-4, 36)],  # Abajo y derecha
        36: [(-3, 36), (-4, 35)]  # Arriba y derecha
    },
    -3: {
        -11: [(-4, -11), (-3, -10)],  # Abajo e izquierda
        -10: [(-4, -10), (-3, -11), (-3, -9)],  # Arriba, abajo e izquierda
        -9: [(-4, -9), (-3, -8)],  # Abajo e izquierda
        -8: [(-4, -8), (-3, -7)],  # Abajo e izquierda
        -7: [(-4, -7), (-3, -6)],  # Abajo e izquierda
        -6: [(-4, -6), (-3, -5)],  # Abajo e izquierda
        -5: [(-4, -5), (-3, -4)],  # Abajo e izquierda
        -4: [(-4, -4), (-3, -3)],  # Abajo e izquierda
        -3: [(-4, -3), (-3, -2)],  # Abajo e izquierda
        -2: [(-4, -2), (-3, -1)],  # Abajo e izquierda
        -1: [(-4, -1), (-3, 0)],  # Abajo e izquierda
        0: [(-4, 0), (-3, 1)],  # Abajo e izquierda
        1: [(-4, 1), (-3, 2)],  # Abajo e izquierda
        2: [(-4, 2), (-3, 3)],  # Abajo e izquierda
        3: [(-4, 3)],  # Solo a la izquierda
        9: [(-4, 9), (-3, 10)],  # Abajo e izquierda
        10: [(-4, 10), (-3, 9)],  # Arriba e izquierda
        11: [(-2, 11), (-3, 12)],  # Abajo y derecha
        12: [(-2, 12), (-3, 11)],  # Arriba y derecha
        30: [(-4, 30), (-3, 31)],  # Abajo e izquierda
        31: [(-4, 31), (-3, 30)],  # Arriba e izquierda
        35: [(-2, 35), (-3, 36)],  # Abajo y derecha
        36: [(-2, 36), (-3, 35)]  # Arriba y derecha
    },
    -2: {
        -11: [(-3, -11), (-2, -10)],  # Abajo e izquierda
        -10: [(-3, -10), (-2, -11)],  # Arriba e izquierda
        -2: [(-1, -2)],  # Solo derecha
        -1: [(-1, -1), (-2, -2)],  # Arriba y derecha
        0: [(-1, 0), (-2, -1)],  # Arriba y derecha
        1: [(-1, 1), (-2, 0)],  # Arriba y derecha
        2: [(-1, 2), (-2, 1)],  # Arriba y derecha
        3: [(-1, 3), (-2, 2)],  # Arriba y derecha
        4: [(-1, 4), (-2, 3)],  # Arriba y derecha
        5: [(-1, 5), (-2, 4)],  # Arriba y derecha
        6: [(-1, 6), (-2, 5)],  # Arriba y derecha
        7: [(-1, 7), (-2, 6)],  # Arriba y derecha
        8: [(-1, 8), (-2, 7)],  # Arriba y derecha
        9: [(-3, 9), (-2, 8), (-2, 10)],  # Arriba, abajo e izquierda
        10: [(-3, 10), (-2, 9)],  # Arriba e izquierda
        11: [(-1, 11), (-2, 12)],  # Abajo y derecha
        12: [(-1, 12), (-2, 11)],  # Arriba y derecha
        30: [(-3, 30), (-2, 31)],  # Abajo e izquierda
        31: [(-3, 31), (-2, 30)],  # Arriba e izquierda
        35: [(-1, 35), (-2, 36)],  # Abajo y derecha
        36: [(-1, 36), (-2, 35)]  # Arriba y derecha
    },
    -1: {
        -11: [(-2, -11), (-1, -10)],  # Abajo e izquierda
        -10: [(-2, -10), (-1, -11)],  # Arriba e izquierda
        -2: [(0, -2)],  # Solo derecha
        -1: [(0, -1), (-1, -2)],  # Arriba y derecha
        0: [(-2, 0), (-1, -1)],  # Arriba e izquierda
        1: [(-2, 1), (-1, 0)],  # Arriba e izquierda
        2: [(-2, 2), (-1, 1)],  # Arriba e izquierda
        3: [(-2, 3), (-1, 2)],  # Arriba e izquierda
        4: [(-2, 4), (-1, 3)],  # Arriba e izquierda
        5: [(-2, 5), (-1, 4)],  # Arriba e izquierda
        6: [(-2, 6), (-1, 5)],  # Arriba e izquierda
        7: [(-2, 7), (-1, 6)],  # Arriba e izquierda
        8: [(-2, 8), (-1, 7)],  # Arriba e izquierda
        9: [(-2, 9), (-1, 8), (-1, 10)],  # Arriba, abajo e izquierda
        10: [(-2, 10), (-1, 9)],  # Arriba e izquierda
        11: [(0, 11), (-1, 12)],  # Abajo y derecha
        12: [(0, 12), (-1, 11)],  # Arriba y derecha
        30: [(-2, 30), (-1, 31)],  # Abajo e izquierda
        31: [(-2, 31), (-1, 30)],  # Arriba e izquierda
        35: [(0, 35), (-1, 36)],  # Abajo y derecha
        36: [(0, 36), (-1, 35)]  # Arriba y derecha
    },
    0: {
        -11: [(-1, -11), (0, -10)],  # Abajo e izquierda
        -10: [(-1, -10), (0, -11)],  # Arriba e izquierda
        -2: [(1, -2), (0, -1)],  # Abajo y derecha
        -1: [(1, -1), (0, -2)],  # Arriba y derecha
        9: [(-1, 9), (0, 10)],  # Abajo e izquierda
        10: [(-1, 10), (0, 9)],  # Arriba e izquierda
        11: [(1, 11), (0, 12)],  # Abajo y derecha
        12: [(1, 12), (0, 11)],  # Arriba y derecha
        30: [(-1, 30), (0, 31)],  # Abajo e izquierda
        31: [(-1, 31), (0, 30)],  # Arriba e izquierda
        35: [(1, 35), (0, 36)],  # Abajo y derecha
        36: [(1, 36), (0, 35)]  # Arriba y derecha
    },
    1: {
        -11: [(0, -11), (1, -10)],  # Abajo e izquierda
        -10: [(0, -10), (1, -11)],  # Arriba e izquierda
        -2: [(2, -2), (1, -1)],  # Abajo y derecha
        -1: [(2, -1), (1, -2)],  # Arriba y derecha
        1: [(1, 2)],
        2: [(1, 1), (1, 3)],
        3: [(1, 4), (2, 3)],
        4: [(1, 5)],
        5: [(1, 6), (2, 5)],
        6: [(1, 7), (2, 6)],
        7: [(1, 8), (2, 7)],
        8: [(1, 9)],
        9: [(1, 10), (2, 9)],
        10: [(1, 11), (2, 10)],
        11: [(1, 12), (2, 11)],
        12: [(1, 13), (2, 12)],
        13: [(1, 14), (2, 13)],
        14: [(1, 15), (2, 14)],
        15: [(1, 16), (2, 15)],
        16: [(1, 17), (2, 16)],
        17: [(1, 18), (2, 17)],
        18: [(1, 19), (2, 18)],
        19: [(1, 20), (2, 19)],
        20: [(1, 21), (2, 20)],
        21: [(1, 22), (2, 21)],
        22: [(1, 23), (2, 22)],
        23: [(1, 24), (2, 23)],
        24: [(1, 23), (2, 24)],
        30: [(0, 30), (1, 31)],  # Abajo e izquierda
        31: [(0, 31), (1, 30)],  # Arriba e izquierda
        35: [(2, 35), (1, 36)],  # Abajo y derecha
        36: [(2, 36), (1, 35)]  # Arriba y derecha
    },
    2: {
        -11: [(1, -11), (2, -10)],  # Abajo e izquierda
        -10: [(1, -10), (2, -11)],  # Arriba e izquierda
        -2: [(3, -2), (2, -1)],  # Abajo y derecha
        -1: [(3, -1), (2, -2)],  # Arriba y derecha
        1: [(2, 2), (1, 1)],
        2: [(2, 1), (2, 3), (1, 2)],
        3: [(2, 4), (1, 3)],
        4: [(2, 5)],
        5: [(2, 6), (1, 5)],
        6: [(2, 7), (1, 6)],
        7: [(2, 8), (1, 7)],
        8: [(2, 9)],
        9: [(2, 10), (1, 9)],
        10: [(2, 11), (1, 10)],
        11: [(2, 12), (1, 11), (3, 11)],
        12: [(2, 13), (1, 12), (3, 12)],
        13: [(2, 14), (1, 13)],
        14: [(2, 15), (1, 14)],
        15: [(2, 16), (1, 15)],
        16: [(2, 17), (1, 16)],
        17: [(2, 18), (1, 17), (3, 17)],
        18: [(2, 19), (1, 18), (3, 18)],
        19: [(2, 20), (1, 19)],
        20: [(2, 21), (1, 20)],
        21: [(2, 22), (1, 21)],
        22: [(2, 23), (1, 22)],
        23: [(2, 24), (3, 23)],
        24: [(2, 23), (3, 24)],
        30: [(1, 30), (2, 31)],  # Abajo e izquierda
        31: [(1, 31), (2, 30)],  # Arriba e izquierda
        35: [(3, 35), (2, 36)],  # Abajo y derecha
        36: [(3, 36), (2, 35)]  # Arriba y derecha
    },
    3: {
        -11: [(2, -11), (3, -10)],  # Abajo e izquierda
        -10: [(2, -10), (3, -11)],  # Arriba e izquierda
        -2: [(4, -2), (3, -1)],  # Abajo y derecha
        -1: [(4, -1), (3, -2)],  # Arriba y derecha
        1: [(3, 2), (2, 1)],
        2: [(3, 1), (2, 2)],
        5: [(2, 5)],
        6: [(2, 6)],
        9: [(2, 9)],
        10: [(2, 10)],
        11: [(3, 12), (4, 11)],
        12: [(3, 11), (4, 12)],
        17: [(3, 18), (4, 17)],
        18: [(3, 17), (4, 18)],
        23: [(3, 24), (4, 23)],
        24: [(3, 23), (4, 24)],
        30: [(2, 30), (3, 31)],  # Abajo e izquierda
        31: [(2, 31), (3, 30)],  # Arriba e izquierda
        35: [(4, 35), (3, 36)],  # Abajo y derecha
        36: [(4, 36), (3, 35)]  # Arriba y derecha
    },
    4: {
        -11: [(3, -11), (4, -10)],  # Abajo e izquierda
        -10: [(3, -10), (4, -11)],  # Arriba e izquierda
        -2: [(5, -2), (4, -1)],  # Abajo y derecha
        -1: [(5, -1), (4, -2)],  # Arriba y derecha
        1: [(4, 2), (3, 1)],
        2: [(4, 1), (3, 2)],
        4: [(4, 5), (5, 4)],
        5: [(4, 6), (3, 5)],
        6: [(4, 5), (3, 6)],
        9: [(4, 10), (3, 9)],
        10: [(4, 9), (3, 10)],
        11: [(4, 12), (5, 11)],
        12: [(4, 11), (5, 12)],
        13: [(4, 12), (5, 13)],
        17: [(4, 18), (5, 17)],
        18: [(4, 17), (5, 18)],
        23: [(4, 24), (5, 23)],
        24: [(4, 23), (5, 24)],
        30: [(3, 30), (4, 31)],  # Abajo e izquierda
        31: [(3, 31), (4, 30)],  # Arriba e izquierda
        35: [(5, 35), (4, 36)],  # Abajo y derecha
        36: [(5, 36), (4, 35)]  # Arriba y derecha
    },
    5: {
        -11: [(4, -11), (5, -10)],  # Abajo e izquierda
        -10: [(4, -10), (5, -11)],  # Arriba e izquierda
        -2: [(6, -2), (5, -1)],  # Abajo y derecha
        -1: [(6, -1), (5, -2)],  # Arriba y derecha
        1: [(5, 2), (4, 1)],
        2: [(5, 1), (5, 3), (4, 2)],
        3: [(5, 4), (6, 3)],
        4: [(5, 5), (4, 4), (6, 4)],
        5: [(5, 6), (4, 5)],
        6: [(5, 5), (5, 7), (4, 6)],
        7: [(5, 8), (6, 7)],
        8: [(5, 9), (6, 8)],
        9: [(5, 10), (4, 9)],
        10: [(5, 9), (4, 10)],
        11: [(5, 12), (6, 11)],
        12: [(5, 11), (6, 12)],
        13: [(5, 12), (4, 13), (6, 13)],
        14: [(5, 13), (6, 14)],
        15: [(5, 14), (6, 15)],
        16: [(5, 15), (6, 16)],
        17: [(5, 16), (5, 18), (6, 17)],
        18: [(5, 17), (6, 18)],
        22: [(5, 23)],
        23: [(5, 24), (6, 23)],
        24: [(5, 23), (6, 24)],
        30: [(4, 30), (5, 31)],  # Abajo e izquierda
        31: [(4, 31), (5, 30)],  # Arriba e izquierda
        35: [(6, 35), (5, 36)],  # Abajo y derecha
        36: [(6, 36), (5, 35)]  # Arriba y derecha
    },
    6: {
        -11: [(5, -11), (6, -10)],  # Abajo e izquierda
        -10: [(5, -10), (6, -11)],  # Arriba e izquierda
        -2: [(7, -2), (6, -1)],  # Abajo y derecha
        -1: [(7, -1), (6, -2)],  # Arriba y derecha
        1: [(6, 2), (5, 1)],
        2: [(6, 1), (6, 3), (5, 2)],
        3: [(6, 4), (5, 3)],
        4: [(6, 5), (5, 4)],
        5: [(6, 6), (5, 5)],
        6: [(6, 5), (6, 7), (5, 6)],
        7: [(6, 8), (5, 7)],
        8: [(6, 9), (5, 8)],
        9: [(6, 10), (5, 9)],
        10: [(6, 9), (5, 10)],
        11: [(6, 12), (7, 11)],
        12: [(6, 11), (7, 12)],
        13: [(6, 12), (5, 13)],
        14: [(6, 13), (5, 14)],
        15: [(6, 14), (5, 15)],
        16: [(6, 15), (5, 16), (7, 16)],
        17: [(6, 16), (6, 18), (7, 17)],
        18: [(6, 17), (7, 18)],
        23: [(6, 24), (7, 23)],
        24: [(6, 23), (7, 24)],
        30: [(5, 30), (6, 31)],  # Abajo e izquierda
        31: [(5, 31), (6, 30)],  # Arriba e izquierda
        35: [(7, 35), (6, 36)],  # Abajo y derecha
        36: [(7, 36), (6, 35)]  # Arriba y derecha
    },
    7: {
        -11: [(6, -11), (7, -10)],  # Abajo e izquierda
        -10: [(6, -10), (7, -11)],  # Arriba e izquierda
        -2: [(8, -2), (7, -1)],  # Abajo y derecha
        -1: [(8, -1), (7, -2)],  # Arriba y derecha
        1: [(7, 2), (6, 1)],
        2: [(7, 1), (6, 2)],
        5: [(7, 6), (6, 5)],
        6: [(7, 5), (6, 6)],
        9: [(7, 10), (6, 9)],
        10: [(7, 9), (6, 10)],
        11: [(7, 12), (8, 11)],
        12: [(7, 11), (8, 12)],
        13: [(7, 12), (8, 13)],
        16: [(7, 17), (6, 16)],
        17: [(7, 16), (7, 18), (8, 17)],
        18: [(7, 17), (7, 19), (8, 18)],
        19: [(7, 18)],
        23: [(7, 24), (8, 23)],
        24: [(7, 23), (8, 24)],
        30: [(6, 30), (7, 31)],  # Abajo e izquierda
        31: [(6, 31), (7, 30)],  # Arriba e izquierda
        35: [(8, 35), (7, 36)],  # Abajo y derecha
        36: [(8, 36), (7, 35)]  # Arriba y derecha
    },
    8: {
        -11: [(7, -11), (8, -10)],  # Abajo e izquierda
        -10: [(7, -10), (8, -11)],  # Arriba e izquierda
        -2: [(9, -2), (8, -1)],  # Abajo y derecha
        -1: [(9, -1), (8, -2)],  # Arriba y derecha
        1: [(8, 2), (7, 1)],
        2: [(8, 1), (7, 2)],
        5: [(8, 6), (7, 5)],
        6: [(8, 5), (8, 7), (7, 6)],
        7: [(8, 6), (9, 7)],
        9: [(8, 10), (7, 9)],
        10: [(8, 9), (7, 10)],
        11: [(8, 12), (9, 11)],
        12: [(8, 11), (9, 12)],
        17: [(8, 18), (9, 17)],
        18: [(8, 17), (9, 18)],
        23: [(9, 23)],
        24: [(9, 24)],
        30: [(7, 30), (8, 31)],  # Abajo e izquierda
        31: [(7, 31), (8, 30)],  # Arriba e izquierda
        35: [(9, 35), (8, 36)],  # Abajo y derecha
        36: [(9, 36), (8, 35)]  # Arriba y derecha
    },
    9: {
        -11: [(8, -11), (9, -10)],  # Abajo e izquierda
        -10: [(8, -10), (9, -11), (9, -9)],  # Abajo, izquierda y arriba
        -9: [(10, -9), (9, -8)],  # Derecha y abajo
        -8: [(10, -8), (9, -7)],  # Derecha y abajo
        -7: [(10, -7), (9, -6)],  # Derecha y abajo
        -6: [(10, -6), (9, -5)],  # Derecha y abajo
        -5: [(10, -5), (9, -4)],  # Derecha y abajo
        -4: [(10, -4), (9, -3)],  # Derecha y abajo
        -3: [(10, -3), (9, -2)],  # Derecha y abajo
        -2: [(10, -2), (9, -1)],  # Derecha y abajo
        -1: [(10, -1), (9, 0)],  # Derecha y abajo
        0: [(10, 0), (9, 1)],  # Derecha y abajo
        1: [(9, 2), (8, 1)],
        2: [(9, 1), (9, 3), (8, 2)],
        3: [(9, 4), (10, 3)],
        4: [(9, 5), (10, 4)],
        5: [(9, 6), (8, 5), (10, 5)],
        6: [(9, 7), (8, 6), (10, 6)],
        7: [(9, 8), (8, 7), (10, 7)],
        8: [(9, 9), (10, 8)],
        9: [(9, 10), (8, 9)],
        10: [(9, 11), (8, 10)],
        11: [(9, 12)],
        12: [(9, 13), (10, 12)],
        13: [(9, 14), (10, 13)],
        14: [(9, 15), (10, 14)],
        15: [(9, 16), (10, 15)],
        16: [(9, 17), (10, 16)],
        17: [(9, 18), (10, 17)],
        18: [(9, 19), (10, 18)],
        19: [(9, 20), (10, 19)],
        20: [(9, 21), (10, 20)],
        21: [(9, 22), (10, 21)],
        22: [(9, 23)],
        23: [(9, 24), (10, 23)],
        24: [(9, 23), (10, 24)],
        25: [(10, 25), (9, 26)],  # Derecha y abajo
        26: [(10, 26), (9, 27)],  # Derecha y abajo
        27: [(10, 27), (9, 28)],  # Derecha y abajo
        28: [(10, 28), (9, 29)],  # Derecha y abajo
        29: [(10, 29), (9, 30)],  # Derecha y abajo
        30: [(10, 30), (9, 31), (8, 30)],  # Abajo, derecha e izquierda
        31: [(10, 31), (9, 32), (8, 31)],  # Abajo, derecha e izquierda
        32: [(10, 32), (9, 33)],  # Derecha y abajo
        33: [(10, 33), (9, 34)],  # Derecha y abajo
        34: [(10, 34), (9, 35)],  # Derecha y abajo
        35: [(10, 35), (9, 36)],  # Derecha y abajo
        36: [(10, 36), (9, 35)]  # Arriba y derecha
    },
    10: {
        -11: [(9, -11), (10, -10)],  # Abajo e izquierda
        -10: [(9, -10), (10, -11)],  # Abajo e izquierda
        -9: [(9, -9), (10, -8)],  # Abajo e izquierda
        -8: [(9, -8), (10, -7)],  # Abajo e izquierda
        -7: [(9, -7), (10, -6)],  # Abajo e izquierda
        -6: [(9, -6), (10, -5)],  # Abajo e izquierda
        -5: [(9, -5), (10, -4)],  # Abajo e izquierda
        -4: [(9, -4), (10, -3)],  # Abajo e izquierda
        -3: [(9, -3), (10, -2)],  # Abajo e izquierda
        -2: [(9, -2), (10, -1)],  # Abajo e izquierda
        -1: [(9, -1), (10, 0)],  # Abajo e izquierda
        0: [(9, 0), (10, 1)],  # Abajo e izquierda
        1: [(10, 2), (9, 1)],
        2: [(10, 1), (10, 3), (9, 2)],
        3: [(10, 4), (9, 3)],
        4: [(10, 5), (9, 4)],
        5: [(10, 6), (9, 5)],
        6: [(10, 7), (9, 6)],
        7: [(10, 8), (9, 7)],
        8: [(10, 9), (9, 8)],
        9: [(9, 9)],
        12: [(10, 13), (11, 12)],
        13: [(10, 14), (9, 13)],
        14: [(10, 15), (9, 14)],
        15: [(10, 16), (9, 15)],
        16: [(10, 17), (9, 16)],
        17: [(10, 18), (9, 17)],
        18: [(10, 19), (9, 18)],
        19: [(10, 20), (9, 19)],
        20: [(10, 21), (9, 20)],
        21: [(10, 22), (9, 21)],
        22: [(10, 23)],
        23: [(10, 24), (11, 23)],
        24: [(10, 23), (11, 24)],
        25: [(9, 25), (10, 26)],  # Abajo e izquierda
        26: [(9, 26), (10, 27)],  # Abajo e izquierda
        27: [(9, 27), (10, 28)],  # Abajo e izquierda
        28: [(9, 28), (10, 29)],  # Abajo e izquierda
        29: [(9, 29), (10, 30)],  # Abajo e izquierda
        30: [(9, 30), (10, 31)],  # Abajo e izquierda
        31: [(9, 31), (10, 32)],  # Abajo e izquierda
        32: [(9, 32), (10, 33)],  # Abajo e izquierda
        33: [(9, 33), (10, 34)],  # Abajo e izquierda
        34: [(9, 34), (10, 35)],  # Abajo e izquierda
        35: [(11, 35), (10, 36)],  # Derecha y abajo
        36: [(11, 36), (10, 35)]  # Derecha y arriba
    },
    11: {
        -11: [(10, -11), (11, -10)],  # Abajo e izquierda
        -10: [(10, -10), (11, -11)],  # Arriba e izquierda
        -9: [(12, -9), (11, -10)],  # Arriba y derecha
        -8: [(12, -8), (11, -9)],  # Arriba y derecha
        -7: [(12, -7), (11, -8)],  # Arriba y derecha
        -6: [(12, -6), (11, -7)],  # Arriba y derecha
        -5: [(12, -5), (11, -6)],  # Arriba y derecha
        -4: [(12, -4), (11, -5)],  # Arriba y derecha
        -3: [(12, -3), (11, -4)],  # Arriba y derecha
        -2: [(12, -2), (11, -3)],  # Arriba y derecha
        -1: [(12, -1), (11, -2)],  # Arriba y derecha
        0: [(12, 0), (11, -1)],  # Arriba y derecha
        1: [(11, 2), (10, 1)],
        2: [(11, 1), (10, 2)],
        3: [(11, 2)],
        4: [(11, 3), (12, 4)],
        5: [(11, 4), (12, 5)],
        6: [(11, 5), (12, 6)],
        7: [(11, 6), (12, 7)],
        8: [(11, 7), (12, 8)],
        9: [(11, 8), (10, 9)],
        12: [(12, 12)],
        13: [(11, 12), (12, 13)],
        14: [(11, 13), (12, 14)],
        15: [(11, 14), (12, 15)],
        16: [(11, 15), (12, 16)],
        17: [(11, 16), (12, 17)],
        18: [(11, 17), (12, 18)],
        19: [(11, 18), (12, 19)],
        20: [(11, 19), (12, 20)],
        21: [(11, 20), (12, 21)],
        22: [(11, 21), (12, 22)],
        23: [(11, 22), (11, 24), (12, 23)],
        24: [(11, 23), (12, 24)],
        25: [(12, 25), (11, 24)],  # Arriba y derecha
        26: [(12, 26), (11, 25)],  # Arriba y derecha
        27: [(12, 27), (11, 26)],  # Arriba y derecha
        28: [(12, 28), (11, 27)],  # Arriba y derecha
        29: [(12, 29), (11, 28)],  # Arriba y derecha
        30: [(12, 30), (11, 29)],  # Arriba y derecha
        31: [(12, 31), (11, 30)],  # Arriba y derecha
        32: [(12, 32), (11, 31)],  # Arriba y derecha
        33: [(12, 33), (11, 32)],  # Arriba y derecha
        34: [(12, 34), (11, 33)],  # Arriba y derecha
        35: [(12, 35), (11, 36), (11, 34)],  # Arriba, abajo y derecha
        36: [(12, 36), (11, 35)]  # Arriba y derecha
    },
    12: {
        -11: [(11, -11), (12, -12)],  # Abajo e izquierda
        -10: [(11, -10), (12, -11)],  # Arriba e izquierda
        -9: [(11, -9), (12, -10)],  # Arriba e izquierda
        -8: [(11, -8), (12, -9)],  # Arriba e izquierda
        -7: [(11, -7), (12, -8)],  # Arriba e izquierda
        -6: [(11, -6), (12, -7)],  # Arriba e izquierda
        -5: [(11, -5), (12, -6)],  # Arriba e izquierda
        -4: [(11, -4), (12, -5)],  # Arriba e izquierda
        -3: [(11, -3), (12, -4)],  # Arriba e izquierda
        -2: [(11, -2), (13, -2), (12, -3)],  # Arriba, izquierda y derecha
        -1: [(11, -1), (13, -1), (12, -2)],  # Arriba, izquierda y derecha
        0: [(11, 0), (12, -1)],  # Arriba e izquierda
        1: [(12, 2), (11, 1)],
        2: [(12, 1), (11, 2)],
        3: [(12, 2)],
        4: [(12, 3), (11, 4)],
        5: [(12, 4), (11, 5), (13, 5)],
        6: [(12, 5), (11, 6), (13, 6)],
        7: [(12, 6), (11, 7)],
        8: [(12, 7), (11, 8)],
        9: [(12, 8), (11, 9)],
        10: [(12, 9)],
        11: [(12, 10), (13, 11)],
        12: [(12, 11), (13, 12)],
        13: [(12, 12), (11, 13)],
        14: [(12, 13), (11, 14)],
        15: [(12, 14), (11, 15)],
        16: [(12, 15), (11, 16)],
        17: [(12, 16), (11, 17)],
        18: [(12, 17), (11, 18)],
        19: [(12, 18), (11, 19), (13, 19)],
        20: [(12, 19), (11, 20)],
        21: [(12, 20), (11, 21)],
        22: [(12, 21), (11, 22)],
        23: [(12, 24), (13, 23)],
        24: [(12, 23), (13, 24)],
        25: [(11, 25), (12, 24)],  # Arriba e izquierda
        26: [(11, 26), (12, 25)],  # Arriba e izquierda
        27: [(11, 27), (12, 26)],  # Arriba e izquierda
        28: [(11, 28), (12, 27)],  # Arriba e izquierda
        29: [(11, 29), (12, 28)],  # Arriba e izquierda
        30: [(11, 30), (12, 29)],  # Arriba e izquierda
        31: [(11, 31), (12, 30)],  # Arriba e izquierda
        32: [(11, 32), (12, 31)],  # Arriba e izquierda
        33: [(11, 33), (12, 32)],  # Arriba e izquierda
        34: [(11, 34), (12, 33)],  # Arriba e izquierda
        35: [(13, 35), (12, 36), (12, 34)],  # Arriba, abajo y derecha
        36: [(13, 36), (12, 35)]  # Arriba y derecha
    },
    13: {
        -11: [(12, -11), (13, -12)],  # Abajo e izquierda
        -10: [(12, -10), (13, -11)],  # Arriba e izquierda
        -6: [(12, -6), (13, -7)],  # Abajo e izquierda
        -5: [(12, -5), (13, -6)],  # Arriba e izquierda
        -2: [(14, -2), (13, -3)],  # Abajo y derecha
        -1: [(14, -1), (13, -2)],  # Arriba y derecha
        1: [(12, 1)],
        2: [(12, 2)],
        5: [(13, 6), (14, 5)],
        6: [(13, 5), (14, 6)],
        9: [(13, 10), (12, 9)],
        10: [(13, 9), (12, 10)],
        11: [(13, 12), (14, 11)],
        12: [(13, 11), (14, 12)],
        16: [(13, 17), (12, 16)],
        17: [(13, 16), (12, 17)],
        19: [(12, 19)],
        23: [(13, 24), (14, 23)],
        24: [(13, 23), (14, 24)],
        30: [(12, 30), (13, 29)],  # Abajo e izquierda
        31: [(12, 31), (13, 30)],  # Arriba e izquierda
        35: [(14, 35), (13, 34)],  # Abajo y derecha
        36: [(14, 36), (13, 35)]  # Arriba y derecha
    },
    14: {
        -11: [(13, -11), (14, -12)],  # Abajo e izquierda
        -10: [(13, -10), (14, -11)],  # Arriba e izquierda
        -6: [(13, -6), (14, -7)],  # Abajo e izquierda
        -5: [(13, -5), (14, -6)],  # Arriba e izquierda
        -2: [(15, -2), (14, -3)],  # Abajo y derecha
        -1: [(15, -1), (14, -2)],  # Arriba y derecha
        1: [(14, 2), (13, 1)],
        2: [(14, 1), (13, 2)],
        4: [(14, 5)],
        5: [(14, 4), (14, 6), (15, 5)],
        6: [(14, 5), (15, 6)],
        9: [(14, 10), (13, 9)],
        10: [(14, 9), (13, 10)],
        11: [(14, 12), (15, 11)],
        12: [(14, 11), (15, 12)],
        16: [(14, 17), (13, 16)],
        17: [(14, 16), (13, 17)],
        23: [(14, 24), (15, 23)],
        24: [(14, 23), (15, 24)],
        30: [(13, 30), (14, 29)],  # Abajo e izquierda
        31: [(13, 31), (14, 30)],  # Arriba e izquierda
        35: [(15, 35), (14, 34)],  # Abajo y derecha
        36: [(15, 36), (14, 35)]  # Arriba y derecha
    },
    15: {
        -11: [(14, -11), (15, -12)],  # Abajo e izquierda
        -10: [(14, -10), (15, -11)],  # Arriba e izquierda
        -6: [(14, -6), (15, -7)],  # Abajo e izquierda
        -5: [(14, -5), (15, -6)],  # Arriba e izquierda
        -2: [(16, -2), (15, -3)],  # Abajo y derecha
        -1: [(16, -1), (15, -2)],  # Arriba y derecha
        1: [(15, 2), (14, 1)],
        2: [(15, 1), (14, 2)],
        5: [(15, 6), (16, 5)],
        6: [(15, 5), (15, 7), (16, 6)],
        7: [(15, 6)],
        9: [(15, 10), (14, 9)],
        10: [(15, 9), (14, 10)],
        11: [(15, 12), (16, 11)],
        12: [(15, 11), (16, 12)],
        15: [(15, 16)],
        16: [(15, 15), (15, 17), (14, 16)],
        17: [(15, 16), (14, 17)],
        22: [(15, 23)],
        23: [(15, 22), (15, 24), (16, 23)],
        24: [(15, 23), (16, 24)],
        30: [(14, 30), (15, 29)],  # Abajo e izquierda
        31: [(14, 31), (15, 30)],  # Arriba e izquierda
        35: [(16, 35), (15, 34)],  # Abajo y derecha
        36: [(16, 36), (15, 35)]  # Arriba y derecha
    },
    16: {
        -11: [(15, -11), (16, -12)],  # Abajo e izquierda
        -10: [(15, -10), (16, -11)],  # Arriba e izquierda
        -6: [(15, -6), (16, -7)],  # Abajo e izquierda
        -5: [(15, -5), (16, -6)],  # Arriba e izquierda
        -2: [(17, -2), (16, -3)],  # Abajo y derecha
        -1: [(17, -1), (16, -2)],  # Arriba y derecha
        1: [(16, 2), (15, 1)],
        2: [(16, 1), (15, 2)],
        5: [(16, 6), (17, 5)],
        6: [(16, 5), (17, 6)],
        9: [(16, 10), (15, 9)],
        10: [(16, 9), (15, 10)],
        11: [(16, 12), (17, 11)],
        12: [(16, 11), (17, 12)],
        16: [(16, 17), (15, 16)],
        17: [(16, 16), (15, 17)],
        23: [(17, 23)],
        24: [(17, 24)],
        30: [(15, 30), (16, 29)],  # Abajo e izquierda
        31: [(15, 31), (16, 30)],  # Arriba e izquierda
        35: [(17, 35), (16, 34)],  # Abajo y derecha
        36: [(17, 36), (16, 35)]  # Arriba y derecha
    },
    17: {
        -11: [(16, -11), (17, -12)],  # Abajo e izquierda
        -10: [(16, -10), (17, -11)],  # Arriba e izquierda
        -6: [(16, -6), (17, -7)],  # Abajo e izquierda
        -5: [(16, -5), (17, -6)],  # Arriba e izquierda
        -2: [(18, -2), (17, -3)],  # Abajo y derecha
        -1: [(18, -1), (17, -2)],  # Arriba y derecha
        1: [(17, 2), (16, 1)],
        2: [(17, 1), (16, 2)],
        5: [(17, 6), (18, 5)],
        6: [(17, 5), (18, 6)],
        9: [(17, 10), (16, 9)],
        10: [(17, 9), (16, 10)],
        11: [(17, 12), (18, 11)],
        12: [(17, 11), (17, 13), (18, 12)],
        13: [(17, 14), (18, 13)],
        14: [(17, 15), (18, 14)],
        15: [(17, 16), (18, 15)],
        16: [(17, 17), (16, 16), (18, 16)],
        17: [(17, 18), (16, 17), (18, 17)],
        18: [(17, 19), (18, 18)],
        19: [(17, 20), (18, 19)],
        20: [(17, 21), (18, 20)],
        21: [(17, 22), (18, 21)],
        22: [(17, 23)],
        23: [(17, 24), (18, 23)],
        24: [(17, 23), (18, 24)],
        30: [(16, 30), (17, 29)],  # Abajo e izquierda
        31: [(16, 31), (17, 30)],  # Arriba e izquierda
        35: [(18, 35), (17, 34)],  # Abajo y derecha
        36: [(18, 36), (17, 35)]  # Arriba y derecha
    },
    18: {
        -11: [(17, -11), (18, -12)],  # Abajo e izquierda
        -10: [(17, -10), (18, -11)],  # Arriba e izquierda
        -6: [(17, -6), (18, -7)],  # Abajo e izquierda
        -5: [(17, -5), (18, -6)],  # Arriba e izquierda
        -2: [(19, -2), (18, -3)],  # Abajo y derecha
        -1: [(19, -1), (18, -2)],  # Arriba y derecha
        1: [(18, 2), (17, 1)],
        2: [(18, 1), (17, 2)],
        5: [(18, 6), (19, 5)],
        6: [(18, 5), (19, 6)],
        9: [(18, 10), (17, 9)],
        10: [(18, 9), (17, 10)],
        11: [(18, 12), (19, 11)],
        12: [(18, 11), (18, 13), (19, 12)],
        13: [(18, 14), (17, 13)],
        14: [(18, 15), (17, 14)],
        15: [(18, 16), (17, 15)],
        16: [(18, 17), (17, 16)],
        17: [(18, 18), (17, 17)],
        18: [(18, 19), (17, 18)],
        19: [(18, 20), (17, 19)],
        20: [(18, 21), (17, 20), (19, 20)],
        21: [(18, 22), (17, 21)],
        22: [(18, 23)],
        23: [(18, 24), (19, 23)],
        36: [(19, 36), (18, 35)]  # Arriba y derecha
    },
    19: {
        -11: [(18, -11), (19, -12)],  # Abajo e izquierda
        -10: [(18, -10), (19, -11)],  # Arriba e izquierda
        -6: [(18, -6), (19, -7)],  # Abajo e izquierda
        -5: [(18, -5), (19, -6)],  # Arriba e izquierda
        -2: [(20, -2), (19, -3)],  # Abajo y derecha
        -1: [(20, -1), (19, -2)],  # Arriba y derecha
        1: [(19, 2), (18, 1)],
        2: [(19, 1), (18, 2)],
        5: [(19, 6), (20, 5)],
        6: [(19, 5), (20, 6)],
        9: [(19, 10), (18, 9)],
        10: [(19, 9), (18, 10)],
        11: [(19, 12), (20, 11)],
        12: [(19, 11), (20, 12)],
        20: [(18, 20)],
        23: [(19, 24), (20, 23)],
        24: [(19, 23), (20, 24)],
        30: [(18, 30), (19, 29)],  # Abajo e izquierda
        31: [(18, 31), (19, 30)],  # Arriba e izquierda
        35: [(20, 35), (19, 34)],  # Abajo y derecha
        36: [(20, 36), (19, 35)]  # Arriba y derecha
    },
    20: {
        -11: [(19, -11), (20, -12)],  # Abajo e izquierda
        -10: [(19, -10), (20, -11)],  # Arriba e izquierda
        -6: [(19, -6), (20, -7)],  # Abajo e izquierda
        -5: [(19, -5), (20, -6)],  # Arriba e izquierda
        -2: [(21, -2), (20, -3)],  # Abajo y derecha
        -1: [(21, -1), (20, -2)],  # Arriba y derecha
        1: [(20, 2), (19, 1)],
        2: [(20, 1), (19, 2)],
        5: [(20, 6), (21, 5)],
        6: [(20, 5), (21, 6)],
        8: [(20, 9)],
        9: [(20, 8), (20, 10), (19, 9)],
        10: [(20, 9), (19, 10)],
        11: [(20, 12), (21, 11)],
        12: [(20, 11), (20, 13), (21, 12)],
        13: [(20, 12)],
        23: [(20, 24), (21, 23)],
        24: [(20, 23), (21, 24)],
        30: [(19, 30), (20, 29)],  # Abajo e izquierda
        31: [(19, 31), (20, 30)],  # Arriba e izquierda
        35: [(21, 35), (20, 34)],  # Abajo y derecha
        36: [(21, 36), (20, 35)]  # Arriba y derecha
    },
    21: {
        -11: [(20, -11), (21, -12)],  # Abajo e izquierda
        -10: [(20, -10), (21, -11)],  # Arriba e izquierda
        -6: [(20, -6), (21, -7)],  # Abajo e izquierda
        -5: [(20, -5), (21, -6)],  # Arriba e izquierda
        -2: [(22, -2), (21, -3)],  # Abajo y derecha
        -1: [(22, -1), (21, -2)],  # Arriba y derecha
        1: [(21, 2), (20, 1)],
        2: [(21, 1), (21, 3), (20, 2)],
        3: [(21, 2)],
        5: [(21, 6), (22, 5)],
        6: [(21, 5), (22, 6)],
        9: [(21, 10), (20, 9)],
        10: [(21, 9), (20, 10)],
        11: [(21, 12), (22, 11)],
        12: [(21, 11), (22, 12)],
        22: [(21, 23)],
        23: [(21, 22), (21, 24), (22, 23)],
        24: [(21, 23), (22, 24)],
        30: [(20, 30), (21, 29)],  # Abajo e izquierda
        31: [(20, 31), (21, 30)],  # Arriba e izquierda
        35: [(22, 35), (21, 34)],  # Abajo y derecha
        36: [(22, 36), (21, 35)]  # Arriba y derecha
    },
    22: {
        -11: [(21, -11), (22, -12)],  # Abajo e izquierda
        -10: [(21, -10), (22, -11)],  # Arriba e izquierda
        -6: [(21, -6), (22, -7)],  # Abajo e izquierda
        -5: [(21, -5), (22, -6)],  # Arriba e izquierda
        -2: [(23, -2), (22, -3)],  # Abajo y derecha
        -1: [(23, -1), (22, -2)],  # Arriba y derecha
        1: [(22, 2), (21, 1)],
        2: [(22, 1), (21, 2)],
        5: [(23, 5)],
        6: [(23, 6)],
        9: [(22, 10), (21, 9)],
        10: [(22, 9), (21, 10)],
        11: [(23, 11)],
        12: [(23, 12)],
        17: [(23, 17)],
        23: [(22, 24), (23, 23)],
        24: [(22, 23), (23, 24)],
        30: [(21, 30), (22, 29)],  # Abajo e izquierda
        31: [(21, 31), (22, 30)],  # Arriba e izquierda
        35: [(23, 35), (22, 34)],  # Abajo y derecha
        36: [(23, 36), (22, 35)]  # Arriba y derecha
    },
    23: {
        -11: [(22, -11), (23, -12)],  # Abajo e izquierda
        -10: [(22, -10), (23, -11)],  # Arriba e izquierda
        -6: [(22, -6), (23, -7)],  # Abajo e izquierda
        -5: [(22, -5), (23, -6)],  # Arriba e izquierda
        -2: [(24, -2), (23, -3)],  # Abajo y derecha
        -1: [(24, -1), (23, -2)],  # Arriba y derecha
        1: [(23, 2), (22, 1)],
        2: [(23, 1), (22, 2)],
        3: [(23, 2), (24, 3)],
        4: [(23, 3), (24, 4)],
        5: [(23, 4), (24, 5)],
        6: [(23, 5), (24, 6)],
        7: [(23, 6)],
        8: [(23, 7), (24, 8)],
        9: [(23, 8), (22, 9), (24, 9)],
        10: [(23, 9), (22, 10), (24, 10)],
        11: [(23, 10), (24, 11)],
        12: [(23, 11), (24, 12)],
        13: [(23, 12)],
        14: [(23, 13), (24, 14)],
        15: [(23, 14), (24, 15)],
        16: [(23, 15), (24, 16)],
        17: [(23, 16), (24, 17)],
        18: [(23, 17), (24, 18)],
        19: [(23, 18), (24, 19)],
        20: [(23, 19), (24, 20)],
        21: [(23, 20), (24, 21)],
        22: [(23, 21), (24, 22)],
        23: [(23, 22), (23, 24), (24, 23)],
        24: [(23, 23), (24, 24)],
        30: [(22, 30), (23, 29)],  # Abajo e izquierda
        31: [(22, 31), (23, 30)],  # Arriba e izquierda
        35: [(24, 35), (23, 34)],  # Abajo y derecha
        36: [(24, 36), (23, 35)]  # Arriba y derecha
    },
    24: {
        -11: [(23, -11), (24, -12)],  # Abajo e izquierda
        -10: [(23, -10), (24, -11)],  # Arriba e izquierda
        -6: [(23, -6), (24, -7)],  # Abajo e izquierda
        -5: [(23, -5), (24, -6)],  # Arriba e izquierda
        -2: [(25, -2), (24, -3)],  # Abajo y derecha
        -1: [(25, -1), (24, -2)],  # Arriba y derecha
        1: [(24, 2), (23, 1)],
        2: [(24, 1), (23, 2)],
        3: [(24, 2), (23, 3)],
        4: [(24, 3), (23, 4)],
        5: [(24, 4), (23, 5)],
        6: [(24, 5), (23, 6)],
        7: [(24, 6)],
        8: [(24, 7), (23, 8)],
        9: [(24, 8), (23, 9)],
        10: [(24, 9), (23, 10)],
        11: [(24, 10), (23, 11)],
        12: [(24, 11), (23, 12)],
        13: [(24, 12)],
        14: [(24, 13), (23, 14)],
        15: [(24, 14), (23, 15)],
        16: [(24, 15), (23, 16)],
        17: [(24, 16), (23, 17)],
        18: [(24, 17), (23, 18)],
        19: [(24, 18), (23, 19)],
        20: [(24, 19), (23, 20)],
        21: [(24, 20), (23, 21)],
        22: [(24, 21), (23, 22)],
        23: [(24, 22), (24, 24)],
        24: [(24, 23)],
        30: [(23, 30), (24, 29)],  # Abajo e izquierda
        31: [(23, 31), (24, 30)],  # Arriba e izquierda
        35: [(25, 35), (24, 34)],  # Abajo y derecha
        36: [(25, 36), (24, 35)]  # Arriba y derecha
    },
    25: {
        -11: [(24, -11), (25, -12)],  # Abajo e izquierda
        -10: [(24, -10), (25, -11), (25, -9)],  # Arriba, abajo e izquierda
        -9: [(26, -9), (25, -10)],  # Abajo y derecha
        -8: [(26, -8), (25, -9)],  # Abajo y derecha
        -7: [(26, -7), (25, -8)],  # Abajo y derecha
        -6: [(24, -6), (26, -6), (25, -7)],  # Izquierda, derecha y abajo
        -5: [(24, -5), (26, -5), (25, -6)],  # Izquierda, derecha y abajo
        -4: [(26, -4), (25, -5)],  # Abajo y derecha
        -3: [(26, -3), (25, -4)],  # Abajo y derecha
        -2: [(26, -2), (25, -3)],  # Abajo y derecha
        -1: [(26, -1), (25, -2)],  # Arriba y derecha
        9: [(24, 9), (25, 8)],  # Abajo e izquierda
        10: [(24, 10), (25, 9)],  # Arriba e izquierda
        11: [(26, 11), (25, 10)],  # Abajo y derecha
        12: [(26, 12), (25, 11)],  # Arriba y derecha
        30: [(24, 30), (25, 29)],  # Abajo e izquierda
        31: [(24, 31), (25, 30)],  # Arriba e izquierda
        35: [(26, 35), (25, 34)],  # Abajo y derecha
        36: [(26, 36), (25, 35)]  # Arriba y derecha
    },
    26: {
        -11: [(25, -11), (26, -12)],  # Abajo e izquierda
        -10: [(25, -10), (26, -11), (26, -9)],  # Arriba, abajo e izquierda
        -9: [(25, -9), (26, -10)],  # Abajo e izquierda
        -8: [(25, -8), (26, -9)],  # Abajo e izquierda
        -7: [(25, -7), (26, -8)],  # Abajo e izquierda
        -6: [(25, -6), (26, -7)],  # Abajo e izquierda
        -5: [(25, -5), (26, -6)],  # Abajo e izquierda
        -4: [(25, -4), (26, -5)],  # Abajo e izquierda
        -3: [(25, -3), (26, -4)],  # Abajo e izquierda
        -2: [(27, -2), (26, -3)],  # Abajo y derecha
        -1: [(27, -1), (26, -2)],  # Arriba y derecha
        9: [(25, 9), (26, 8)],  # Abajo e izquierda
        10: [(25, 10), (26, 9)],  # Arriba e izquierda
        11: [(27, 11), (26, 10)],  # Abajo y derecha
        12: [(27, 12), (26, 13), (26, 11)],  # Arriba, abajo y derecha
        13: [(27, 13), (26, 12)],  # Abajo y derecha
        14: [(27, 14), (26, 13)],  # Abajo y derecha
        15: [(27, 15), (26, 14)],  # Abajo y derecha
        16: [(27, 16), (26, 15)],  # Abajo y derecha
        17: [(27, 17), (26, 16)],  # Abajo y derecha
        18: [(27, 18), (26, 17)],  # Abajo y derecha
        19: [(27, 19), (26, 18)],  # Abajo y derecha
        20: [(27, 20), (26, 19)],  # Abajo y derecha
        21: [(27, 21), (26, 20)],  # Abajo y derecha
        22: [(27, 22), (26, 21)],  # Abajo y derecha
        23: [(27, 23), (26, 22)],  # Abajo y derecha
        24: [(27, 24), (26, 23)],  # Abajo y derecha
        25: [(27, 25), (26, 24)],  # Abajo y derecha
        26: [(27, 26), (26, 25)],  # Abajo y derecha
        27: [(27, 27), (26, 26)],  # Abajo y derecha
        28: [(27, 28), (26, 27)],  # Abajo y derecha
        29: [(27, 29), (26, 28)],  # Abajo y derecha
        30: [(25, 30), (27, 30), (26, 29)],  # Abajo, izquierda y derecha
        31: [(25, 31), (27, 31), (26, 30)],  # Abajo, izquierda y derecha
        32: [(27, 32), (26, 31)],  # Abajo y derecha
        33: [(27, 33), (26, 32)],  # Abajo y derecha
        34: [(27, 34), (26, 33)],  # Abajo y derecha
        35: [(27, 35), (26, 34)],  # Abajo y derecha
        36: [(27, 36), (26, 35)]  # Arriba y derecha
    },
    27: {
        -11: [(26, -11), (27, -12)],  # Abajo e izquierda
        -10: [(26, -10), (27, -11)],  # Arriba e izquierda
        -2: [(28, -2), (27, -3)],  # Abajo y derecha
        -1: [(28, -1), (27, -2)],  # Arriba y derecha
        9: [(26, 9), (27, 8)],  # Abajo e izquierda
        10: [(26, 10), (27, 9)],  # Arriba e izquierda
        11: [(28, 11), (27, 10)],  # Arriba y derecha
        12: [(28, 12), (27, 13), (27, 11)],  # Arriba, abajo y derecha
        13: [(26, 13), (27, 12)],  # Abajo e izquierda
        14: [(26, 14), (27, 13)],  # Abajo e izquierda
        15: [(26, 15), (27, 14)],  # Abajo e izquierda
        16: [(26, 16), (27, 15)],  # Abajo e izquierda
        17: [(26, 17), (27, 16)],  # Abajo e izquierda
        18: [(26, 18), (27, 17)],  # Abajo e izquierda
        19: [(26, 19), (27, 18)],  # Abajo e izquierda
        20: [(26, 20), (27, 19)],  # Abajo e izquierda
        21: [(26, 21), (27, 20)],  # Abajo e izquierda
        22: [(26, 22), (27, 21)],  # Abajo e izquierda
        23: [(26, 23), (27, 22)],  # Abajo e izquierda
        24: [(26, 24), (27, 23)],  # Abajo e izquierda
        25: [(26, 25), (27, 24)],  # Abajo e izquierda
        26: [(26, 26), (27, 25)],  # Abajo e izquierda
        27: [(26, 27), (27, 26)],  # Abajo e izquierda
        28: [(26, 28), (27, 27)],  # Abajo e izquierda
        29: [(26, 29), (27, 28)],  # Abajo e izquierda
        30: [(26, 30), (27, 29)],  # Abajo e izquierda
        31: [(26, 31), (27, 30)],  # Abajo e izquierda
        32: [(26, 32), (27, 31)],  # Abajo e izquierda
        33: [(26, 33), (27, 32)],  # Abajo e izquierda
        34: [(26, 34), (27, 33)],  # Abajo e izquierda
        35: [(28, 35), (27, 34)],  # Abajo y derecha
        36: [(28, 36), (27, 35)]  # Arriba y derecha
    },
    28: {
        -11: [(27, -11), (28, -12)],  # Abajo e izquierda
        -10: [(27, -10), (28, -11)],  # Arriba e izquierda
        -2: [(29, -2), (28, -3)],  # Abajo y derecha
        -1: [(29, -1), (28, -2)],  # Arriba y derecha
        9: [(27, 9), (28, 8)],  # Abajo e izquierda
        10: [(27, 10), (28, 9)],  # Arriba e izquierda
        11: [(29, 11), (28, 10)],  # Arriba y derecha
        12: [(29, 12), (28, 13), (28, 11)],  # Arriba, abajo y derecha
        35: [(29, 35), (28, 34)],  # Abajo y derecha
        36: [(29, 36), (28, 35)]  # Arriba y derecha
    },
    29: {
        -11: [(28, -11), (29, -12)],  # Abajo e izquierda
        -10: [(28, -10), (29, -11)],  # Arriba e izquierda
        -2: [(30, -2), (29, -3)],  # Abajo y derecha
        -1: [(30, -1), (29, -2)],  # Arriba y derecha
        9: [(28, 9), (29, 8)],  # Abajo e izquierda
        10: [(28, 10), (29, 9)],  # Arriba e izquierda
        11: [(30, 11), (29, 10)],  # Arriba y derecha
        12: [(30, 12), (29, 13), (29, 11)],  # Arriba, abajo y derecha
        35: [(30, 35), (29, 34)],  # Abajo y derecha
        36: [(30, 36), (29, 35)]  # Arriba y derecha
    },
    30: {
        -11: [(29, -11), (30, -12)],  # Abajo e izquierda
        -10: [(29, -10), (30, -11)],  # Arriba e izquierda
        -2: [(31, -2), (30, -3)],  # Abajo y derecha
        -1: [(31, -1), (30, -2)],  # Arriba y derecha
        9: [(29, 9), (30, 8)],  # Abajo e izquierda
        10: [(29, 10), (30, 9)],  # Arriba e izquierda
        11: [(31, 11), (30, 10)],  # Arriba y derecha
        12: [(31, 12), (30, 13), (30, 11)],  # Arriba, abajo y derecha
        35: [(31, 35), (30, 34)],  # Abajo y derecha
        36: [(31, 36), (30, 35)]  # Arriba y derecha
    },
    31: {
        -11: [(30, -11), (31, -12)],  # Abajo e izquierda
        -10: [(30, -10), (31, -11)],  # Arriba e izquierda
        -2: [(32, -2), (31, -3)],  # Abajo y derecha
        -1: [(32, -1), (31, -2), (31, 0)],  # Arriba, abajo y derecha
        0: [(32, 0), (31, -1)],  # Abajo y derecha
        1: [(32, 1), (31, 0)],  # Abajo y derecha
        2: [(32, 2), (31, 1)],  # Abajo y derecha
        3: [(32, 3), (31, 2)],  # Abajo y derecha
        4: [(32, 4), (31, 3)],  # Abajo y derecha
        5: [(32, 5), (31, 4)],  # Abajo y derecha
        6: [(32, 6), (31, 5)],  # Abajo y derecha
        7: [(32, 7), (31, 6)],  # Abajo y derecha
        8: [(32, 8), (31, 7)],  # Abajo y derecha
        9: [(30, 9), (31, 8)],  # Abajo e izquierda
        10: [(30, 10), (31, 9)],  # Arriba e izquierda
        11: [(32, 11), (31, 10)],  # Abajo y derecha
        12: [(32, 12), (31, 11)],  # Arriba y derecha
        35: [(32, 35), (31, 34)],  # Abajo y derecha
        36: [(32, 36), (31, 35)]  # Arriba y derecha
    },
    32: {
        -11: [(31, -11), (32, -12)],  # Abajo e izquierda
        -10: [(31, -10), (32, -11)],  # Arriba e izquierda
        -2: [(33, -2), (32, -3)],  # Abajo y derecha
        -1: [(33, -1), (32, -2), (32, 0)],  # Arriba, abajo y derecha
        0: [(31, 0), (32, -1)],  # Abajo e izquierda
        1: [(31, 1), (32, 0)],  # Abajo e izquierda
        2: [(31, 2), (32, 1)],  # Abajo e izquierda
        3: [(31, 3), (32, 2)],  # Abajo e izquierda
        4: [(31, 4), (32, 3)],  # Abajo e izquierda
        5: [(31, 5), (32, 4)],  # Abajo e izquierda
        6: [(31, 6), (32, 5)],  # Abajo e izquierda
        7: [(31, 7), (32, 6)],  # Abajo e izquierda
        8: [(31, 8), (32, 7)],  # Abajo e izquierda
        9: [(31, 9), (32, 8)],  # Abajo e izquierda
        10: [(31, 10), (32, 9)],  # Arriba e izquierda
        11: [(33, 11), (32, 10)],  # Abajo y derecha
        12: [(33, 12), (32, 11)],  # Arriba y derecha
        35: [(33, 35), (32, 34)],  # Abajo y derecha
        36: [(33, 36), (32, 35)]  # Arriba y derecha
    },
    33: {
        -11: [(32, -11), (33, -12)],  # Abajo e izquierda
        -10: [(32, -10), (33, -11)],  # Arriba e izquierda
        -2: [(34, -2), (33, -3)],  # Abajo y derecha
        -1: [(34, -1), (33, -2)],  # Arriba y derecha
        9: [(32, 9), (33, 8)],  # Abajo e izquierda
        10: [(32, 10), (33, 9)],  # Arriba e izquierda
        11: [(34, 11), (33, 10)],  # Abajo y derecha
        12: [(34, 12), (33, 11)],  # Arriba y derecha
        35: [(34, 35), (33, 34)],  # Abajo y derecha
        36: [(34, 36), (33, 35)]  # Arriba y derecha
    },
    34: {
        -11: [(33, -11), (34, -12)],  # Abajo e izquierda
        -10: [(33, -10), (34, -11)],  # Arriba e izquierda
        -2: [(35, -2), (34, -3)],  # Abajo y derecha
        -1: [(35, -1), (34, -2)],  # Arriba y derecha
        9: [(33, 9), (34, 8)],  # Abajo e izquierda
        10: [(33, 10), (34, 9)],  # Arriba e izquierda
        11: [(35, 11), (34, 10)],  # Abajo y derecha
        12: [(35, 12), (34, 11)],  # Arriba y derecha
        35: [(35, 35), (34, 34)],  # Abajo y derecha
        36: [(35, 36), (34, 35)]  # Arriba y derecha
    },
    35: {
        -11: [(34, -11)],  # Solo izquierda
        -10: [(34, -10), (36, -10), (35, -11)],  # Arriba, izquierda y derecha
        -9: [(36, -9), (35, -10)],  # Arriba y derecha
        -8: [(36, -8), (35, -9)],  # Arriba y derecha
        -7: [(36, -7), (35, -8)],  # Arriba y derecha
        -6: [(36, -6), (35, -7)],  # Arriba y derecha
        -5: [(36, -5), (35, -6)],  # Arriba y derecha
        -4: [(36, -4), (35, -5)],  # Arriba y derecha
        -3: [(36, -3), (35, -4)],  # Arriba y derecha
        -2: [(36, -2), (35, -3)],  # Arriba y derecha
        -1: [(36, -1), (35, -2)],  # Arriba y derecha
        0: [(36, 0), (35, -1)],  # Arriba y derecha
        1: [(36, 1), (35, 0)],  # Arriba y derecha
        2: [(36, 2), (35, 1)],  # Arriba y derecha
        3: [(36, 3), (35, 2)],  # Arriba y derecha
        4: [(36, 4), (35, 3)],  # Arriba y derecha
        5: [(36, 5), (35, 4)],  # Arriba y derecha
        6: [(36, 6), (35, 5)],  # Arriba y derecha
        7: [(36, 7), (35, 6)],  # Arriba y derecha
        8: [(36, 8), (35, 7)],  # Arriba y derecha
        9: [(34, 9), (36, 9), (35, 8)],  # Arriba, izquierda y derecha
        10: [(34, 10), (36, 10), (35, 9)],  # Arriba, izquierda y derecha
        11: [(36, 11), (35, 10)],  # Arriba y derecha
        12: [(36, 12), (35, 11)],  # Arriba y derecha
        13: [(36, 13), (35, 12)],  # Arriba y derecha
        14: [(36, 14), (35, 13)],  # Arriba y derecha
        15: [(36, 15), (35, 14)],  # Arriba y derecha
        16: [(36, 16), (35, 15)],  # Arriba y derecha
        17: [(36, 17), (35, 16)],  # Arriba y derecha
        18: [(36, 18), (35, 17)],  # Arriba y derecha
        19: [(36, 19), (35, 18)],  # Arriba y derecha
        20: [(36, 20), (35, 19)],  # Arriba y derecha
        21: [(36, 21), (35, 20)],  # Arriba y derecha
        22: [(36, 22), (35, 21)],  # Arriba y derecha
        23: [(36, 23), (35, 22)],  # Arriba y derecha
        24: [(36, 24), (35, 23)],  # Arriba y derecha
        25: [(36, 25), (35, 24)],  # Arriba y derecha
        26: [(36, 26), (35, 25)],  # Arriba y derecha
        27: [(36, 27), (35, 26)],  # Arriba y derecha
        28: [(36, 28), (35, 27)],  # Arriba y derecha
        29: [(36, 29), (35, 28)],  # Arriba y derecha
        30: [(36, 30), (35, 29)],  # Arriba y derecha
        31: [(36, 31), (35, 30)],  # Arriba y derecha
        32: [(36, 32), (35, 31)],  # Arriba y derecha
        33: [(36, 33), (35, 32)],  # Arriba y derecha
        34: [(36, 34), (35, 33)],  # Arriba y derecha
        35: [(36, 35), (35, 34)],  # Arriba y derecha
        36: [(36, 36), (35, 35)]  # Arriba y derecha
    },
    36: {
        -11: [(35, -11)],  # Solo izquierda
        -10: [(35, -10), (36, -11)],  # Arriba e izquierda
        -9: [(35, -9), (36, -10)],  # Arriba e izquierda
        -8: [(35, -8), (36, -9)],  # Arriba e izquierda
        -7: [(35, -7), (36, -8)],  # Arriba e izquierda
        -6: [(35, -6), (36, -7)],  # Arriba e izquierda
        -5: [(35, -5), (36, -6)],  # Arriba e izquierda
        -4: [(35, -4), (36, -5)],  # Arriba e izquierda
        -3: [(35, -3), (36, -4)],  # Arriba e izquierda
        -2: [(35, -2), (36, -3)],  # Arriba e izquierda
        -1: [(35, -1), (36, -2)],  # Arriba e izquierda
        0: [(35, 0), (36, -1)],  # Arriba e izquierda
        1: [(35, 1), (36, 0)],  # Arriba e izquierda
        2: [(35, 2), (36, 1)],  # Arriba e izquierda
        3: [(35, 3), (36, 2)],  # Arriba e izquierda
        4: [(35, 4), (36, 3)],  # Arriba e izquierda
        5: [(35, 5), (36, 4)],  # Arriba e izquierda
        6: [(35, 6), (36, 5)],  # Arriba e izquierda
        7: [(35, 7), (36, 6)],  # Arriba e izquierda
        8: [(35, 8), (36, 7)],  # Arriba e izquierda
        9: [(35, 9), (36, 8)],  # Arriba e izquierda
        10: [(35, 10), (36, 9)],  # Arriba e izquierda
        11: [(35, 11), (36, 10)],  # Arriba e izquierda
        12: [(35, 12), (36, 11)],  # Arriba e izquierda
        13: [(35, 13), (36, 12)],  # Arriba e izquierda
        14: [(35, 14), (36, 13)],  # Arriba e izquierda
        15: [(35, 15), (36, 14)],  # Arriba e izquierda
        16: [(35, 16), (36, 15)],  # Arriba e izquierda
        17: [(35, 17), (36, 16)],  # Arriba e izquierda
        18: [(35, 18), (36, 17)],  # Arriba e izquierda
        19: [(35, 19), (36, 18)],  # Arriba e izquierda
        20: [(35, 20), (36, 19)],  # Arriba e izquierda
        21: [(35, 21), (36, 20)],  # Arriba e izquierda
        22: [(35, 22), (36, 21)],  # Arriba e izquierda
        23: [(35, 23), (36, 22)],  # Arriba e izquierda
        24: [(35, 24), (36, 23)],  # Arriba e izquierda
        25: [(35, 25), (36, 24)],  # Arriba e izquierda
        26: [(35, 26), (36, 25)],  # Arriba e izquierda
        27: [(35, 27), (36, 26)],  # Arriba e izquierda
        28: [(35, 28), (36, 27)],  # Arriba e izquierda
        29: [(35, 29), (36, 28)],  # Arriba e izquierda
        30: [(35, 30), (36, 29)],  # Arriba e izquierda
        31: [(35, 31), (36, 30)],  # Arriba e izquierda
        32: [(35, 32), (36, 31)],  # Arriba e izquierda
        33: [(35, 33), (36, 32)],  # Arriba e izquierda
        34: [(35, 34), (36, 33)],  # Arriba e izquierda
        35: [(36, 34)],  # Solo arriba
        36: [(36, 35)]  # Solo arriba
    }
}

# Código que le suma 12 a todo (el grid queda de 1 a 48 en x y en y)
adjusted_movement_map = {}
for x in movimientos_posibles:
    adjusted_movement_map[x + 12] = {}
    for y in movimientos_posibles[x]:
        adjusted_movement_map[x + 12][y + 12] = []
        for coord in movimientos_posibles[x][y]:
            adjusted_movement_map[x + 12][y + 12].append((coord[0] + 12, coord[1] + 12))

# PARA UNITY USEN ADJUSTED MOVEMENT_MAP

pprint.pprint(adjusted_movement_map)