# Portfolio site

Files needed to host the portfolio are inside this folder. To serve locally:

```bash
# from repo root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install Flask
python -m http.server 8000 --directory portfolio
```
