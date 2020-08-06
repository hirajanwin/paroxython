"""
Read and execute a pipeline of commands and report the learning costs.

USAGE:
    ```
    paroxython recommend [options] DB_PATH
    ```

DESCRIPTION:
    ```plain
    Requires an existing database previously generated by the command:

        paroxython collect

    ... and a pipeline of commands describing which concepts (taxa) are
    already known, which ones need to be illustrated or must be avoided. It
    results in a list of recommended programs, along with their total learning
    costs and the individual learning cost of each of the concepts they feature.
    These results are presented in Markdown format.
    ```

OPTIONS:
    ```plain
    -b --base=PATH      Value accessible, with the syntax "{base}", by any shell
                        command of the pipeline. If not specified, this is the
                        parent directory of DB_PATH. [default: ]
    -c --cost=STR       Learning cost assessment strategy. [default: zeno]
                        Currently available:
                        • zeno: the i-th edge of a taxon, if not already
                                imparted, costs 2^(-i). For instance, the taxon
                                old/new/new will costs 2^-2 + 2^-3 = 0.375.
                        • linear: simply count the number of new edges.
    -o --output=PATH    The path of the resulting report. If it is omitted, and
                        DB_PATH is of the form PREFIX_db.json, a value of
                        PREFIX_recommendations.md is used. If it is STDOUT, the
                        sorted list of recommended (but not hidden) programs, is
                        printed on the standard output. [default: ]
    -p --pipe=PATH      Path of the command pipeline. If it is omitted, and
                        DB_PATH is of the form PREFIX_db.json, a value of
                        PREFIX_pipe.py is used. If the associated file is
                        missing or malformed, no filter is applied. [default: ]
    ```
"""

import json
import sys
from pathlib import Path

import regex  # type: ignore
from typed_ast.ast3 import literal_eval

from ..recommend_programs import Recommendations


def cli_wrapper(args):
    db_path = Path(args["DB_PATH"])
    parent_path = db_path.parent
    m = regex.fullmatch(r"(.+)[_-]db\.json", db_path.name)
    prefix = m[1] if m else None
    pipeline_path = Path(args["--pipe"] or parent_path / f"{prefix}_pipe.py")
    if pipeline_path.is_file():
        try:
            commands = literal_eval(pipeline_path.read_text())
        except Exception:  # Too many possible exceptions
            sys.exit(f"The pipeline '{pipeline_path}' is malformed: aborted.")
    elif args["--pipe"]:
        sys.exit(f"No pipeline at '{pipeline_path}': aborted.")
    else:
        commands = []
    stdout_backup = sys.stdout
    if args["--output"].upper() == "STDOUT":
        sys.stdout = sys.stderr
    rec = Recommendations(
        db=json.loads(db_path.read_text()),
        base_path=Path(args["--base"] or parent_path),
        assessment_strategy=args["--cost"],
    )
    rec.run_pipeline(commands)
    if args["--output"].upper() == "STDOUT":
        sys.stdout = stdout_backup
        return print("\n".join(sorted(rec.selected_programs - rec.hidden_programs)))
    output_path = Path(args["--output"] or parent_path / f"{prefix}_recommendations.md")
    output_path.write_text(rec.get_markdown())
    print(f"Dumped: {output_path.resolve()}.\n")
