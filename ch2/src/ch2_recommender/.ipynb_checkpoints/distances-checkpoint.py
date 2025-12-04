"""
Distance and similarity functions for user–item rating data.

Designed to support Chapter 2 exercises from
"A Programmer's Guide to Data Mining".
"""

import math
from typing import Dict, Iterable


# ratings[user][item] = numeric rating (e.g. 1–5)
RatingDict = Dict[str, Dict[str, float]]


def shared_items(ratings: RatingDict, u1: str, u2: str) -> Iterable[str]:
    """
    Return the set of items rated by both u1 and u2.

    If one of the users does not exist in the ratings dictionary,
    a KeyError will be raised (by design, so we notice inconsistent input).
    """
    return set(ratings[u1].keys()).intersection(ratings[u2].keys())


def manhattan_distance(ratings: RatingDict, u1: str, u2: str) -> float:
    """
    Manhattan (L1) distance between two users over shared items.

    If users have no items in common, returns math.inf.
    """
    common = shared_items(ratings, u1, u2)
    if not common:
        return math.inf
    return sum(abs(ratings[u1][i] - ratings[u2][i]) for i in common)


def euclidean_distance(ratings: RatingDict, u1: str, u2: str) -> float:
    """
    Euclidean (L2) distance between two users over shared items.

    If users have no items in common, returns math.inf.
    """
    common = shared_items(ratings, u1, u2)
    if not common:
        return math.inf
    return math.sqrt(sum((ratings[u1][i] - ratings[u2][i]) ** 2 for i in common))


def minkowski_distance(
    ratings: RatingDict,
    u1: str,
    u2: str,
    p: float = 2.0,
) -> float:
    """
    General Minkowski distance between two users over shared items.

    p must be > 0. p=1 gives Manhattan, p=2 gives Euclidean.

    If users have no items in common, returns math.inf.
    """
    if p <= 0:
        raise ValueError("p must be > 0")

    common = shared_items(ratings, u1, u2)
    if not common:
        return math.inf

    return sum(abs(ratings[u1][i] - ratings[u2][i]) ** p for i in common) ** (1.0 / p)


def pearson_correlation(ratings: RatingDict, u1: str, u2: str) -> float:
    """
    Pearson correlation coefficient between two users.

    Returns a value in [-1, 1]. If users have no items in common
    or variance is zero, returns 0.0.
    """
    common = list(shared_items(ratings, u1, u2))
    n = len(common)
    if n == 0:
        return 0.0

    sum1 = sum(ratings[u1][i] for i in common)
    sum2 = sum(ratings[u2][i] for i in common)

    sum1_sq = sum(ratings[u1][i] ** 2 for i in common)
    sum2_sq = sum(ratings[u2][i] ** 2 for i in common)

    product_sum = sum(ratings[u1][i] * ratings[u2][i] for i in common)

    # numerator
    num = product_sum - (sum1 * sum2 / n)

    # denominator
    den = math.sqrt(
        (sum1_sq - (sum1 ** 2) / n) * (sum2_sq - (sum2 ** 2) / n)
    )

    if den == 0:
        return 0.0

    return num / den


def manhattan_similarity(ratings: RatingDict, u1: str, u2: str) -> float:
    """
    Convert Manhattan distance into a similarity score in (0, 1].

    Larger similarity means closer users. If there are no shared items,
    returns 0.0.
    """
    d = manhattan_distance(ratings, u1, u2)
    if d == math.inf:
        return 0.0
    return 1.0 / (1.0 + d)


def pearson_similarity(ratings: RatingDict, u1: str, u2: str) -> float:
    """
    Pearson-based similarity in [0, 1].

    Pearson correlation is in [-1, 1]. Negative correlations are
    mapped to 0.0, positive correlations remain unchanged.
    """
    corr = pearson_correlation(ratings, u1, u2)
    return max(0.0, corr)
