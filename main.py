from fastapi import FastAPI


app = FastAPI(
    title="Gaming For All API",
    description="Première version minimale de l'API Gaming For All.",
    version="0.1.0",
)


@app.get("/")
def home() -> dict[str, str]:
    """Retourne un message lorsque l'API est accessible."""
    return {"message": "Bienvenue sur Gaming For All"}


@app.get("/health")
def health() -> dict[str, str]:
    """Permet de vérifier simplement que l'API fonctionne."""
    return {"status": "ok"}
