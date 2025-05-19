#!/usr/bin/python3
"""
Module 1-square.
Définit la classe Square avec un attribut privé __size.
"""


class Square:
    """definit un carré par la longueur de son côté (privé)."""

    def __init__(self, size):
        """
        Initialise une instance de Square avec une taille donnée.

        Args:
            size (int): La taille du côté du carré.
        """
        self.__size = size
