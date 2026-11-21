# DevOps lab 09

Isolated educational repository: MkDocs, Pylint, pull-request quality gates and GitHub Pages.

```sh
python -m pip install -r requirements-dev.txt
python -m pylint src --score=no
mkdocs build --strict
```

Intentionally failing commits in PR history demonstrate diagnostics and recovery. No production configuration or credentials are used.
