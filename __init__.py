"""
ComfyUI Workflow Models Downloader (promoteAI fork)
Scans the active workflow for missing models and provides a UI to download them from HuggingFace (with optional mirror), CivitAI, and other sources.

Features:
- Scans active workflow JSON for model references
- Identifies missing models and their target directories
- Supports configurable HuggingFace mirror base URL for downloads
- Downloads missing models with progress tracking
"""

import os
import sys
import importlib.util

# Dependencies are declared in pyproject.toml and installed by ComfyUI Manager
# or Comfy CLI. We only verify they are importable here and warn if missing.
def verify_dependencies():
    """Check that optional runtime dependencies are importable, warn if missing."""
    for import_name, pip_name in (("requests", "requests"), ("aiohttp", "aiohttp")):
        if importlib.util.find_spec(import_name) is None:
            print(f"[Workflow-Models-Downloader] {pip_name} is not installed. "
                  f"Install dependencies with 'comfy node install' or ComfyUI Manager.")
    return True


# Run verification before any other imports
verify_dependencies()

# Add the extension directory to path for imports
extension_path = os.path.dirname(__file__)
if extension_path not in sys.path:
    sys.path.insert(0, extension_path)

# Import and register the server routes
from . import server

WEB_DIRECTORY = "js"
NODE_CLASS_MAPPINGS = {}
__all__ = ['NODE_CLASS_MAPPINGS', 'WEB_DIRECTORY']
