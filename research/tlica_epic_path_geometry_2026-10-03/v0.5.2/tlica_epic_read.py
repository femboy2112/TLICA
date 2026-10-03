#!/usr/bin/env python3
"""
tlica_epic_read.py -- reference reader for TLICA-EPIC v0.5.2 diagram serializations.

Pure Python 3 standard library. No third-party packages.

A v0.5 diagram is a list of lines in the text grammar below. This script parses
the lines and computes, for every content node, the four readings that the
diagram is shorthand for:

    rho(x)   identity-correlation   = C/(1+C), C = max-flow from the cogito I to x
                                       over integration wires (per mode k)
    phi(x)   truth-indistinguishability
                                     = 1 - n*delta - eps, where n = number of
                                       verification steps (=>) on the chain from
                                       x to ground, eps = sum over EXECUTED probes
                                       on the chain of mu*(1-q). Undefined if the
                                       chain does not reach ground.
    kappa(x) contact                 = max chi over contact wires into x, or over
                                       the source-map ancestry of x if x has none.
    D(x)     mediation order         = number of substrate vertices on the inbound
                                       path from a world item to x.
    class(x) conscious-clear / conscious-fuzzy / latent / unconscious-operative,
             from (A(x), phi defined?)

Grammar (one statement per line; '#' starts a comment):

    cogito  I
    world   n  "label"
    content x  "label"  [A=0|1]
    claim   c  "label"  [A=0|1]            # a content used only as a chain link
    sub     s  "label"                     # substrate vertex
    (the token Foc may appear in a path; it is focus, not a node)
    tool    g  "label"                     # ground: a verification tool in Tools_t
    wire    u -> v  [k=<mode>] [w=<0..1>]  # integration wire (default k=0, w=1)
    step    u => v                         # one verification step (costs delta)
    probe   q? -> x [mu=<0..1>]            # constructible, NOT executed
    probe   q! -> x [mu=<0..1>] [q=<0..1>] # executed, with result q(x)
    contact n ~> x [chi=<0..1>]            # contact wire from world item n
    path    n -> s1 -> s2 -> I -> x        # inbound mediation path; D = #subs + [I on path]
    event   u -> v [k=] [alpha=] [beta=]   # imprinting event on a wire (applied)
    bridge  u -> v "label"                 # CONJECTURED modulation; never computed
    source  x : n1, n2                      # source map sigma(x) = {world items only}
    gate    X  M=<cap> P=<pressure> [Sp=<perceived>]
                                           # actualization vertex (the turnaround I -> I+).
                                           # S = M - P.  S <= 0: automatic;  S > 0: slack-mediated.
                                           # Sp (perceived slack) optional: Sp <= 0 < S = "stuck but capable".
    act     X -> a  "label" [mode=auto|B]  # outbound: policy -> action. Drawn; only the gate
                                           #   decides which mode is REALIZED this cycle.
    wake    a -> n  "label"                # action leaves a world record (next cycle's input)
    delta   <value>                        # default 0.05

Lower-lane statements (gate/act/wake) are declared, not computed, except the
gate's mode, which is read from the sign of S. Pressure and M are open functions
in the foundation; here they are declared inputs, and the reader says so.

Readings are returned as a dict and printed as a table.
"""
import re
import sys
from collections import defaultdict, deque

DELTA_DEFAULT = 0.05


# ---------------------------------------------------------------- parsing
def _kv(tokens):
    out = {}
    for t in tokens:
        if "=" in t:
            k, v = t.split("=", 1)
            out[k] = v
    return out


