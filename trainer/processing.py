import numpy as np
def processing_fn(df):
    # Handle missing values for features where median/mean or most common value doesn't make sense

    # Alley : data description says NA means "no alley access"
    df.loc[:, "Alley"] = df.loc[:, "Alley"].fillna("None")
    # BedroomAbvGr : NA most likely means 0
    df.loc[:, "BedroomAbvGr"] = df.loc[:, "BedroomAbvGr"].fillna(0)
    # BsmtQual etc : data description says NA for basement features is "no basement"
    df.loc[:, "BsmtQual"] = df.loc[:, "BsmtQual"].fillna("No")
    df.loc[:, "BsmtCond"] = df.loc[:, "BsmtCond"].fillna("No")
    df.loc[:, "BsmtExposure"] = df.loc[:, "BsmtExposure"].fillna("No")
    df.loc[:, "BsmtFinType1"] = df.loc[:, "BsmtFinType1"].fillna("No")
    df.loc[:, "BsmtFinType2"] = df.loc[:, "BsmtFinType2"].fillna("No")
    df.loc[:, "BsmtFullBath"] = df.loc[:, "BsmtFullBath"].fillna(0)
    df.loc[:, "BsmtHalfBath"] = df.loc[:, "BsmtHalfBath"].fillna(0)
    df.loc[:, "BsmtUnfSF"] = df.loc[:, "BsmtUnfSF"].fillna(0)
    # CentralAir : NA most likely means No
    df.loc[:, "CentralAir"] = df.loc[:, "CentralAir"].fillna("N")
    # Condition : NA most likely means Normal
    df.loc[:, "Condition1"] = df.loc[:, "Condition1"].fillna("Norm")
    df.loc[:, "Condition2"] = df.loc[:, "Condition2"].fillna("Norm")
    # EnclosedPorch : NA most likely means no enclosed porch
    df.loc[:, "EnclosedPorch"] = df.loc[:, "EnclosedPorch"].fillna(0)
    # External stuff : NA most likely means average
    df.loc[:, "ExterCond"] = df.loc[:, "ExterCond"].fillna("TA")
    df.loc[:, "ExterQual"] = df.loc[:, "ExterQual"].fillna("TA")
    # Fence : data description says NA means "no fence"
    df.loc[:, "Fence"] = df.loc[:, "Fence"].fillna("No")
    # FireplaceQu : data description says NA means "no fireplace"
    df.loc[:, "FireplaceQu"] = df.loc[:, "FireplaceQu"].fillna("No")
    df.loc[:, "Fireplaces"] = df.loc[:, "Fireplaces"].fillna(0)
    # Functional : data description says NA means typical
    df.loc[:, "Functional"] = df.loc[:, "Functional"].fillna("Typ")
    # GarageType etc : data description says NA for garage features is "no garage"
    df.loc[:, "GarageType"] = df.loc[:, "GarageType"].fillna("No")
    df.loc[:, "GarageFinish"] = df.loc[:, "GarageFinish"].fillna("No")
    df.loc[:, "GarageQual"] = df.loc[:, "GarageQual"].fillna("No")
    df.loc[:, "GarageCond"] = df.loc[:, "GarageCond"].fillna("No")
    df.loc[:, "GarageArea"] = df.loc[:, "GarageArea"].fillna(0)
    df.loc[:, "GarageCars"] = df.loc[:, "GarageCars"].fillna(0)
    # HalfBath : NA most likely means no half baths above grade
    df.loc[:, "HalfBath"] = df.loc[:, "HalfBath"].fillna(0)
    # HeatingQC : NA most likely means typical
    df.loc[:, "HeatingQC"] = df.loc[:, "HeatingQC"].fillna("TA")
    # KitchenAbvGr : NA most likely means 0
    df.loc[:, "KitchenAbvGr"] = df.loc[:, "KitchenAbvGr"].fillna(0)
    # KitchenQual : NA most likely means typical
    df.loc[:, "KitchenQual"] = df.loc[:, "KitchenQual"].fillna("TA")
    # LotFrontage : NA most likely means no lot frontage
    df.loc[:, "LotFrontage"] = df.loc[:, "LotFrontage"].fillna(0)
    # LotShape : NA most likely means regular
    df.loc[:, "LotShape"] = df.loc[:, "LotShape"].fillna("Reg")
    # MasVnrType : NA most likely means no veneer
    df.loc[:, "MasVnrType"] = df.loc[:, "MasVnrType"].fillna("None")
    df.loc[:, "MasVnrArea"] = df.loc[:, "MasVnrArea"].fillna(0)
    # MiscFeature : data description says NA means "no misc feature"
    df.loc[:, "MiscFeature"] = df.loc[:, "MiscFeature"].fillna("No")
    df.loc[:, "MiscVal"] = df.loc[:, "MiscVal"].fillna(0)
    # OpenPorchSF : NA most likely means no open porch
    df.loc[:, "OpenPorchSF"] = df.loc[:, "OpenPorchSF"].fillna(0)
    # PavedDrive : NA most likely means not paved
    df.loc[:, "PavedDrive"] = df.loc[:, "PavedDrive"].fillna("N")
    # PoolQC : data description says NA means "no pool"
    df.loc[:, "PoolQC"] = df.loc[:, "PoolQC"].fillna("No")
    df.loc[:, "PoolArea"] = df.loc[:, "PoolArea"].fillna(0)
    # SaleCondition : NA most likely means normal sale
    df.loc[:, "SaleCondition"] = df.loc[:, "SaleCondition"].fillna("Normal")
    # ScreenPorch : NA most likely means no screen porch
    df.loc[:, "ScreenPorch"] = df.loc[:, "ScreenPorch"].fillna(0)
    # TotRmsAbvGrd : NA most likely means 0
    df.loc[:, "TotRmsAbvGrd"] = df.loc[:, "TotRmsAbvGrd"].fillna(0)
    # Utilities : NA most likely means all public utilities
    df.loc[:, "Utilities"] = df.loc[:, "Utilities"].fillna("AllPub")
    # WoodDeckSF : NA most likely means no wood deck
    df.loc[:, "WoodDeckSF"] = df.loc[:, "WoodDeckSF"].fillna(0)

    df = df.replace({"MSSubClass" : {20 : "SC20", 30 : "SC30", 40 : "SC40", 45 : "SC45", 
                                        50 : "SC50", 60 : "SC60", 70 : "SC70", 75 : "SC75", 
                                        80 : "SC80", 85 : "SC85", 90 : "SC90", 120 : "SC120", 
                                        150 : "SC150", 160 : "SC160", 180 : "SC180", 190 : "SC190"},
                        "MoSold" : {1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun",
                                    7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec"}
                        })
    df = df.replace({"Alley" : {"Grvl" : 1, "Pave" : 2},
                        "BsmtCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "BsmtExposure" : {"No" : 0, "Mn" : 1, "Av": 2, "Gd" : 3},
                        "BsmtFinType1" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, 
                                            "ALQ" : 5, "GLQ" : 6},
                        "BsmtFinType2" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, 
                                            "ALQ" : 5, "GLQ" : 6},
                        "BsmtQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA": 3, "Gd" : 4, "Ex" : 5},
                        "ExterCond" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
                        "ExterQual" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
                        "FireplaceQu" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "Functional" : {"Sal" : 1, "Sev" : 2, "Maj2" : 3, "Maj1" : 4, "Mod": 5, 
                                        "Min2" : 6, "Min1" : 7, "Typ" : 8},
                        "GarageCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "GarageQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "HeatingQC" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "KitchenQual" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "LandSlope" : {"Sev" : 1, "Mod" : 2, "Gtl" : 3},
                        "LotShape" : {"IR3" : 1, "IR2" : 2, "IR1" : 3, "Reg" : 4},
                        "PavedDrive" : {"N" : 0, "P" : 1, "Y" : 2},
                        "PoolQC" : {"No" : 0, "Fa" : 1, "TA" : 2, "Gd" : 3, "Ex" : 4},
                        "Street" : {"Grvl" : 1, "Pave" : 2},
                        "Utilities" : {"ELO" : 1, "NoSeWa" : 2, "NoSewr" : 3, "AllPub" : 4}})
    # Create new features
    # 1* Simplifications of existing features
    df["SimplOverallQual"] = df.OverallQual.replace({1 : 1, 2 : 1, 3 : 1, # bad
                                                        4 : 2, 5 : 2, 6 : 2, # average
                                                        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
                                                        })
    df["SimplOverallCond"] = df.OverallCond.replace({1 : 1, 2 : 1, 3 : 1, # bad
                                                        4 : 2, 5 : 2, 6 : 2, # average
                                                        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
                                                        })
    df["SimplPoolQC"] = df.PoolQC.replace({1 : 1, 2 : 1, # average
                                                3 : 2, 4 : 2 # good
                                                })
    df["SimplGarageCond"] = df.GarageCond.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    df["SimplGarageQual"] = df.GarageQual.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    df["SimplFireplaceQu"] = df.FireplaceQu.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    df["SimplFireplaceQu"] = df.FireplaceQu.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    df["SimplFunctional"] = df.Functional.replace({1 : 1, 2 : 1, # bad
                                                        3 : 2, 4 : 2, # major
                                                        5 : 3, 6 : 3, 7 : 3, # minor
                                                        8 : 4 # typical
                                                        })
    df["SimplKitchenQual"] = df.KitchenQual.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    df["SimplHeatingQC"] = df.HeatingQC.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    df["SimplBsmtFinType1"] = df.BsmtFinType1.replace({1 : 1, # unfinished
                                                            2 : 1, 3 : 1, # rec room
                                                            4 : 2, 5 : 2, 6 : 2 # living quarters
                                                            })
    df["SimplBsmtFinType2"] = df.BsmtFinType2.replace({1 : 1, # unfinished
                                                            2 : 1, 3 : 1, # rec room
                                                            4 : 2, 5 : 2, 6 : 2 # living quarters
                                                            })
    df["SimplBsmtCond"] = df.BsmtCond.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    df["SimplBsmtQual"] = df.BsmtQual.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    df["SimplExterCond"] = df.ExterCond.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    df["SimplExterQual"] = df.ExterQual.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    # 2* Combinations of existing features
    # Overall quality of the house
    df["OverallGrade"] = df["OverallQual"] * df["OverallCond"]
    # Overall quality of the garage
    df["GarageGrade"] = df["GarageQual"] * df["GarageCond"]
    # Overall quality of the exterior
    df["ExterGrade"] = df["ExterQual"] * df["ExterCond"]
    # Overall kitchen score
    df["KitchenScore"] = df["KitchenAbvGr"] * df["KitchenQual"]
    # Overall fireplace score
    df["FireplaceScore"] = df["Fireplaces"] * df["FireplaceQu"]
    # Overall garage score
    df["GarageScore"] = df["GarageArea"] * df["GarageQual"]
    # Overall pool score
    df["PoolScore"] = df["PoolArea"] * df["PoolQC"]
    # Simplified overall quality of the house
    df["SimplOverallGrade"] = df["SimplOverallQual"] * df["SimplOverallCond"]
    # Simplified overall quality of the exterior
    df["SimplExterGrade"] = df["SimplExterQual"] * df["SimplExterCond"]
    # Simplified overall pool score
    df["SimplPoolScore"] = df["PoolArea"] * df["SimplPoolQC"]
    # Simplified overall garage score
    df["SimplGarageScore"] = df["GarageArea"] * df["SimplGarageQual"]
    # Simplified overall fireplace score
    df["SimplFireplaceScore"] = df["Fireplaces"] * df["SimplFireplaceQu"]
    # Simplified overall kitchen score
    df["SimplKitchenScore"] = df["KitchenAbvGr"] * df["SimplKitchenQual"]
    # Total number of bathrooms
    df["TotalBath"] = df["BsmtFullBath"] + (0.5 * df["BsmtHalfBath"]) + \
    df["FullBath"] + (0.5 * df["HalfBath"])
    # Total SF for house (incl. basement)
    df["AllSF"] = df["GrLivArea"] + df["TotalBsmtSF"]
    # Total SF for 1st + 2nd floors
    df["AllFlrsSF"] = df["1stFlrSF"] + df["2ndFlrSF"]
    # Total SF for porch
    df["AllPorchSF"] = df["OpenPorchSF"] + df["EnclosedPorch"] + \
    df["3SsnPorch"] + df["ScreenPorch"]
    # Has masonry veneer or not
    df["HasMasVnr"] = df.MasVnrType.replace({"BrkCmn" : 1, "BrkFace" : 1, "CBlock" : 1, 
                                                "Stone" : 1, "None" : 0})
    # House completed before sale or not
    df["BoughtOffPlan"] = df.SaleCondition.replace({"Abnorml" : 0, "Alloca" : 0, "AdjLand" : 0, 
                                                        "Family" : 0, "Normal" : 0, "Partial" : 1})
    # Create new features
    # 3* Polynomials on the top 10 existing features
    df["OverallQual-s2"] = df["OverallQual"] ** 2
    df["OverallQual-s3"] = df["OverallQual"] ** 3
    df["OverallQual-Sq"] = np.sqrt(df["OverallQual"])
    df["AllSF-2"] = df["AllSF"] ** 2
    df["AllSF-3"] = df["AllSF"] ** 3
    df["AllSF-Sq"] = np.sqrt(df["AllSF"])
    df["AllFlrsSF-2"] = df["AllFlrsSF"] ** 2
    df["AllFlrsSF-3"] = df["AllFlrsSF"] ** 3
    df["AllFlrsSF-Sq"] = np.sqrt(df["AllFlrsSF"])
    df["GrLivArea-2"] = df["GrLivArea"] ** 2
    df["GrLivArea-3"] = df["GrLivArea"] ** 3
    df["GrLivArea-Sq"] = np.sqrt(df["GrLivArea"])
    df["SimplOverallQual-s2"] = df["SimplOverallQual"] ** 2
    df["SimplOverallQual-s3"] = df["SimplOverallQual"] ** 3
    df["SimplOverallQual-Sq"] = np.sqrt(df["SimplOverallQual"])
    df["ExterQual-2"] = df["ExterQual"] ** 2
    df["ExterQual-3"] = df["ExterQual"] ** 3
    df["ExterQual-Sq"] = np.sqrt(df["ExterQual"])
    df["GarageCars-2"] = df["GarageCars"] ** 2
    df["GarageCars-3"] = df["GarageCars"] ** 3
    df["GarageCars-Sq"] = np.sqrt(df["GarageCars"])
    df["TotalBath-2"] = df["TotalBath"] ** 2
    df["TotalBath-3"] = df["TotalBath"] ** 3
    df["TotalBath-Sq"] = np.sqrt(df["TotalBath"])
    df["KitchenQual-2"] = df["KitchenQual"] ** 2
    df["KitchenQual-3"] = df["KitchenQual"] ** 3
    df["KitchenQual-Sq"] = np.sqrt(df["KitchenQual"])
    df["GarageScore-2"] = df["GarageScore"] ** 2
    df["GarageScore-3"] = df["GarageScore"] ** 3
    df["GarageScore-Sq"] = np.sqrt(df["GarageScore"])
    return df