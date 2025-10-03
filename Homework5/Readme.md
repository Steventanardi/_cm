# Week 2 – Finite Fields (F_p)

## 1) What is a finite field?
A finite field (Galois field) is a field with finitely many elements. For prime \(p\),
\(\mathbb{F}_p = \{0,1,\dots,p-1\}\) with addition and multiplication modulo \(p\) forms a field.
Both \((\mathbb{F}_p,+)\) and \((\mathbb{F}_p\setminus\{0\},\cdot)\) are abelian groups, and
multiplication distributes over addition.

> AI Q&A link (required by the assignment):  
> https://chatgpt.com/s/t_68dfe2e9d2a8819186d8a5df91de47d6

## 2) Code structure
- `finite_field.py`: field implementation (`Fp`, `FiniteField`) with operator overloading.
- Axiom checkers:
  - `check_group()` verifies group axioms (closure, associativity, identity, inverses, optional commutativity).
  - `check_distributivity()` verifies distributivity of `*` over `+`.

## 3) How the program verifies the axioms
- **Addition group**: runs `check_group(F.all_elements(), add, 0, neg, commutative=True)`.
- **Multiplicative group**: runs `check_group(F.nonzero_elements(), mul, 1, inverse, commutative=True)`.
- **Distributivity**: triple loop over all `a,b,c` in `F` and checks  
  `a*(b+c) == a*b + a*c` and `(b+c)*a == b*a + c*a`.

## 4) How to run
```bash
python finite_field.py
