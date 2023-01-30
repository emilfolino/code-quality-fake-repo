"""
Contains data about countries Fossil CO2 emission (in megaton, multiply with 1 000 000),
area (in KM2) and population size.
There is one dictionary for each year of emission data, emission_1990, emission_2005 and emission_2017.
Each dictionary contain a key and value pair.
The key is an integer id that can be connected to a country in the dictionary "country_data".
The value is that countries CO2 emission (in megaton) for that year, 1990, 2005 or 2017 depending on
the variable with corresponding name.

Example:
emission_1990 = {
    0: 2.546,
    1: 6.583,
}

The variable `country_data` is a nested dictionary, meaning a dictionary inside a dictionary.
Each countries data is a dictionary inside the dictionary. The country name is the key and the value is
a dictionary that has the follwing keys id, area and population. "id" is used to connect the key from
the emission dictionaries to a country. "area" is the countries area in KM2 and population is a
tuple with three elements. The first element is the population data for 1990, second is for 2005 and
the last is for 2017.

Example:
country_data = {
    'Afghanistan':
    {
        'area': 652864.0,
        'id': 0,
        'population': (12412311, 25654274, 36296111)
    },
    'Albania':
    {
        'area': 28748.0,
        'id': 1,
        'population': (3286070, 3086810, 2884169)
    },
}

Sources:
emission data:
    https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions#Fossil_CO2_emissions_by_country/region
Country area: https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2015
Population size:
    https://www.populationpyramid.net/population-size-per-country/1990/
    https://www.populationpyramid.net/population-size-per-country/2005/
    https://www.populationpyramid.net/population-size-per-country/2017/
    https://data.worldbank.org/indicator/SP.POP.TOTL?locations=EU
"""
# pylint: disable=bad-continuation
emission_1990 = {0: 2.546,
 1: 6.583,
 2: 65.677,
 3: 5.851,
 4: 0.006,
 5: 0.223,
 6: 112.434,
 7: 20.699,
 8: 0.297,
 9: 275.408,
 10: 62.918,
 11: 58.077,
 12: 1.524,
 13: 11.988,
 14: 13.868,
 15: 0.776,
 16: 109.069,
 17: 115.903,
 18: 0.188,
 19: 0.415,
 20: 0.335,
 21: 0.208,
 22: 6.287,
 23: 24.559,
 24: 2.818,
 25: 228.603,
 26: 0.026,
 27: 3.397,
 28: 82.271,
 29: 0.38,
 30: 0.21,
 31: 0.407,
 32: 7.097,
 33: 455.827,
 34: 0.049,
 35: 0.148,
 36: 0.159,
 37: 0.268,
 38: 32.654,
 39: 2397.048,
 40: 51.919,
 41: 0.049,
 42: 0.902,
 43: 0.043,
 44: 2.913,
 45: 25.164,
 46: 37.109,
 47: 5.474,
 48: 4.54,
 49: 162.835,
 50: 3.441,
 51: 53.705,
 52: 1.101,
 53: 0.033,
 54: 8.024,
 55: 0.13,
 56: 16.119,
 57: 90.783,
 58: 2.633,
 59: 0.097,
 60: 0.214,
 61: 38.467,
 62: 0.602,
 63: 2.39,
 64: 4409.339,
 65: 0.013,
 66: 0.001,
 67: 1.028,
 68: 57.242,
 69: 386.214,
 70: 0.371,
 71: 0.839,
 72: 4.857,
 73: 34.745,
 74: 1018.097,
 75: 3.195,
 76: 0.144,
 77: 79.201,
 78: 0.003,
 79: 0.075,
 80: 0.875,
 81: 3.874,
 82: 1.074,
 83: 0.196,
 84: 0.337,
 85: 1.147,
 86: 2.351,
 87: 34.182,
 88: 71.929,
 89: 2.346,
 90: 605.968,
 91: 162.0,
 92: 206.78,
 93: 69.262,
 94: 32.852,
 95: 35.291,
 96: 430.762,
 97: 3.02,
 98: 7.525,
 99: 1149.4,
 100: 10.208,
 101: 250.382,
 102: 6.467,
 103: 0.02,
 104: 31.414,
 105: 23.696,
 106: 0.211,
 107: 20.141,
 108: 5.977,
 109: 0.1,
 110: 0.416,
 111: 37.143,
 112: 35.314,
 113: 11.75,
 114: 0.982,
 115: 0.7,
 116: 0.457,
 117: 59.225,
 118: 0.065,
 119: 0.383,
 120: 2.352,
 121: 0.944,
 122: 0.684,
 123: 1.191,
 124: 290.355,
 125: 31.957,
 126: 13.151,
 127: 22.386,
 128: 1.183,
 129: 4.401,
 130: 1.542,
 131: 1.066,
 132: 161.447,
 133: 1.623,
 134: 24.006,
 135: 1.945,
 136: 0.875,
 137: 68.581,
 138: 131.365,
 139: 11.189,
 140: 51.454,
 141: 11.884,
 142: 66.27,
 143: 2.155,
 144: 2.735,
 145: 2.307,
 146: 2.263,
 147: 21.039,
 148: 43.623,
 149: 371.139,
 150: 43.672,
 151: 2.064,
 152: 16.291,
 153: 1.01,
 154: 187.142,
 155: 2378.921,
 156: 0.525,
 157: 0.01,
 158: 0.034,
 159: 0.076,
 160: 0.148,
 161: 0.038,
 162: 0.129,
 163: 0.047,
 164: 166.172,
 165: 2.397,
 166: 66.388,
 167: 0.288,
 168: 0.741,
 169: 31.623,
 170: 60.537,
 171: 16.623,
 172: 0.133,
 173: 0.695,
 174: 312.463,
 175: 270.056,
 176: 229.966,
 177: 4.187,
 178: 5.536,
 179: 0.908,
 180: 58.117,
 181: 44.955,
 182: 33.876,
 183: 124.383,
 184: 12.267,
 185: 2.096,
 186: 93.009,
 187: 0.149,
 188: 0.765,
 189: 0.064,
 190: 14.895,
 191: 14.705,
 192: 149.893,
 193: 45.628,
 194: 0.007,
 195: 0.644,
 196: 783.21,
 197: 56.922,
 198: 589.038,
 199: 5085.897,
 200: 3.893,
 201: 123.106,
 202: 0.13,
 203: 109.268,
 204: 20.182,
 205: 0.144,
 206: 6.887,
 207: 2.955,
 208: 17.178}
