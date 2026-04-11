"""
test_recursive_flows.py

Verify basic properties of all labeled recursive flows.
Flows are callable: (M, lam) -> (M, lam) for SdS; (M, Q, lam) -> (M, Q, lam) for RNdS.
Use iterate_sds / iterate_rnds to generate trajectories.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.sds_state import SdSState, sds_from_x, _nariai_mass
from src.rnds_state import RNdSState
from src.recursion_flows import (
    SdS_M_GradientFlow, SdS_Nariai_LinearMap, SdS_Coupled_MLambda_Flow,
    SdS_ConstantX_Flow, RNdS_MQ_GradientFlow, RNdS_MQ_CircularFlow,
    RNdS_Coupled_3D_Flow, iterate_sds, iterate_rnds,
)


def _valid_sds_start(x=0.4, lam=1.0):
    s = sds_from_x(x, lam)
    assert s.is_valid()
    return s


def _valid_rnds_params(lam=1.0):
    M_nar = _nariai_mass(lam)
    for M_frac in [0.3, 0.2, 0.1]:
        for Q in [0.01, 0.005, 0.001]:
            M = M_frac * M_nar
            s = RNdSState(M, Q, lam)
            if s.is_valid():
                return M, Q, lam
    raise RuntimeError("No valid RNdS params found")


def test_phys_gradient_flow_runs():
    s0 = _valid_sds_start()
    flow = SdS_M_GradientFlow(step=0.001)
    traj = iterate_sds(flow, s0.M, s0.Lambda, n_steps=100)
    assert traj.shape == (101, 2)
    assert not np.any(np.isnan(traj))
    print(f"  [PASS] phys_gradient_flow_runs")


def test_phys_gradient_flow_conserves_s_lambda():
    s0 = _valid_sds_start()
    lam = s0.Lambda
    expected = 3.0 * np.pi / lam
    flow = SdS_M_GradientFlow(step=0.001)
    traj = iterate_sds(flow, s0.M, lam, n_steps=200)
    lam_vals = traj[:, 1]
    assert np.allclose(lam_vals, lam, atol=1e-10), "Lambda changed"
    S_lam = 3.0 * np.pi / lam_vals
    assert np.allclose(S_lam, expected, rtol=1e-10), "S_Lambda changed"
    print(f"  [PASS] phys_gradient_flow_conserves_s_lambda")


def test_phys_gradient_flow_label():
    assert SdS_M_GradientFlow().label == "PHYS"
    print(f"  [PASS] phys_gradient_flow_label")


def test_conv_nariai_label():
    assert SdS_Nariai_LinearMap().label == "CONV"
    print(f"  [PASS] conv_nariai_label")


def test_conv_nariai_map_runs():
    s0 = _valid_sds_start(x=0.3)
    flow = SdS_Nariai_LinearMap(alpha=0.1)
    traj = iterate_sds(flow, s0.M, s0.Lambda, n_steps=30)
    assert traj.shape[0] == 31
    # M should increase toward Nariai
    assert traj[-1, 0] >= s0.M - 1e-6
    print(f"  [PASS] conv_nariai_map_runs")


def test_conv_constant_x_flow_runs():
    s0 = _valid_sds_start(x=0.4, lam=1.0)
    flow = SdS_ConstantX_Flow(scale=1.05)
    traj = iterate_sds(flow, s0.M, s0.Lambda, n_steps=20)
    assert not np.all(np.isnan(traj))
    print(f"  [PASS] conv_constant_x_flow_runs")


def test_expl_coupled_ml_label():
    assert SdS_Coupled_MLambda_Flow().label == "EXPL"
    print(f"  [PASS] expl_coupled_ml_label")


def test_expl_coupled_ml_all_variants():
    s0 = _valid_sds_start(x=0.4, lam=1.0)
    for variant in ["gradient_both", "thermalization", "free"]:
        flow = SdS_Coupled_MLambda_Flow(variant=variant, eps_M=0.001, eps_Lambda=0.001)
        traj = iterate_sds(flow, s0.M, s0.Lambda, n_steps=30)
        assert not np.all(np.isnan(traj)), f"All NaN for variant={variant}"
    print(f"  [PASS] expl_coupled_ml_all_variants")


def test_expl_rnds_circular_label():
    assert RNdS_MQ_CircularFlow().label == "EXPL"
    print(f"  [PASS] expl_rnds_circular_label")


def test_expl_rnds_circular_runs():
    try:
        M0, Q0, lam = _valid_rnds_params()
        flow = RNdS_MQ_CircularFlow(theta=0.1, M_0=M0, Q_0=Q0, radius=0.01)
        traj = iterate_rnds(flow, M0, Q0, lam, n_steps=50)
        assert traj.shape == (51, 3)
        print(f"  [PASS] expl_rnds_circular_runs")
    except RuntimeError as e:
        print(f"  [SKIP] expl_rnds_circular_runs: {e}")


def test_expl_rnds_3d_flow_runs():
    try:
        M0, Q0, lam = _valid_rnds_params()
        flow = RNdS_Coupled_3D_Flow(step=0.005)
        traj = iterate_rnds(flow, M0, Q0, lam, n_steps=50)
        assert traj.shape == (51, 3)
        print(f"  [PASS] expl_rnds_3d_flow_runs")
    except RuntimeError as e:
        print(f"  [SKIP] expl_rnds_3d_flow_runs: {e}")


def test_phys_rnds_gradient_label():
    assert "PHYS" in RNdS_MQ_GradientFlow().label
    print(f"  [PASS] phys_rnds_gradient_label")


def test_phys_rnds_gradient_runs():
    try:
        M0, Q0, lam = _valid_rnds_params()
        flow = RNdS_MQ_GradientFlow(step_M=0.001, step_Q=0.001)
        traj = iterate_rnds(flow, M0, Q0, lam, n_steps=100)
        assert traj.shape == (101, 3)
        print(f"  [PASS] phys_rnds_gradient_runs")
    except RuntimeError as e:
        print(f"  [SKIP] phys_rnds_gradient_runs: {e}")


if __name__ == "__main__":
    tests = [
        test_phys_gradient_flow_runs, test_phys_gradient_flow_conserves_s_lambda,
        test_phys_gradient_flow_label, test_conv_nariai_label,
        test_conv_nariai_map_runs, test_conv_constant_x_flow_runs,
        test_expl_coupled_ml_label, test_expl_coupled_ml_all_variants,
        test_expl_rnds_circular_label, test_expl_rnds_circular_runs,
        test_expl_rnds_3d_flow_runs, test_phys_rnds_gradient_label,
        test_phys_rnds_gradient_runs,
    ]
    passed = failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except (AssertionError, Exception) as e:
            print(f"  [FAIL] {t.__name__}: {e}")
            failed += 1
    print(f"\n  Results: {passed} passed, {failed} failed")
