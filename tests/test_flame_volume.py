import pytest
import graphics.flame_volume as mod

CASES = [
    ("fixed_step_integrate", (1,)),
    ("temp_velocity_couple", (1,)),
    ("blackbody_temp_map", (1,)),
    ("per_emitter_volume", (1,)),
    ("queue_barrier", (1,)),
    ("volume_release", (1,)),
    ("load_flame", (1,)),
    ("advect_flame", (1,)),
    ("shade_flame", (1,)),
    ("present_flame", (1,)),
    ("validate_flame", (1,)),
    ("metrics_flame", (1,)),
    ("audit_flame", (1,)),
    ("fallback_flame", (1,)),
    ("determinism_flame", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