emission_2005 = {0: 1.063,
 1: 4.196,
 2: 98.197,
 3: 15.975,
 4: 0.014,
 5: 0.283,
 6: 165.429,
 7: 4.542,
 8: 0.47,
 9: 391.59,
 10: 80.994,
 11: 30.485,
 12: 2.068,
 13: 23.388,
 14: 38.834,
 15: 2.162,
 16: 61.396,
 17: 118.708,
 18: 0.44,
 19: 2.839,
 20: 0.284,
 21: 0.515,
 22: 9.998,
 23: 16.89,
 24: 4.465,
 25: 380.765,
 26: 0.032,
 27: 5.174,
 28: 52.032,
 29: 1.038,
 30: 0.307,
 31: 2.686,
 32: 5.52,
 33: 581.267,
 34: 0.227,
 35: 0.188,
 36: 0.246,
 37: 0.383,
 38: 59.747,
 39: 6263.064,
 40: 60.61,
 41: 0.115,
 42: 4.359,
 43: 0.058,
 44: 6.306,
 45: 23.634,
 46: 26.165,
 47: 4.774,
 48: 7.883,
 49: 127.157,
 50: 2.589,
 51: 51.485,
 52: 1.469,
 53: 0.035,
 54: 19.409,
 55: 0.272,
 56: 28.32,
 57: 176.329,
 58: 6.905,
 59: 3.371,
 60: 0.688,
 61: 19.643,
 62: 1.541,
 63: 5.327,
 64: 4249.995,
 65: 0.016,
 66: 0.002,
 67: 2.174,
 68: 58.36,
 69: 408.158,
 70: 0.491,
 71: 0.785,
 72: 6.394,
 73: 4.979,
 74: 837.284,
 75: 7.329,
 76: 0.406,
 77: 104.835,
 78: 0.631,
 79: 0.125,
 80: 1.035,
 81: 11.674,
 82: 1.119,
 83: 0.289,
 84: 0.725,
 85: 2.234,
 86: 7.806,
 87: 41.916,
 88: 59.758,
 89: 3.17,
 90: 1210.754,
 91: 359.989,
 92: 467.905,
 93: 89.103,
 94: 47.277,
 95: 62.149,
 96: 498.205,
 97: 6.392,
 98: 10.631,
 99: 1276.863,
 100: 19.755,
 101: 182.369,
 102: 8.787,
 103: 0.033,
 104: 75.218,
 105: 5.475,
 106: 1.038,
 107: 8.242,
 108: 16.505,
 109: 0.175,
 110: 0.473,
 111: 56.7,
 112: 14.075,
 113: 12.156,
 114: 1.624,
 115: 2.22,
 116: 1.437,
 117: 182.503,
 118: 0.479,
 119: 0.543,
 120: 2.769,
 121: 1.12,
 122: 2.911,
 123: 2.977,
 124: 448.171,
 125: 8.139,
 126: 11.083,
 127: 44.368,
 128: 2.703,
 129: 11.146,
 130: 2.504,
 131: 3.298,
 132: 181.433,
 133: 2.453,
 134: 36.746,
 135: 4.312,
 136: 0.796,
 137: 100.196,
 138: 79.568,
 139: 9.694,
 140: 55.403,
 141: 32.964,
 142: 130.354,
 143: 1.734,
 144: 7.204,
 145: 4.379,
 146: 3.934,
 147: 31.692,
 148: 81.261,
 149: 316.256,
 150: 68.077,
 151: 2.272,
 152: 43.435,
 153: 2.367,
 154: 104.713,
 155: 1733.95,
 156: 0.748,
 157: 0.01,
 158: 0.063,
 159: 0.158,
 160: 0.031,
 161: 0.095,
 162: 0.121,
 163: 0.057,
 164: 339.441,
 165: 5.8,
 166: 61.497,
 167: 0.678,
 168: 0.493,
 169: 42.998,
 170: 42.194,
 171: 18.3,
 172: 0.187,
 173: 0.765,
 174: 433.17,
 175: 514.946,
 176: 368.948,
 177: 14.421,
 178: 10.773,
 179: 1.686,
 180: 55.877,
 181: 47.161,
 182: 25.582,
 183: 269.099,
 184: 3.263,
 185: 5.78,
 186: 225.613,
 187: 0.235,
 188: 1.327,
 189: 0.12,
 190: 34.45,
 191: 23.355,
 192: 246.169,
 193: 52.851,
 194: 0.005,
 195: 1.664,
 196: 354.429,
 197: 122.395,
 198: 561.543,
 199: 5971.571,
 200: 5.483,
 201: 116.386,
 202: 0.063,
 203: 152.464,
 204: 99.231,
 205: 0.227,
 206: 21.768,
 207: 2.457,
 208: 11.388}
