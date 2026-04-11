"""Compatibility wrapper: forward to src.evolution.rnds_state."""
from .evolution.rnds_state import *  # noqa: F401,F403
from .evolution.rnds_state import _rnds_admissible, _rnds_f, _rnds_fprime, _solve_rnds_quartic  # noqa: F401
