"""
.. include:: ../README.md
   :start-after: ![](docs/resources/logo.png)
   :end-before: # Documentation

<br>

# Tutorial
.. include:: ../docs/md/pipeline_tutorial.md
.. include:: ../docs/md/pipeline_documentation.md
<br>

# Under the hood

## Flow
.. image:: resources/flow.png

## Pattern specifications

Browse [spec.md](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/spec.md) on GitHub.

## Default Taxonomy

Browse [taxonomy.tsv](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/taxonomy.tsv) on GitHub.

## User types

Paroxython makes heavy use of Python 3.5+ [type hints](https://docs.python.org/3/library/typing.html).
They are documented directly in the source code.
Browse [user_types.py](https://github.com/laowantong/paroxython/blob/master/paroxython/user_types.py) on GitHub.

## Glossary

- Hint:
- Label:
- Span:
- Tag:
- Taxon:
- Taxonomy:

## Default argument trick

Several functions or methods declare a compiled and bound regex pattern as an optional argument
(see `paroxython.normalize_predicate.normalize_predicate` for an example). Such arguments
are not meant to be provided by the caller. Their default value will be used systematically, with
the benefit of being evaluated only once. This is arguably better for both performance and
encapsulation. More details on [Stack Overflow](https://stackoverflow.com/a/30688691/173003).
"""


import sys

if "ipykernel" in sys.modules:
    # Declare the magic stuff paroxython iff the module is loaded as an IPython extension.

    from IPython.core.magic import Magics, line_cell_magic, magics_class  # type: ignore
    from IPython.display import Markdown, display  # type: ignore

    from .cli.cli_tag import main

    def load_ipython_extension(ipython):
        ipython.register_magics(ParoxythonMagics)

    @magics_class
    class ParoxythonMagics(Magics):
        @staticmethod
        @line_cell_magic
        def paroxython(self, line, source=None):
            """
            Tag a Python code cell and output the table of its taxa or labels.

            In cell mode:
                %%paroxython [labels] [raw]
                ... Python source code ...
            """
            if source:
                args = set(line.lower().split())
                tags = "Label" if args.intersection(["label", "labels"]) else "Taxon"
                source = f"# Compensate the offset of the magic command.\n{source}"
                result = main(source, tags=tags)
                if "raw" in args:
                    print(result)
                else:
                    display(Markdown(result))