emission_2017 = {0: 11.422,
 1: 5.026,
 2: 159.929,
 3: 30.876,
 4: 0.028,
 5: 0.624,
 6: 209.968,
 7: 4.832,
 8: 0.959,
 9: 402.253,
 10: 72.249,
 11: 32.544,
 12: 2.997,
 13: 35.775,
 14: 84.546,
 15: 3.172,
 16: 62.34,
 17: 104.221,
 18: 0.44,
 19: 7.097,
 20: 0.429,
 21: 1.454,
 22: 20.462,
 23: 25.618,
 24: 7.913,
 25: 492.791,
 26: 0.149,
 27: 6.711,
 28: 49.568,
 29: 3.399,
 30: 0.289,
 31: 10.56,
 32: 9.768,
 33: 617.301,
 34: 0.955,
 35: 0.493,
 36: 0.486,
 37: 0.925,
 38: 90.325,
 39: 10877.218,
 40: 74.954,
 41: 0.206,
 42: 5.514,
 43: 0.047,
 44: 8.138,
 45: 17.466,
 46: 31.277,
 47: 7.519,
 48: 7.035,
 49: 109.756,
 50: 3.496,
 51: 33.573,
 52: 1.014,
 53: 0.122,
 54: 23.111,
 55: 0.422,
 56: 39.507,
 57: 258.668,
 58: 7.857,
 59: 2.469,
 60: 0.737,
 61: 17.89,
 62: 1.247,
 63: 14.9,
 64: 3548.345,
 65: 0.038,
 66: 0.002,
 67: 1.44,
 68: 46.846,
 69: 338.193,
 70: 0.719,
 71: 0.636,
 72: 6.564,
 73: 11.558,
 74: 796.529,
 75: 18.626,
 76: 0.627,
 77: 72.145,
 78: 0.518,
 79: 0.28,
 80: 2.257,
 81: 17.76,
 82: 2.731,
 83: 0.409,
 84: 1.771,
 85: 3.521,
 86: 10.562,
 87: 44.715,
 88: 50.856,
 89: 4.097,
 90: 2454.774,
 91: 511.327,
 92: 671.45,
 93: 199.296,
 94: 38.914,
 95: 66.916,
 96: 361.176,
 97: 12.505,
 98: 7.546,
 99: 1320.776,
 100: 24.565,
 101: 266.207,
 102: 18.594,
 103: 0.03,
 104: 97.151,
 105: 11.18,
 106: 2.818,
 107: 8.049,
 108: 23.102,
 109: 0.754,
 110: 1.129,
 111: 57.584,
 112: 15.311,
 113: 9.54,
 114: 1.28,
 115: 4.156,
 116: 1.572,
 117: 258.783,
 118: 0.964,
 119: 0.951,
 120: 1.876,
 121: 2.374,
 122: 2.962,
 123: 3.993,
 124: 507.183,
 125: 8.263,
 126: 25.747,
 127: 61.584,
 128: 7.754,
 129: 28.462,
 130: 4.299,
 131: 8.218,
 132: 174.77,
 133: 5.912,
 134: 36.795,
 135: 5.919,
 136: 2.497,
 137: 94.847,
 138: 37.774,
 139: 8.049,
 140: 52.492,
 141: 78.421,
 142: 197.297,
 143: 1.411,
 144: 12.256,
 145: 4.351,
 146: 6.535,
 147: 55.931,
 148: 137.154,
 149: 319.028,
 150: 56.771,
 151: 2.164,
 152: 97.787,
 153: 2.916,
 154: 81.131,
 155: 1764.866,
 156: 1.106,
 157: 0.015,
 158: 0.238,
 159: 0.364,
 160: 0.075,
 161: 0.179,
 162: 0.147,
 163: 0.157,
 164: 638.762,
 165: 9.689,
 166: 62.487,
 167: 0.968,
 168: 1.309,
 169: 55.018,
 170: 37.855,
 171: 15.209,
 172: 0.146,
 173: 0.927,
 174: 467.654,
 175: 673.324,
 176: 282.364,
 177: 23.978,
 178: 21.056,
 179: 2.213,
 180: 50.874,
 181: 39.738,
 182: 28.377,
 183: 279.74,
 184: 5.699,
 185: 14.65,
 186: 279.296,
 187: 0.554,
 188: 2.843,
 189: 0.136,
 190: 37.745,
 191: 31.63,
 192: 429.563,
 193: 72.474,
 194: 0.165,
 195: 5.042,
 196: 205.723,
 197: 202.802,
 198: 379.15,
 199: 5107.393,
 200: 6.93,
 201: 95.35,
 202: 0.091,
 203: 145.877,
 204: 218.729,
 205: 0.276,
 206: 12.503,
 207: 4.967,
 208: 12.087}
