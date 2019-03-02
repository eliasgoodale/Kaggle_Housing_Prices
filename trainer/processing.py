FILL_NA_DICT = {
    "Alley": "None",
    "BedroomAbvGr": 0,
    "BsmtQual": "No",
    "BsmtCond": "No",
    "BsmtExposure": "No",
    "BsmtFinType1": "No",
    "BsmtFinType2": "No",
    "BsmtFullBath": 0,
    "BsmtHalfBath": 0,
    "BsmtUnfSF": 0,
    "CentralAir": "N",
    "Condition1": "Norm",
    "Condition2": "Norm",
    "EnclosedPorch": 0,
    "ExterCond": "TA",
    "ExterQual": "TA",
    "Fence": "No",
    "FireplaceQu": "No",
    "Fireplaces": 0,
    "Functional": "Typ",
    "GarageType": "No",
    "GarageFinish": "No",
    "GarageQual": "No",
    "GarageCond": "No",
    "GarageArea": 0,
    "GarageCars": 0,
    "HalfBath": 0,
    "HeatingQC": "TA",
    "KitchenAbvGr": 0,
    "KitchenQual": "TA",
    "LotFrontage": 0,
    "LotShape": "Reg",
    "MasVnrType": "None",
    "MasVnrArea": 0,
    "MiscFeature": "No",
    "MiscVal": 0,
    "OpenPorchSF": 0,
    "PavedDrive": "N",
    "PoolQC": "No",
    "PoolArea": 0,
    "SaleCondition": "Normal",
    "ScreenPorch": 0,
    "TotRmsAbvGrd": 0,
    "Utilities": "AllPub",
    "WoodDeckSF": 0,
}






# feature_name: {number_threshold: category_name, ...}

NUMERIC_COLUMNS_AS_CATEGORIES = {
    
    "MSSubClass": {
        20 : "SC20",
        30 : "SC30",
        40 : "SC40",
        45 : "SC45",
        50 : "SC50",
        60 : "SC60",
        70 : "SC70",
        75 : "SC75",
        80 : "SC80",
        85 : "SC85",
        90 : "SC90",
        120 : "SC120",
        150 : "SC150",
        160 : "SC160",
        180 : "SC180",
        190 : "SC190"
    },

    "MoSold" : {
    1 : "Jan",
    2 : "Feb",
    3 : "Mar",
    4 : "Apr",
    5 : "May",
    6 : "Jun",
    7 : "Jul",
    8 : "Aug",
    9 : "Sep",
    10 : "Oct",
    11 : "Nov",
    12 : "Dec"
    }

}

CATEGORICAL_COLUMNS_AS_NUMBERS = {
    "Alley" : {"Grvl" : 1, "Pave" : 2},
    "BsmtCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
    "BsmtExposure" : {"No" : 0, "Mn" : 1, "Av": 2, "Gd" : 3},
    "BsmtFinType1" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, "ALQ" : 5, "GLQ" : 6},
    "BsmtFinType2" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, "ALQ" : 5, "GLQ" : 6},
    "BsmtQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA": 3, "Gd" : 4, "Ex" : 5},
    "ExterCond" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
    "ExterQual" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
    "FireplaceQu" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
    "Functional" : {"Sal" : 1, "Sev" : 2, "Maj2" : 3, "Maj1" : 4, "Mod": 5, "Min2" : 6, "Min1" : 7, "Typ" : 8},
    "GarageCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
    "GarageQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
    "HeatingQC" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
    "KitchenQual" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
    "LandSlope" : {"Sev" : 1, "Mod" : 2, "Gtl" : 3},
    "LotShape" : {"IR3" : 1, "IR2" : 2, "IR1" : 3, "Reg" : 4},
    "PavedDrive" : {"N" : 0, "P" : 1, "Y" : 2},
    "PoolQC" : {"No" : 0, "Fa" : 1, "TA" : 2, "Gd" : 3, "Ex" : 4},
    "Street" : {"Grvl" : 1, "Pave" : 2},
    "Utilities" : {"ELO" : 1, "NoSeWa" : 2, "NoSewr" : 3, "AllPub" : 4}
}

