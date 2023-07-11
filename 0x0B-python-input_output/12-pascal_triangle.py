#!/usr/bin/python3
"""Defines a python class student"""

def pascal_triangle(n):
    """Represents a pascal triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        holder = [1]
        for i in range(len(tri) - 1):
            holder.append(tri[i] + tri[i + 1])
        holder.append(1)
        triangles.append(holder)
    return triangles
