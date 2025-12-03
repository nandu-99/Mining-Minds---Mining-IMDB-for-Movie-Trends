
"""
fix_notebook_widgets.py

Usage:
  python3 fix_notebook_widgets.py path/to/notebook.ipynb        # add empty "state" when missing
  python3 fix_notebook_widgets.py path/to/notebook.ipynb --remove   # remove metadata.widgets entries entirely
  python3 fix_notebook_widgets.py path/to/notebook.ipynb --add-empty # same as default
"""

import json
import sys
from pathlib import Path

def fix_notebook(fp: Path, mode: str = "add-empty"):
    nb = json.loads(fp.read_text(encoding='utf-8'))
    changed = False

    # Top-level metadata.widgets
    mw = nb.get("metadata", {}).get("widgets")
    if mw is not None:
        if mode == "remove":
            if "widgets" in nb["metadata"]:
                del nb["metadata"]["widgets"]
                changed = True
        else:
            # add missing state keys where necessary
            if isinstance(nb["metadata"]["widgets"], dict):
                if "state" not in nb["metadata"]["widgets"]:
                    nb["metadata"]["widgets"]["state"] = {}
                    changed = True

    # per-cell metadata.widgets
    for cell in nb.get("cells", []):
        cmw = cell.get("metadata", {}).get("widgets")
        if cmw is not None:
            if mode == "remove":
                if "widgets" in cell["metadata"]:
                    del cell["metadata"]["widgets"]
                    changed = True
            else:
                if isinstance(cmw, dict) and "state" not in cmw:
                    cmw["state"] = {}
                    changed = True

    if changed:
        bkp = fp.with_suffix(fp.suffix + ".bak")
        fp.replace(bkp)  # move original to .bak
        fp.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
        print(f"Fixed notebook. Original moved to {bkp}")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide notebook path. See header for usage.")
        sys.exit(1)
    p = Path(sys.argv[1])
    if not p.exists():
        print("File not found:", p)
        sys.exit(2)
    m = "add-empty"
    if len(sys.argv) > 2:
        if sys.argv[2] == "--remove":
            m = "remove"
        elif sys.argv[2] in ("--add-empty",):
            m = "add-empty"
    fix_notebook(p, mode=m)
