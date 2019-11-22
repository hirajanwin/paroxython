import ast
from collections import defaultdict
from pathlib import Path
import regex
import sys

sys.path[0:0] = [str(Path(__file__).parent)]

from flatten import flatten


def simplify_negative_litterals():
    sub = regex.compile(
        r"""(?mx)
                    ^(.*?)/_type='UnaryOp'
            (\n(?:.+\n)*?)\1/op/_type='USub'
             \n(?:.+\n)*? \1/operand/n=(.+)
        """
    ).sub
    return lambda flat_ast: sub(r"\1/_type='Num'\2\1/n=-\3", flat_ast)


simplify_negative_litterals = simplify_negative_litterals()


find_all_constructs = regex.compile(
    r"""(?msx)
            ^\#{4}\s+Construct\s+`(.+?)` # capture the label
            .+?\#{5}\s+Regex # ensure the next pattern is in the Regex section
            .+?```re\n+(.+?)\n``` # capture this pattern
        """
).findall


class Parser:
    def __init__(self, ref_path="paroxython/ref.md"):
        self.ref_path = Path(ref_path)
        text = self.ref_path.read_text()
        self.constructs = {}
        for (label, pattern) in find_all_constructs(text):
            if label in self.constructs:
                raise ValueError(f"Duplicated label '{label}'!")
            self.constructs[label] = regex.compile(f"(?mx){pattern}")

    def __call__(self, source, yield_failed_matches=False):
        try:
            tree = ast.parse(source)
        except:
            return print("Warning: unable to construct the AST")
        self.flat_ast = simplify_negative_litterals(flatten(tree))
        for (label, rex) in self.constructs.items():
            result = defaultdict(list)
            d = None
            for match in rex.finditer(self.flat_ast, overlapped=True):
                d = match.capturesdict()
                if d.get("SUFFIX"):  # there is a "SUFFIX" key and its value is not []
                    for suffix in d["SUFFIX"]:
                        lines = "-".join(map(str, sorted(map(int, d["LINE"]))))
                        result[f"{label}:{suffix}"].append(lines)
                else:
                    lines = "-".join(map(str, sorted(map(int, d["LINE"]))))
                    result[label].append(lines)
            if yield_failed_matches and not d:
                yield (label, [])
            else:
                yield from result.items()


if __name__ == "__main__":
    time = __import__("time")
    source = Path("sandbox/source.py").read_text()
    for (i, line) in enumerate(source.splitlines(), 1):
        print(f"{i: 3} {line}")
    print()
    parse = Parser()
    start = time.perf_counter()
    acc = []
    for (label, lines) in parse(source, yield_failed_matches=False):
        stop = time.perf_counter()
        lines = ', '.join(lines)
        acc.append(f"{stop - start:7.4f} s.: | `{label}` | {lines} |")
        start = stop
    print("\n".join(sorted(acc, reverse=True)))
    Path("sandbox/flat_ast.txt").write_text(parse.flat_ast)
