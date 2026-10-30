"""Tests for element stiffness matrices."""

import numpy as np
import pytest

from structkit import beam_element_stiffness

E = 200e9  # Pa
I = 8.0e-6  # m^4
L = 4.0  # m


def test_beam_stiffness_is_symmetric():
    k = beam_element_stiffness(E, I, L)
    assert np.allclose(k, k.T)


def test_beam_stiffness_has_two_rigid_body_modes():
    # An unsupported beam element can translate and rotate freely,
    # so its stiffness matrix must have rank 2.
    k = beam_element_stiffness(E, I, L)
    assert np.linalg.matrix_rank(k) == 2


def test_cantilever_tip_load_matches_closed_form():
    # Fix node 1 (v1 = theta1 = 0) and apply a transverse load P at node 2.
    # Textbook results: tip deflection P L^3 / 3EI, tip rotation P L^2 / 2EI.
    P = 10e3  # N
    k = beam_element_stiffness(E, I, L)
    free = [2, 3]
    k_ff = k[np.ix_(free, free)]
    v2, theta2 = np.linalg.solve(k_ff, np.array([P, 0.0]))

    assert v2 == pytest.approx(P * L**3 / (3 * E * I))
    assert theta2 == pytest.approx(P * L**2 / (2 * E * I))


@pytest.mark.parametrize("args", [(0, I, L), (E, -I, L), (E, I, 0)])
def test_non_positive_inputs_are_rejected(args):
    with pytest.raises(ValueError):
        beam_element_stiffness(*args)
