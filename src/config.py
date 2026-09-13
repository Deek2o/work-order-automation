from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class PipelineConfig:
    input_file: Path
    output_dir: Path

    @classmethod
    def from_values(cls, input_file: str, output_dir: str) -> "PipelineConfig":
        return cls(Path(input_file), Path(output_dir))