FEATURE_SIMPLIFICATIONS = {

    "SimplOverallQual": {
        1 : 1, 2 : 1, 3 : 1, # bad  
        4 : 2, 5 : 2, 6 : 2, # average
        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
    },

    "SimplOverallCond": {
        1 : 1, 2 : 1, 3 : 1, # bad
        4 : 2, 5 : 2, 6 : 2, # average
        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
    },

    "SimplPoolQC": {
        1 : 1, 2 : 1, # average
        3 : 2, 4 : 2 # good
    },

    "SimplGarageCond": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplGarageQual": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplFireplaceQu": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplFireplaceQu": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplFunctional": {
        1 : 1, 2 : 1, # bad
        3 : 2, 4 : 2, # major
        5 : 3, 6 : 3, 7 : 3, # minor
        8 : 4 # typical
    },

    "SimplKitchenQual": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplHeatingQC": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplBsmtFinType1": {
        1 : 1, # unfinished
        2 : 1, 3 : 1, # rec room
        4 : 2, 5 : 2, 6 : 2 # living quarters
    },

    "SimplBsmtFinType2": {
        1 : 1, # unfinished
        2 : 1, 3 : 1, # rec room
        4 : 2, 5 : 2, 6 : 2 # living quarters
    },

    "SimplBsmtCond": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplBsmtQual": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplExterCond": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },

    "SimplExterQual": {
        1 : 1, # bad
        2 : 1, 3 : 1, # average
        4 : 2, 5 : 2 # good
    },
}
'''
ENGINEER_FEATURES = {
    # Has Masonry Veneer
    "HasMasVnr": [
        'op': "replace",
        'targets': ["MasVnrType"],
        "inputs": {
            "BrkCmn" : 1, 
            "BrkFace" : 1, 
            "CBlock" : 1, 
            "Stone" : 1, 
            "None" : 0
        },
    ],

    # House completed before sale
    "BoughtOffPlan": [
        {
            'op': 'replace',
            'targets': ['SaleCondition'],
            'inputs': {
                "Abnorml" : 0,
                "Alloca" : 0,
                "AdjLand" : 0,
                "Family" : 0,
                "Normal" : 0,
                "Partial" : 1
            }
        },
    ],

    "OverallGrade":[
        {
            "op": 'multiply',
            'targets': ["OverallQual", "OverallCond"],
        },
    ],

    "GarageGrade":[
        {
            "op": 'multiply'
            "targets": ["GarageQual", "GarageCond"],
        } 

    ]
    "ExterGrade":[
        {
            "op": 'multiply'
            "targets": ["ExterQual", "ExterCond"],
        } 

    ]
    "KitchenScore":[
        {
            "op":
            "targets": ["KitchenAbvGr","KitchenQual"],
        } 

    ]
    "FireplaceScore":[
        {
            "op":
            "targets": ["Fireplaces","FireplaceQu"],
        } 

    ]
    "GarageScore":[
        {
            "op":
            "targets": ["GarageArea","GarageQual"],
        } 

    ]
    "PoolScore":[
        {
            "op":
            "targets": ["PoolArea","PoolQC"],
        } 

    ]
    "SimplOverallGrade":[
        {
            "op":
            "targets": ["SimplOverallQual","SimplOverallCond"],
        } 

    ]
    "SimplExterGrade":[
        {
            "op":
            "targets": ["SimplExterQual","SimplExterCond"],
        } 

    ]
    "SimplPoolScore":[
        {
            "op":
            "targets": ["PoolArea","SimplPoolQC"],
        } 

    ]
    "SimplGarageScore":[
        {
            "op":
            "targets": ["GarageArea","SimplGarageQual"],
        } 

    ]
    "SimplFireplaceScore":[
        {
            "op":
            "targets": ["Fireplaces","SimplFireplaceQu"],
        } 

    ]
    "SimplKitchenScore":[
        {
            "op":
            "targets": ["KitchenAbvGr","SimplKitchenQual"],
        } 

    ]
    "TotalBath":[
        {
            "op":
        } 

    ]
    "AllSF":[
        {
            "op":
        } 

    ]
    "AllFlrsSF":[
        "op": 

    ]
    "AllPorchSF":[
        "op": 

    ]
    }
}

# 2* Combinations of existing features
# Overall quality of the house
train["OverallGrade"] = train["OverallQual"] * train["OverallCond"]
# Overall quality of the garage
train["GarageGrade"] = train["GarageQual"] * train["GarageCond"]
# Overall quality of the exterior
train["ExterGrade"] = train["ExterQual"] * train["ExterCond"]
# Overall kitchen score
train["KitchenScore"] = ["KitchenAbvGr","KitchenQual"]
# Overall fireplace score
train["FireplaceScore"] = ["Fireplaces","FireplaceQu"]
# Overall garage score
train["GarageScore"] = ["GarageArea","GarageQual"]
# Overall pool score
train["PoolScore"] = ["PoolArea","PoolQC"]
# Simplified overall quality of the house
train["SimplOverallGrade"] = ["SimplOverallQual","SimplOverallCond"]
# Simplified overall quality of the exterior
train["SimplExterGrade"] = ["SimplExterQual","SimplExterCond"]
# Simplified overall pool score
train["SimplPoolScore"] = ["PoolArea","SimplPoolQC"]
# Simplified overall garage score
train["SimplGarageScore"] = ["GarageArea","SimplGarageQual"]
# Simplified overall fireplace score
train["SimplFireplaceScore"] = ["Fireplaces","SimplFireplaceQu"]
# Simplified overall kitchen score
train["SimplKitchenScore"] = ["KitchenAbvGr","SimplKitchenQual"]
# Total number of bathrooms
train["TotalBath"] = train["BsmtFullBath"] + (0.5 * train["BsmtHalfBath"]) + \
train["FullBath"] + (0.5 * train["HalfBath"])
# Total SF for house (incl. basement)
train["AllSF"] = train["GrLivArea"] + train["TotalBsmtSF"]
# Total SF for 1st + 2nd floors
train["AllFlrsSF"] = train["1stFlrSF"] + train["2ndFlrSF"]
# Total SF for porch
train["AllPorchSF"] = train["OpenPorchSF"] + train["EnclosedPorch"] + \
train["3SsnPorch"] + train["ScreenPorch"]


# Has masonry veneer or not
train["HasMasVnr"] = train.MasVnrType.replace({"BrkCmn" : 1, "BrkFace" : 1, "CBlock" : 1, 
                                               "Stone" : 1, "None" : 0})
# House completed before sale or not
train["BoughtOffPlan"] = train.SaleCondition.replace({"Abnorml" : 0, "Alloca" : 0, "AdjLand" : 0, 
                                                      "Family" : 0, "Normal" : 0, "Partial" : 1})

'''