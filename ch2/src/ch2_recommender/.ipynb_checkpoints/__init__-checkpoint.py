"""
ch2_recommender

Support code for Chapter 2 – Recommendation Systems
from "A Programmer's Guide to Data Mining".
"""

from .distances import (
    RatingDict,
    shared_items,
    manhattan_distance,
    euclidean_distance,
    minkowski_distance,
    pearson_correlation,
    manhattan_similarity,
    pearson_similarity,
)

from .recommender import (
    neighbours,
    recommend_user_based,
)
