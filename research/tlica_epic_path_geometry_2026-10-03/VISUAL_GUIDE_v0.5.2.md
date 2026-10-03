# TLICA–EPIC v0.5.2 — Visual Guide

## 1. World/content typing

```mermaid
flowchart LR
    Y["WORLD y_wet<br/>wet clothes in dryer"] --> S["SUBSTRATE<br/>cognitive mediation"]
    S --> X["CONTENT x_wet<br/>I encounter wet clothes"]
```

World contact and internal content are different objects.

## 2. Corrected dryer chronology

```mermaid
flowchart LR
    W["prior wake"] -. "candidate pressure contribution" .-> G["low-slack gate state"]
    C["immediate constraints"] -. "candidate pressure contribution" .-> G
    W --> A["anger / urgency"]
    C --> A
    A -. "candidate further pressure" .-> G

    Y["WORLD: wet clothes"] --> S["substrate"]
    S --> X["CONTENT: encounter wet clothes"]

    P["PRIOR: my method normally works"] --> H1["H1: they ran it wrong"]
    X --> H1
    X --> H2["H2: load/heat/time mattered"]

    H1 --> Gate["S = -0.3"]
    H2 --> Gate
    G --> Gate

    Gate --> Auto["REALIZED: automatic blame / re-run"]
    Gate -. "not taken" .-> Probe["run q_chk / q_man first"]
```

The crucial ordering is **precondition first, dryer encounter second**.

## 3. What the read-offs attach to

```text
WORLD ITEMS:
  n_wake, n_constraints, y_wet, n_other
      │
      └── κ/contact lives here and on mediated contact

SUBSTRATE:
  S_som, S_cog
      │
      └── D counts mediation stages into incoming contents

INTERNAL CONTENTS:
  A, x_wet, P, H1, H2
      │
      ├── ρ reads integration from the cogito
      └── φ reads verification-chain closure

TURNAROUND:
  S = M - Pressure
      └── sign selects automatic vs slack-mediated exit
```

## 4. Corrected semantic wake

```mermaid
flowchart LR
    A1["WORLD action 1"] --> S["observer substrate"]
    A2["WORLD action 2"] --> S
    H["WORLD semantic header"] --> S

    S --> a1["content: saw action 1"]
    S --> a2["content: saw action 2"]
    S --> h["content: received header"]

    a1 --> M["reconstructed actor model<br/>wake alone"]
    a2 --> M

    h --> Mh["reconstructed actor model<br/>with header"]

    M -. "q_fit?" .-> U["open φ-chain"]
    Mh --> Q["q_next! → ground"]
```

The actor's mind never appears as a directly contacted node in the observer's diagram.
