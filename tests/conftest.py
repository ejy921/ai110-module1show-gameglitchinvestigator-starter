import sys
from pathlib import Path

# Add the project root to sys.path during pytest collection so tests can
# import top-level modules like `logic_utils` without depending on
# how pytest is invoked. This mirrors how the app imports modules at
# runtime and keeps test imports predictable.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
