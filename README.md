# StructKit

A Python toolkit for structural analysis of beams, plane trusses and plane frames using the direct stiffness method.

> **Status:** early development, started October 2026. Only the first building block is in place, and the interface will change as the project grows.

## Why StructKit

Matrix structural analysis is taught in every civil engineering programme, but most students meet it either as hand calculations or as a closed commercial package. StructKit aims to sit in between: a small, readable, scriptable library where every step of the direct stiffness method can be inspected, and where results are checked against textbook solutions.

It is intended for:

- civil engineering students learning matrix methods of structural analysis
- engineers who want a free, transparent tool to check hand calculations or verify results from commercial software

## Roadmap

- [x] Euler–Bernoulli beam element stiffness matrix
- [ ] Global stiffness assembly and support conditions
- [ ] Beam analysis with point loads, distributed loads and applied moments
- [ ] Plane truss elements
- [ ] Plane frame elements
- [ ] Member releases (internal hinges)
- [ ] Support settlement and temperature loads
- [ ] Shear force, bending moment and deflected-shape plots
- [ ] Load combinations as per IS 456 / IS 875 (Part 5)
- [ ] Export of results to CSV and PDF reports
- [ ] Documentation and worked examples

## Validation

Every feature is tested against closed-form solutions or worked textbook examples before it is considered done. The first test, for example, checks the tip deflection and rotation of a cantilever under a point load against PL³/3EI and PL²/2EI.

## Installation (development)

```bash
git clone https://github.com/birajaprasadmishra/structkit.git
cd structkit
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Example

```python
from structkit import beam_element_stiffness

# Steel beam element: E = 200 GPa, I = 8.0e-6 m^4, L = 4 m
k = beam_element_stiffness(E=200e9, I=8.0e-6, L=4.0)
print(k)
```

StructKit does not impose a unit system. Use any consistent set of units, for example N and m, or kN and mm.

## License

MIT. See [LICENSE](LICENSE).

## Author

Biraja Prasad Mishra
