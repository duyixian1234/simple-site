import typer

from helper.build import build_pages, clean_build, find_pages
from helper.serve import serve

app = typer.Typer()


@app.command()
def version():
    typer.echo("Version: 0.1.0")


@app.command()
def build():
    pages = find_pages()
    build_pages(pages)


@app.command()
def clean():
    clean_build()
    typer.echo("Build files have been removed")


@app.command("serve")
def _serve():
    build()
    serve()


if __name__ == "__main__":
    app()