def parse(text):
    d = {
        "cogito": None, "world": {}, "content": {}, "sub": {}, "tool": {},
        "A": {}, "wire": [], "step": [], "probe": [], "contact": [],
        "path": [], "event": [], "bridge": [], "source": {}, "delta": DELTA_DEFAULT,
        "gate": {}, "act": [], "wake": [],
    }
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        kind, rest = (line.split(None, 1) + [""])[:2]
        m = re.match(r'(\S+)\s*(?:"([^"]*)")?\s*(.*)', rest)
        if kind == "cogito":
            d["cogito"] = rest.strip()
        elif kind in ("world", "content", "claim", "sub", "tool"):
            name, label, tail = m.group(1), m.group(2) or m.group(1), m.group(3)
            if kind == "claim":           # chain link: a content hidden from the table
                d["content"][name] = label
                d["A"][name] = int(_kv(tail.split()).get("A", 1))
                d.setdefault("hidden", set()).add(name)
                continue
            d[kind][name] = label
            if kind == "content":
                d["A"][name] = int(_kv(tail.split()).get("A", 1))
        elif kind == "wire" or kind == "event":
            u, v, tail = re.match(r"(\S+)\s*->\s*(\S+)\s*(.*)", rest).groups()
            kv = _kv(tail.split())
            if kind == "wire":
                d["wire"].append((u, v, kv.get("k", "0"), float(kv.get("w", 1))))
            else:
                d["event"].append((u, v, kv.get("k", "0"),
                                   float(kv.get("alpha", 0)), float(kv.get("beta", 0))))
        elif kind == "step":
            u, v = re.match(r"(\S+)\s*=>\s*(\S+)", rest).groups()
            d["step"].append((u, v))
        elif kind == "probe":
            q, x, tail = re.match(r"(\S+)\s*->\s*(\S+)\s*(.*)", rest).groups()
            kv = _kv(tail.split())
            d["probe"].append((q, x, q.endswith("!"), float(kv.get("mu", 1)),
                               float(kv.get("q", 0)) if "q" in kv else None))
        elif kind == "contact":
            n, x, tail = re.match(r"(\S+)\s*~>\s*(\S+)\s*(.*)", rest).groups()
            d["contact"].append((n, x, float(_kv(tail.split()).get("chi", 1))))
        elif kind == "path":
            d["path"].append([t.strip() for t in rest.split("->")])
        elif kind == "bridge":
            u, v, label = re.match(r'(\S+)\s*->\s*(\S+)\s*"?([^"]*)"?', rest).groups()
            d["bridge"].append((u, v, label))
        elif kind == "source":
            x, ys = re.match(r"(\S+)\s*:\s*(.*)", rest).groups()
            d["source"][x] = [y.strip() for y in ys.split(",") if y.strip()]
        elif kind == "gate":
            name, tail = (rest.split(None, 1) + [""])[:2]
            kv = _kv(tail.split())
            d["gate"][name] = {"M": float(kv["M"]), "P": float(kv["P"]),
                               "Sp": float(kv["Sp"]) if "Sp" in kv else None}
        elif kind == "act":
            X, a, label, tail = re.match(r'(\S+)\s*->\s*(\S+)\s*"([^"]*)"\s*(.*)', rest).groups()
            d["act"].append((X, a, label, _kv(tail.split()).get("mode", "?")))
        elif kind == "wake":
            a, n, label = re.match(r'(\S+)\s*->\s*(\S+)\s*"?([^"]*)"?', rest).groups()
            d["wake"].append((a, n, label))
        elif kind == "delta":
            d["delta"] = float(rest)
        else:
            raise ValueError("unknown statement: " + raw)
    if d["cogito"] is None:
        raise ValueError("diagram has no cogito leg")
    return d


# ---------------------------------------------------------------- rho
def apply_events(d):
    """Imprinting rule: w <- clip((1-beta) w + alpha (1-w)). Returns wires."""
    wires = {(u, v, k): w for (u, v, k, w) in d["wire"]}
    for (u, v, k, a, b) in d["event"]:
        w = wires.get((u, v, k), 0.0)
        wires[(u, v, k)] = min(1.0, max(0.0, (1 - b) * w + a * (1 - w)))
    return wires


def max_flow(adj, s, t):
    """Edmonds-Karp on a capacity dict adj[u][v]. Returns max-flow s->t."""
    cap = defaultdict(lambda: defaultdict(float))
    for u in adj:
        for v, c in adj[u].items():
            cap[u][v] += c
            cap[v]  # ensure key
    flow = 0.0
    while True:
        parent = {s: None}
        dq = deque([s])
        while dq and t not in parent:
            u = dq.popleft()
            for v, c in cap[u].items():
                if c > 1e-12 and v not in parent:
                    parent[v] = u
                    dq.append(v)
        if t not in parent:
            return flow
        # bottleneck
        f, v = float("inf"), t
        while parent[v] is not None:
            u = parent[v]
            f = min(f, cap[u][v])
            v = u
        v = t
        while parent[v] is not None:
            u = parent[v]
            cap[u][v] -= f
            cap[v][u] += f
            v = u
        flow += f


