import time
from pathlib import Path

from label_generators import generate_labeled_sources

# fmt: off
DIRECTORIES = [
    "../Python/project_euler",
    "../Python/maths",
    "../Algo/programs",
]
# fmt: on

total_elapsed_time: float = 0
for directory in DIRECTORIES:
    path = Path(directory)
    if (path / "__is_private_directory").exists():
        output_path = Path(path.parent, "snapshot_" + path.parts[-1] + ".py")
    else:
        output_path = Path("snapshots", "-".join(path.parts[-2:]) + ".py")
    start = time.perf_counter()
    acc = [result for result in generate_labeled_sources(directory)]
    total_elapsed_time += time.perf_counter() - start
    output_path.write_text("\n".join(acc))
print(f"Total elapsed time: {total_elapsed_time:.2f} s.")