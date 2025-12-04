"""
User-based k-NN recommender functions.

Designed to support Chapter 2 exercises from
"A Programmer's Guide to Data Mining".
"""

import math
from typing import Callable, Dict, Iterable, List, Tuple

from .distances import RatingDict


SimilarityFunc = Callable[[RatingDict, str, str], float]


def neighbours(
    ratings: RatingDict,
    target_user: str,
    similarity_fn: SimilarityFunc,
    top_n: int = 3,
) -> List[Tuple[float, str]]:
    """
    Return top_n neighbours (similarity, user) for target_user.

    Neighbours are sorted in descending order of similarity.
    """
    if target_user not in ratings:
        raise KeyError(f"Unknown user: {target_user}")

    scores: List[Tuple[float, str]] = []

    for other in ratings:
        if other == target_user:
            continue
        sim = similarity_fn(ratings, target_user, other)
        scores.append((sim, other))

    scores.sort(reverse=True, key=lambda x: x[0])
    return scores[:top_n]


def recommend_user_based(
    ratings: RatingDict,
    target_user: str,
    similarity_fn: SimilarityFunc,
    k: int = 3,
    min_sim: float = 0.0,
) -> List[Tuple[float, str]]:
    """
    Recommend items to target_user based on k nearest neighbours.

    Algorithm (standard user-based collaborative filtering):

    1. Find k nearest neighbours of target_user using similarity_fn.
    2. Consider items not yet rated by target_user.
    3. For each candidate item, compute a weighted average of neighbours'
       ratings, where weights are similarity scores.
    4. Return a list of (predicted_rating, item), sorted by predicted_rating
       in descending order.

    Items for which the sum of similarities is zero are ignored.
    """
    if target_user not in ratings:
        raise KeyError(f"Unknown user: {target_user}")

    # 1. Get k neighbours
    neighs = neighbours(ratings, target_user, similarity_fn, top_n=k)

    # 2. Collect candidate items (not yet rated by target_user)
    target_items = set(ratings[target_user].keys())
    all_items = {i for r in ratings.values() for i in r.keys()}
    candidate_items = all_items - target_items

    weighted_scores: Dict[str, float] = {}
    sim_sums: Dict[str, float] = {}

    for sim, other in neighs:
        if sim <= min_sim:
            continue
        for item, rating in ratings[other].items():
            if item in target_items:
                continue
            weighted_scores.setdefault(item, 0.0)
            sim_sums.setdefault(item, 0.0)
            weighted_scores[item] += sim * rating
            sim_sums[item] += sim

    predictions: List[Tuple[float, str]] = []
    for item in candidate_items:
        if item not in weighted_scores:
            continue
        if sim_sums.get(item, 0.0) == 0.0:
            continue
        predicted = weighted_scores[item] / sim_sums[item]
        predictions.append((predicted, item))

    predictions.sort(reverse=True, key=lambda x: x[0])
    return predictions


def distance_matrix(
    ratings: RatingDict,
    distance_fn: Callable[[RatingDict, str, str], float],
    users: Iterable[str] | None = None,
) -> None:
    """
    Utility function for Chapter 2 experiments.

    Print a distance matrix for the given users (or all users
    if users is None), using the supplied distance function.
    """

    if users is None:
        user_list = list(ratings.keys())
    else:
        user_list = list(users)

    # Header
    header = "       " + "  ".join(f"{u:>7}" for u in user_list)
    print("Distance matrix:")
    print(header)

    for u1 in user_list:
        row = [f"{u1:>7}"]
        for u2 in user_list:
            if u1 == u2:
                row.append("   0.00")
            else:
                d = distance_fn(ratings, u1, u2)
                if d == math.inf:
                    row.append("    inf")
                else:
                    row.append(f"{d:7.2f}")
        print("  ".join(row))
