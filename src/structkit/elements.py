"""Element stiffness matrices."""

from __future__ import annotations

import numpy as np


def beam_element_stiffness(E: float, I: float, L: float) -> np.ndarray:
    """Return the local stiffness matrix of a 2D Euler-Bernoulli beam element.

    The degrees of freedom are ordered ``[v1, theta1, v2, theta2]``: the
    transverse displacement and rotation at node 1, followed by those at
    node 2.

    Parameters
    ----------
    E : float
        Young's modulus of the material.
    I : float
        Second moment of area of the cross-section about the bending axis.
    L : float
        Length of the element.

    Use any consistent set of units, for example N and m, or kN and mm.

    Returns
    -------
    numpy.ndarray
        The 4 x 4 element stiffness matrix.

    Raises
    ------
    ValueError
        If E, I or L is not positive.
    """
    if E <= 0 or I <= 0 or L <= 0:
        raise ValueError("E, I and L must all be positive.")

    c = E * I / L**3
    return c * np.array(
        [
            [12.0, 6.0 * L, -12.0, 6.0 * L],
            [6.0 * L, 4.0 * L**2, -6.0 * L, 2.0 * L**2],
            [-12.0, -6.0 * L, 12.0, -6.0 * L],
            [6.0 * L, 2.0 * L**2, -6.0 * L, 4.0 * L**2],
        ]
    )