country_data = {'Afghanistan': {'area': 652864.0,
                 'id': 0,
                 'population': (12412311, 25654274, 36296111)},
 'Albania': {'area': 28748.0,
             'id': 1,
             'population': (3286070, 3086810, 2884169)},
 'Algeria': {'area': 2381741.0,
             'id': 2,
             'population': (25758872, 33149720, 41389174)},
 'Angola': {'area': 1246700.0,
            'id': 3,
            'population': (11848385, 19433604, 29816769)},
 'Anguilla': {'area': 0, 'id': 4, 'population': []},
 'Antigua and Barbuda': {'area': 440.0,
                         'id': 5,
                         'population': (62533, 81462, 95425)},
 'Argentina': {'area': 2780400.0,
               'id': 6,
               'population': (32618648, 38892924, 43937143)},
 'Armenia': {'area': 29743.0,
             'id': 7,
             'population': (3538164, 2981262, 2944789)},
 'Aruba': {'area': 180.0, 'id': 8, 'population': (62152, 100028, 105361)},
 'Australia': {'area': 7692024.0,
               'id': 9,
               'population': (16960600, 20178543, 24584619)},
 'Austria': {'area': 83879.0,
             'id': 10,
             'population': (7723954, 8253656, 8819902)},
 'Azerbaijan': {'area': 86600.0,
                'id': 11,
                'population': (7242758, 8538610, 9845316)},
 'Bahamas': {'area': 13878.0, 'id': 12, 'population': (256227, 324848, 381749)},
 'Bahrain': {'area': 765.3, 'id': 13, 'population': (495927, 889157, 1494077)},
 'Bangladesh': {'area': 147570.0,
                'id': 14,
                'population': (103171957, 139035505, 159685421)},
 'Barbados': {'area': 439.0, 'id': 15, 'population': (260933, 276320, 286229)},
 'Belarus': {'area': 207595.0,
             'id': 16,
             'population': (10151135, 9562083, 9450233)},
 'Belgium': {'area': 30528.0,
             'id': 17,
             'population': (10006545, 10546885, 11419752)},
 'Belize': {'area': 22966.0, 'id': 18, 'population': (187554, 283798, 375775)},
 'Benin': {'area': 114763.0,
           'id': 19,
           'population': (4978489, 7982223, 11175192)},
 'Bermuda': {'area': 0, 'id': 20, 'population': []},
 'Bhutan': {'area': 38394.0, 'id': 21, 'population': (530801, 648744, 745563)},
 'Bolivia': {'area': 1098581.0,
             'id': 22,
             'population': (6864839, 9232301, 11192853)},
 'Bosnia and Herzegovina': {'area': 51129.0,
                            'id': 23,
                            'population': (4463422, 3765332, 3351534)},
 'Botswana': {'area': 581730.0,
              'id': 24,
              'population': (1286756, 1799077, 2205076)},
 'Brazil': {'area': 881913.0,
            'id': 25,
            'population': (149003225, 186127108, 207833825)},
 'Brunei': {'area': 5765.0, 'id': 27, 'population': (258714, 365112, 424481)},
 'Bulgaria': {'area': 110993.6,
              'id': 28,
              'population': (8841466, 7686964, 7102452)},
 'Burkina Faso': {'area': 274200.0,
                  'id': 29,
                  'population': (8811033, 13421935, 19193236)},
 'Burundi': {'area': 27834.0,
             'id': 30,
             'population': (5438959, 7364857, 10827010)},
 'Cambodia': {'area': 181035.0,
              'id': 31,
              'population': (8975597, 13273355, 16009413)},
 'Cameroon': {'area': 475442.0,
              'id': 32,
              'population': (11780086, 17733408, 24566070)},
 'Canada': {'area': 9984670.0,
            'id': 33,
            'population': (27541323, 32164313, 36732091)},
 'Cape Verde': {'area': 4033.0,
                'id': 34,
                'population': (337953, 463034, 537499)},
 'Cayman Islands': {'area': 0, 'id': 35, 'population': []},
 'Central African Republic': {'area': 622984.0,
                              'id': 36,
                              'population': (2806740, 4038380, 4596023)},
 'Chad': {'area': 1284000.0,
          'id': 37,
          'population': (5963250, 10096630, 15016761)},
 'Chile': {'area': 756096.0,
           'id': 38,
           'population': (13274617, 16182713, 18470435)},
 'China': {'area': 9596961.0,
           'id': 39,
           'population': (1176883681, 1330776380, 1421021794)},
 'Colombia': {'area': 1141748.0,
              'id': 40,
              'population': (33102569, 42647731, 48909844)},
 'Comoros': {'area': 1861.0, 'id': 41, 'population': (411598, 611625, 813890)},
 'Congo': {'area': 342000.0,
           'id': 42,
           'population': (2356740, 3622775, 5110701)},
 'Cook Islands': {'area': 0, 'id': 43, 'population': []},
 'Costa Rica': {'area': 51100.0,
                'id': 44,
                'population': (3119436, 4285504, 4949955)},
 'Croatia': {'area': 56594.0,
             'id': 45,
             'population': (4776370, 4378066, 4182847)},
 'Cuba': {'area': 109884.0,
          'id': 46,
          'population': (10596986, 11261586, 11339255)},
 'Curaçao': {'area': 444.0, 'id': 47, 'population': (146679, 130136, 161986)},
 'Cyprus': {'area': 9251.0, 'id': 48, 'population': (766616, 1027657, 1179685)},
 'Czech Republic': {'area': 78866.0,
                    'id': 49,
                    'population': (10340877, 10258165, 10641032)},
 'Democratic Republic of the Congo': {'area': 2345409.0,
                                      'id': 50,
                                      'population': (34612023,
                                                     54785894,
                                                     81398765)},
 'Denmark': {'area': 42931.0,
             'id': 51,
             'population': (5141117, 5421701, 5732277)},
 'Djibouti': {'area': 23200.0,
              'id': 52,
              'population': (590393, 783248, 944100)},
 'Dominica': {'area': 0, 'id': 53, 'population': []},
 'Dominican Republic': {'area': 48315.0,
                        'id': 54,
                        'population': (7133491, 9097262, 10513111)},
 'East Timor': {'area': 15007.0,
                'id': 55,
                'population': (737814, 995130, 1243260)},
 'Ecuador': {'area': 283561.0,
             'id': 56,
             'population': (10230931, 13825839, 16785356)},
 'Egypt': {'area': 1010408.0,
           'id': 57,
           'population': (56134478, 75523576, 96442590)},
 'El Salvador': {'area': 21041.0,
                 'id': 58,
                 'population': (5270074, 6052124, 6388124)},
 'Equatorial Guinea': {'area': 28050.0,
                       'id': 59,
                       'population': (419188, 749527, 1262008)},
 'Eritrea': {'area': 117600.0,
             'id': 60,
             'population': (2258649, 2826653, 3412894)},
 'Estonia': {'area': 45227.0,
             'id': 61,
             'population': (1565246, 1355650, 1319389)},
 'Ethiopia': {'area': 1104300.0,
              'id': 63,
              'population': (47887864, 76346310, 106399926)},
 'European Union': {'area': 4233262.0,
                    'id': 64,
                    'population': (420477979, 435581949, 446131273)},
 'Falkland Islands': {'area': 0, 'id': 65, 'population': []},
 'Faroe Islands': {'area': 0, 'id': 66, 'population': []},
 'Fiji': {'area': 18274.0, 'id': 67, 'population': (728575, 821606, 877460)},
 'Finland': {'area': 338424.0,
             'id': 68,
             'population': (4996220, 5258933, 5511372)},
 'France': {'area': 640679.0,
            'id': 69,
            'population': (56666861, 61120128, 64842513)},
 'French Guiana': {'area': 83534.0,
                   'id': 70,
                   'population': (115784, 202973, 275189)},
 'French Polynesia': {'area': 4167.0,
                      'id': 71,
                      'population': (199906, 258780, 276108)},
 'Gabon': {'area': 267667.0,
           'id': 72,
           'population': (949493, 1390550, 2064812)},
 'Gambia': {'area': 10689.0,
            'id': 187,
            'population': (955595, 1543745, 2213900)},
 'Georgia': {'area': 69700.0,
             'id': 73,
             'population': (5410400, 4210158, 4008723)},
 'Germany': {'area': 357168.0,
             'id': 74,
             'population': (79053984, 81602739, 82658409)},
 'Ghana': {'area': 239567.0,
           'id': 75,
           'population': (14773274, 21814648, 29121464)},
 'Gibraltar': {'area': 0, 'id': 76, 'population': []},
 'Greece': {'area': 131957.0,
            'id': 77,
            'population': (10225990, 11224800, 10569449)},
 'Greenland': {'area': 0, 'id': 78, 'population': []},
 'Grenada': {'area': 348.0, 'id': 79, 'population': (96328, 104658, 110874)},
 'Guadeloupe': {'area': 1628.0,
                'id': 80,
                'population': (389251, 402903, 399679)},
 'Guatemala': {'area': 108889.0,
               'id': 81,
               'population': (9263820, 13096028, 16914979)},
 'Guinea': {'area': 245836.0,
            'id': 82,
            'population': (6352282, 9109585, 12067516)},
 'Guinea-Bissau': {'area': 36125.0,
                   'id': 83,
                   'population': (975265, 1344931, 1828146)},
 'Guyana': {'area': 214970.0, 'id': 84, 'population': (743306, 746156, 775218)},
 'Haiti': {'area': 27750.0,
           'id': 85,
           'population': (7037915, 9195289, 10982367)},
 'Honduras': {'area': 112492.0,
              'id': 86,
              'population': (4955302, 7458982, 9429016)},
 'Hong Kong': {'area': 2755.0,
               'id': 87,
               'population': (5727942, 6769579, 7306315)},
 'Hungary': {'area': 93030.0,
             'id': 88,
             'population': (10377135, 10085942, 9729822)},
 'Iceland': {'area': 102775.0,
             'id': 89,
             'population': (255044, 294976, 334395)},
 'India': {'area': 3287263.0,
           'id': 90,
           'population': (873277799, 1147609924, 1338676779)},
 'Indonesia': {'area': 1904569.0,
               'id': 91,
               'population': (181413398, 226289468, 264650969)},
 'Iran': {'area': 1648195.0,
          'id': 92,
          'population': (56366212, 69762345, 80673888)},
 'Iraq': {'area': 437072.0,
          'id': 93,
          'population': (17419113, 26922279, 37552789)},
 'Ireland': {'area': 70273.0,
             'id': 94,
             'population': (3510881, 4141218, 4753281)},
 'Israel': {'area': 22072.0,
            'id': 95,
            'population': (4448348, 6529470, 8243849)},
 'Italy': {'area': 301338.0,
           'id': 96,
           'population': (57048237, 58281209, 60673694)},
 'Ivory Coast': {'area': 322463.0,
                 'id': 97,
                 'population': (11924873, 18354513, 24437475)},
 'Jamaica': {'area': 10991.0,
             'id': 98,
             'population': (2419901, 2740000, 2920848)},
 'Japan': {'area': 377972.0,
           'id': 99,
           'population': (124505243, 128326115, 127502728)},
 'Jordan': {'area': 89341.0,
            'id': 100,
            'population': (3565888, 5765639, 9785840)},
 'Kazakhstan': {'area': 2724900.0,
                'id': 101,
                'population': (16383881, 15402803, 18080023)},
 'Kenya': {'area': 580367.0,
           'id': 102,
           'population': (23724574, 36624897, 50221146)},
 'Kiribati': {'area': 811.0, 'id': 103, 'population': (72394, 92319, 114153)},
 'Kuwait': {'area': 17818.0,
            'id': 104,
            'population': (2095350, 2270196, 4056102)},
 'Kyrgyzstan': {'area': 199951.0,
                'id': 105,
                'population': (4372885, 5075340, 6189727)},
 'Laos': {'area': 237955.0,
          'id': 106,
          'population': (4258471, 5751675, 6953031)},
 'Latvia': {'area': 64589.0,
            'id': 107,
            'population': (2664447, 2251996, 1951097)},
 'Lebanon': {'area': 10452.0,
             'id': 108,
             'population': (2803032, 4698761, 6819373)},
 'Lesotho': {'area': 30355.0,
             'id': 109,
             'population': (1703757, 1996115, 2091532)},
 'Liberia': {'area': 111369.0,
             'id': 110,
             'population': (2075917, 3218114, 4702224)},
 'Libya': {'area': 1759541.0,
           'id': 111,
           'population': (4436663, 5798615, 6580723)},
 'Lithuania': {'area': 65300.0,
               'id': 112,
               'population': (3696035, 3344259, 2845419)},
 'Luxembourg': {'area': 2586.0,
                'id': 113,
                'population': (381780, 457848, 591914)},
 'Macao': {'area': 115.3, 'id': 114, 'population': (343816, 482863, 622578)},
 'Macedonia': {'area': 25713.0,
               'id': 139,
               'population': (1996218, 2060280, 2081996)},
 'Madagascar': {'area': 587041.0,
                'id': 115,
                'population': (11598647, 18336722, 25570511)},
 'Malawi': {'area': 118484.0,
            'id': 116,
            'population': (9404499, 12625950, 17670193)},
 'Malaysia': {'area': 330803.0,
              'id': 117,
              'population': (18029824, 25690615, 31104655)},
 'Maldives': {'area': 298.0, 'id': 118, 'population': (223159, 319604, 496398)},
 'Mali': {'area': 1240192.0,
          'id': 119,
          'population': (8449915, 12775509, 18512429)},
 'Malta': {'area': 316.0, 'id': 120, 'population': (362017, 404659, 437935)},
 'Martinique': {'area': 1128.0,
                'id': 121,
                'population': (358457, 397191, 375946)},
 'Mauritania': {'area': 1030000.0,
                'id': 122,
                'population': (2034347, 3024198, 4282582)},
 'Mauritius': {'area': 2040.0,
               'id': 123,
               'population': (1055869, 1222010, 1264497)},
 'Mexico': {'area': 1972550.0,
            'id': 124,
            'population': (83943135, 106005199, 124777326)},
 'Moldova': {'area': 33846.0,
             'id': 125,
             'population': (4365562, 4159296, 4059687)},
 'Mongolia': {'area': 1566000.0,
              'id': 126,
              'population': (2184139, 2526429, 3113788)},
 'Morocco': {'area': 710850.0,
             'id': 127,
             'population': (24807461, 30455563, 35581257)},
 'Mozambique': {'area': 801590.0,
                'id': 128,
                'population': (12987292, 20493927, 28649007)},
 'Myanmar': {'area': 676578.0,
             'id': 129,
             'population': (41335188, 48949931, 53382521)},
 'Namibia': {'area': 825615.0,
             'id': 130,
             'population': (1432899, 1938316, 2402623)},
 'Nepal': {'area': 147181.0,
           'id': 131,
           'population': (18905480, 25744500, 27632682)},
 'Netherlands': {'area': 41543.0,
                 'id': 132,
                 'population': (14965442, 16367153, 17021343)},
 'New Caledonia': {'area': 18576.0,
                   'id': 133,
                   'population': (170335, 236441, 277159)},
 'New Zealand': {'area': 268021.0,
                 'id': 134,
                 'population': (3398175, 4135353, 4702029)},
 'Nicaragua': {'area': 130375.0,
               'id': 135,
               'population': (4173435, 5438692, 6384843)},
 'Niger': {'area': 1267000.0,
           'id': 136,
           'population': (8026592, 13624474, 21602388)},
 'Nigeria': {'area': 923768.0,
             'id': 137,
             'population': (95212454, 138865014, 190873247)},
 'North Korea': {'area': 120540.0,
                 'id': 138,
                 'population': (20293057, 23904167, 25429816)},
 'Norway': {'area': 385203.0,
            'id': 140,
            'population': (4247286, 4632359, 5296324)},
 'Oman': {'area': 309500.0,
          'id': 141,
          'population': (1812158, 2511254, 4665926)},
 'Pakistan': {'area': 8515767.0,
              'id': 142,
              'population': (107647918, 160304007, 207906210)},
 'Palau': {'area': 0, 'id': 143, 'population': []},
 'Panama': {'area': 75417.0,
            'id': 144,
            'population': (2470946, 3330222, 4106764)},
 'Papua New Guinea': {'area': 462840.0,
                      'id': 145,
                      'population': (4615843, 6494902, 8438038)},
 'Paraguay': {'area': 406752.0,
              'id': 146,
              'population': (4223413, 5824095, 6867058)},
 'Peru': {'area': 1285216.0,
          'id': 147,
          'population': (22071433, 27866140, 31444299)},
 'Philippines': {'area': 343448.0,
                 'id': 148,
                 'population': (61895169, 86326251, 105172921)},
 'Poland': {'area': 312679.0,
            'id': 149,
            'population': (37960193, 38368957, 37953176)},
 'Portugal': {'area': 92212.0,
              'id': 150,
              'population': (9895358, 10508494, 10288527)},
 'Puerto Rico': {'area': 9104.0,
                 'id': 151,
                 'population': (3403168, 3631885, 3163676)},
 'Qatar': {'area': 11581.0, 'id': 152, 'population': (476275, 865410, 2724727)},
 'Romania': {'area': 238397.0,
             'id': 154,
             'population': (23489156, 21417287, 19653966)},
 'Russia': {'area': 17075200.0,
            'id': 155,
            'population': (147531562, 143672125, 145530091)},
 'Rwanda': {'area': 26338.0,
            'id': 156,
            'population': (7288883, 8840220, 11980960)},
 'Réunion': {'area': 2511.0, 'id': 153, 'population': (610584, 791598, 876131)},
 'Saint Helena': {'area': 0, 'id': 157, 'population': []},
 'Saint Kitts and Nevis': {'area': 0, 'id': 158, 'population': []},
 'Saint Lucia': {'area': 617.0,
                 'id': 159,
                 'population': (138019, 163408, 180955)},
 'Saint Pierre and Miquelon': {'area': 0, 'id': 160, 'population': []},
 'Saint Vincent and the Grenadines': {'area': 389.0,
                                      'id': 161,
                                      'population': (107489, 108617, 109826)},
 'Samoa': {'area': 2842.0, 'id': 162, 'population': (162797, 179722, 195358)},
 'Sao Tome and Principe': {'area': 1001.0,
                           'id': 163,
                           'population': (119211, 157472, 207086)},
 'Saudi Arabia': {'area': 2149690.0,
                  'id': 164,
                  'population': (16233786, 23816175, 33101183)},
 'Senegal': {'area': 196712.0,
             'id': 165,
             'population': (7526306, 11090123, 15419354)},
 'Serbia and Montenegro': {'area': 91286.0,
                           'id': 166,
                           'population': (9517677, 9193818, 8829623)},
 'Seychelles': {'area': 459.0, 'id': 167, 'population': (70572, 88652, 96418)},
 'Sierra Leone': {'area': 71740.0,
                  'id': 168,
                  'population': (4319763, 5645629, 7488427)},
 'Singapore': {'area': 721.5,
               'id': 169,
               'population': (3012968, 4265693, 5708042)},
 'Slovakia': {'area': 49035.0,
              'id': 170,
              'population': (5288455, 5398962, 5447903)},
 'Slovenia': {'area': 20273.0,
              'id': 171,
              'population': (2006404, 1994979, 2076395)},
 'Solomon Islands': {'area': 28400.0,
                     'id': 172,
                     'population': (311869, 469918, 636030)},
 'Somalia': {'area': 637657.0,
             'id': 173,
             'population': (7225089, 10446856, 14589165)},
 'South Africa': {'area': 1221037.0,
                  'id': 174,
                  'population': (36800507, 47880595, 57009751)},
 'South Korea': {'area': 100210.0,
                 'id': 175,
                 'population': (42918416, 48701069, 51096408)},
 'South Sudan': {'area': 619.0,
                 'id': 178,
                 'population': (5492620, 7535931, 10910774)},
 'Spain': {'area': 505990.0,
           'id': 176,
           'population': (39202524, 44019118, 46647425)},
 'Sri Lanka': {'area': 65610.0,
               'id': 177,
               'population': (17325769, 19544988, 21128028)},
 'Suriname': {'area': 163821.0,
              'id': 179,
              'population': (405169, 499461, 570501)},
 'Swaziland': {'area': 17364.0,
               'id': 62,
               'population': (822423, 1030575, 1124808)},
 'Sweden': {'area': 450295.0,
            'id': 180,
            'population': (8567375, 9038627, 9904895)},
 'Switzerland': {'area': 41285.0,
                 'id': 181,
                 'population': (6652873, 7386818, 8455797)},
 'Syria': {'area': 185180.0,
           'id': 182,
           'population': (12446168, 18361178, 17095669)},
 'Taiwan': {'area': 36197.0,
            'id': 183,
            'population': (20478516, 22705719, 23674546)},
 'Tajikistan': {'area': 143100.0,
                'id': 184,
                'population': (5283811, 6789318, 8880270)},
 'Tanzania': {'area': 947303.0,
              'id': 185,
              'population': (25203848, 38450323, 54660345)},
 'Thailand': {'area': 513120.0,
              'id': 186,
              'population': (56558196, 65416189, 69209817)},
 'Togo': {'area': 56785.0,
          'id': 188,
          'population': (3774310, 5611643, 7698476)},
 'Tonga': {'area': 748.0, 'id': 189, 'population': (95069, 100908, 102002)},
 'Trinidad and Tobago': {'area': 5131.0,
                         'id': 190,
                         'population': (1221121, 1296497, 1384060)},
 'Tunisia': {'area': 163610.0,
             'id': 191,
             'population': (8242509, 10106778, 11433438)},
 'Turkey': {'area': 783356.0,
            'id': 192,
            'population': (53921758, 67903461, 81116451)},
 'Turkmenistan': {'area': 491210.0,
                  'id': 193,
                  'population': (3683978, 4754652, 5757667)},
 'Turks and Caicos Islands': {'area': 0, 'id': 194, 'population': []},
 'Uganda': {'area': 241038.0,
            'id': 195,
            'population': (17354395, 27684590, 41166588)},
 'Ukraine': {'area': 603628.0,
             'id': 196,
             'population': (51463101, 46890775, 44487708)},
 'United Arab Emirates': {'area': 83600.0,
                          'id': 197,
                          'population': (1828437, 4588222, 9487206)},
 'United Kingdom': {'area': 242495.0,
                    'id': 198,
                    'population': (57134377, 60287953, 66727463)},
 'United States of America': {'area': 9833520.0,
                              'id': 199,
                              'population': (252120309, 294993509, 325084758)},
 'Uruguay': {'area': 176215.0,
             'id': 200,
             'population': (3109598, 3321799, 3436645)},
 'Uzbekistan': {'area': 448978.0,
                'id': 201,
                'population': (20398347, 26427785, 31959774)},
 'Vanuatu': {'area': 12189.0,
             'id': 202,
             'population': (146575, 209282, 285499)},
 'Venezuela': {'area': 716445.0,
               'id': 203,
               'population': (19632665, 26432445, 29402480)},
 'Vietnam': {'area': 331230.8,
             'id': 204,
             'population': (67988855, 83832662, 94600643)},
 'Virgin Islands': {'area': 346.0,
                    'id': 26,
                    'population': (103755, 107801, 104745)},
 'Western Sahara': {'area': 266000.0,
                    'id': 205,
                    'population': (217258, 437516, 552617)},
 'Yemen': {'area': 527968.0,
           'id': 206,
           'population': (11709987, 20107416, 27834811)},
 'Zambia': {'area': 752618.0,
            'id': 207,
            'population': (8036849, 11856244, 16853608)},
 'Zimbabwe': {'area': 390757.0,
              'id': 208,
              'population': (10432409, 12076697, 14236599)}}