def rho_readings(d):
    wires = apply_events(d)
    modes = sorted({k for (_, _, k) in wires})
    I = d["cogito"]
    out = {}
    for x in d["content"]:
        vec = {}
        for k in modes:
            adj = defaultdict(dict)
            for (u, v, kk), w in wires.items():
                if kk == k:
                    adj[u][v] = w
            C = max_flow(adj, I, x)
            vec[k] = C / (1 + C)
        out[x] = vec
    return out, modes


# ---------------------------------------------------------------- phi
def phi_readings(d):
    """Follow => steps from x. Chain must end at a tool (ground)."""
    nxt = defaultdict(list)
    for (u, v) in d["step"]:
        nxt[u].append(v)
    exec_probes = defaultdict(list)   # node -> [(mu, q)]
    open_probes = defaultdict(list)   # node -> [mu]
    for (q, x, executed, mu, qval) in d["probe"]:
        if executed:
            exec_probes[x].append((mu, qval if qval is not None else 0.0))
        else:
            open_probes[x].append((q, mu))
    delta = d["delta"]
    out = {}
    for x in d["content"]:
        # BFS shortest chain to any tool
        best = None
        seen = {x: (0, [x])}
        dq = deque([x])
        while dq:
            u = dq.popleft()
            n, chain = seen[u]
            if u in d["tool"]:
                best = (n, chain)
                break
            for v in nxt[u]:
                if v not in seen:
                    seen[v] = (n + 1, chain + [v])
                    dq.append(v)
        if best is None:
            # chain is open; record where it stops and which q? could close it
            tips = [u for u in seen if not nxt[u]]
            pending = [q for u in seen for (q, _) in open_probes.get(u, [])]
            out[x] = {"phi": None, "n": None, "eps": None,
                      "open_at": tips, "pending": pending}
            continue
        n, chain = best
        eps = sum(mu * (1 - qv) for u in chain for (mu, qv) in exec_probes.get(u, []))
        eps = min(eps, 1 - n * delta)  # foundation: eps + n*delta <= 1
        out[x] = {"phi": 1 - n * delta - eps, "n": n, "eps": eps,
                  "chain": chain, "pending": []}
    return out


# ---------------------------------------------------------------- kappa, D
def kappa_readings(d):
    """World-first contact typing.

    Each `contact n ~> x chi=c` declares contact strength κ(n)=c for the
    world item n and direct mediated contact c for content x.  A source map
    `source x : n1, n2` may name WORLD ITEMS only; inherited content-level
    contact is sup κ(n) over those world sources.

    This intentionally rejects the older v0.5 convenience in which σ(x)
    could point to another content node.
    """
    direct_content = defaultdict(float)
    world_contact = defaultdict(float)
    for (n, x, chi) in d["contact"]:
        if n not in d["world"]:
            raise ValueError("contact source must be a declared world item: " + n)
        direct_content[x] = max(direct_content[x], chi)
        world_contact[n] = max(world_contact[n], chi)

    out = {}
    for x in d["content"]:
        if x in direct_content:
            out[x] = direct_content[x]
            continue

        srcs = d["source"].get(x, [])
        bad = [s for s in srcs if s not in d["world"]]
        if bad:
            raise ValueError(
                "source map sigma(%s) must contain world items only; invalid: %s"
                % (x, ", ".join(bad))
            )
        out[x] = max([world_contact.get(s, 0.0) for s in srcs] + [0.0])
    return out


def D_readings(d):
    """Mediation order = (#substrate vertices on the inbound path)
                       + (1 if the path delivers to the cogito I, 0 if it only
                          moves focus (token Foc)).
    This reproduces the foundation's named orders exactly:
        N -> S_sal -> Foc -> x        : 1 + 0 = 1   (salience capture)
        N -> S_cog -> I -> x          : 1 + 1 = 2   (cognitive)
        N -> S_som -> S_cog -> I -> x : 2 + 1 = 3   (somatic-then-cognitive)
    """
    out = {}
    I = d["cogito"]
    for p in d["path"]:
        x = p[-1]
        out[x] = sum(1 for s in p if s in d["sub"]) + (1 if I in p[:-1] else 0)
    return out


