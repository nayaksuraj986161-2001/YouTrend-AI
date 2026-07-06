def calculate_kpis(df):

    return {

        "videos": len(df),

        "views": df["views"].sum(),

        "likes": df["likes"].sum(),

        "comments": df["comment_count"].sum(),

        "countries": df["Country"].nunique()

    }


def format_number(value):

    if value >= 1_000_000_000:
        return f"{value/1_000_000_000:.1f}B"

    elif value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"

    elif value >= 1_000:
        return f"{value/1_000:.1f}K"

    else:
        return str(int(value))