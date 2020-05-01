"""
USAGE:
    paroxython tag [options] FILENAME

OPTIONS:
    -l --labels         Output the labels instead of the taxons.
    -f --output_format=FORMAT  Format of the output, either "md" (Markdown) or "tsv" (Tab Separated
                        Values). [default: md]

DESCRIPTION:
    Tag one Python file and output the table of its taxons or labels.
"""

from pathlib import Path

import context

from label_programs import ProgramLabeller
from map_taxonomy import Taxonomy
from list_programs import get_program
from typing import List, Tuple
from typing_extensions import Literal

from goodies import couple_to_string
from user_types import Source


def main(
    source: Source,
    tags: Literal["Taxon", "Label"] = "Taxon",
    relative_path: Path = Path("."),
    output_format: Literal["md", "tsv"] = "md",
) -> str:
    program = get_program(source, relative_path)
    labeller = ProgramLabeller()
    labeller.label_program(program)
    couples: List[Tuple[str, str]] = [(tags, "Lines")]
    if tags == "Label":
        for (label_name, label_spans) in sorted(program.labels):
            s = ", ".join(map(couple_to_string, sorted(label_spans)))
            couples.append((label_name, s))
    else:
        taxonomy = Taxonomy()
        taxons = taxonomy.to_taxons(program.labels)
        for (taxon_name, taxon_spans) in sorted(taxons):
            s = ", ".join(map(couple_to_string, sorted(taxon_spans.elements())))
            couples.append((taxon_name, s))
    if output_format == "md":
        result = [f"| {tag} | {lines} |" for (tag, lines) in couples]
        result[1:1] = ["|:--|:--|"]
    else:
        result = [f"{tag}\t{lines}" for (tag, lines) in couples]
    return "\n".join(result)


def cli_wrapper(args):
    path = Path(args["FILENAME"])
    result = main(
        source=Source(path.read_text()),
        tags="Label" if args["--labels"] else "Taxon",
        relative_path=path.parent,
        output_format=args["--output_format"],
    )
    print(result)