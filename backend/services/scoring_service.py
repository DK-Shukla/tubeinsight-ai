def calculate_health_score(subscribers, views, videos):
    score = (
        min(subscribers / 1_000_000, 40)
        + min(views / 10_000_000, 40)
        + min(videos / 1000, 20)
    )
    return round(score, 2)


def calculate_growth_score(subscribers, views):
    score = (
        min(subscribers / 1_000_000, 50)
        + min(views / 10_000_000, 50)
    )
    return round(score, 2)


def calculate_creator_segment(subscribers):
    if subscribers >= 10_000_000:
        return "Elite Creator"
    elif subscribers >= 1_000_000:
        return "Macro Creator"
    elif subscribers >= 100_000:
        return "Mid Creator"
    else:
        return "Emerging Creator"