# ---------------------------------------------------------------- class
def classify(A, phi):
    if A == 1 and phi is not None:
        return "conscious-clear"
    if A == 1:
        return "conscious-fuzzy"
    if phi is not None:
        return "latent"
    return "unconscious-operative"


# ---------------------------------------------------------------- gate
def gate_readings(d):
    """S = M - Pressure (File 3 s8.11). S <= 0 -> automatic; S > 0 -> slack-mediated.
    The threshold at S = 0 is a foundation POSIT (named, not derived)."""
    out = {}
    for X, g in d["gate"].items():
        S = g["M"] - g["P"]
        mode = "automatic" if S <= 0 else "slack-mediated"
        note = ""
        if g["Sp"] is not None:
            if g["Sp"] <= 0 < S:
                note = "stuck-but-capable (perceived slack <= 0 < actual slack)"
            elif S <= 0 < g["Sp"]:
                note = "over-certified (perceived slack > 0 >= actual slack)"
        realized = [(a, label, m) for (XX, a, label, m) in d["act"] if XX == X]
        out[X] = {"S": S, "mode": mode, "note": note, "acts": realized}
    return out


# ---------------------------------------------------------------- driver
def read(text):
    d = parse(text)
    rho, modes = rho_readings(d)
    phi = phi_readings(d)
    kap = kappa_readings(d)
    D = D_readings(d)
    rows = []
    for x, label in d["content"].items():
        if x in d.get("hidden", set()):
            continue
        rows.append({
            "node": x, "label": label,
            "kappa": kap[x],
            "phi": phi[x]["phi"], "n": phi[x]["n"], "eps": phi[x]["eps"],
            "pending": phi[x]["pending"],
            "rho": rho[x], "D": D.get(x), "A": d["A"][x],
            "class": classify(d["A"][x], phi[x]["phi"]),
        })
    return d, rows


def fmt(v):
    return "undef" if v is None else ("%.2f" % v)


def main(path):
    text = open(path).read() if path != "-" else sys.stdin.read()
    d, rows = read(text)
    print("delta = %g   modes = %s" % (d["delta"], sorted({k for (_, _, k, _) in d['wire']})))
    hdr = "%-6s %-5s %-7s %-3s %-5s %-7s %-3s %-2s %-22s %s"
    print(hdr % ("node", "kappa", "phi", "n", "eps", "rho", "D", "A", "class", "pending q?"))
    for r in rows:
        rho_s = "/".join("%s:%.2f" % (k, v) for k, v in sorted(r["rho"].items()))
        print(hdr % (r["node"], fmt(r["kappa"]), fmt(r["phi"]),
                     "-" if r["n"] is None else r["n"], fmt(r["eps"]), rho_s,
                     "-" if r["D"] is None else r["D"], r["A"], r["class"],
                     ",".join(r["pending"])))
    gates = gate_readings(d)
    for X, g in gates.items():
        print("\nactualization vertex %s:  S = M - P = %.2f  ->  %s%s" % (
            X, g["S"], g["mode"].upper(), ("   [" + g["note"] + "]") if g["note"] else ""))
        print("  (S = 0 threshold is a foundation posit; M and P are declared inputs here)")
        for (a, label, m) in g["acts"]:
            tag = "REALIZED" if (m == "auto" and g["mode"] == "automatic") or (m == "B" and g["mode"] == "slack-mediated") else "not taken this cycle"
            print("  act %-8s mode=%-4s %-14s %s" % (a, m, tag, label))
        for (a, n, label) in d["wake"]:
            if any(a == aa for (aa, _, _) in g["acts"]):
                print("  wake %-7s -> %-10s %s" % (a, n, label))
    if d["bridge"]:
        print("\nCONJECTURED bridges (drawn, never computed):")
        for (u, v, label) in d["bridge"]:
            print("  %s --> %s   %s" % (u, v, label))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "-")
