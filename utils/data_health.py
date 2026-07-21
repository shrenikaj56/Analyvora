import pandas as pd


# -------------------------
# Basic Dataset Information
# -------------------------

def get_total_rows(df):
    return df.shape[0]


def get_total_columns(df):
    return df.shape[1]


def get_missing_values(df):
    return df.isnull().sum().sum()


def get_duplicate_rows(df):
    return df.duplicated().sum()


def get_numeric_columns(df):
    return len(df.select_dtypes(include=["number"]).columns)


def get_categorical_columns(df):
    return len(df.select_dtypes(include=["object", "category"]).columns)


# -------------------------
# Percentages
# -------------------------

def get_missing_percentage(df):
    total_cells = df.shape[0] * df.shape[1]

    if total_cells == 0:
        return 0

    missing = get_missing_values(df)

    return round((missing / total_cells) * 100, 2)


def get_duplicate_percentage(df):
    total_rows = df.shape[0]

    if total_rows == 0:
        return 0

    duplicates = get_duplicate_rows(df)

    return round((duplicates / total_rows) * 100, 2)


# -------------------------
# Missing Values Table
# -------------------------

def get_missing_table(df):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    missing_df = missing.reset_index()

    missing_df.columns = ["Column", "Missing Values"]

    return missing_df


# -------------------------
# Data Quality Score
# -------------------------

def get_quality_score(df):

    missing = get_missing_percentage(df)
    duplicate = get_duplicate_percentage(df)

    score = 100 - (missing + duplicate)

    if score < 0:
        score = 0

    return round(score, 2)


# -------------------------
# Recommendations
# -------------------------

def get_recommendations(df):

    recommendations = []

    if get_missing_values(df) > 0:
        recommendations.append("⚠ Fill or remove missing values.")

    if get_duplicate_rows(df) > 0:
        recommendations.append("⚠ Remove duplicate rows.")

    if (
        get_missing_values(df) == 0
        and get_duplicate_rows(df) == 0
    ):
        recommendations.append(
            "✅ Dataset looks clean and ready for analysis."
        )

    return recommendations