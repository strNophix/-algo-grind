import click
import jinja2
from os import path


class LeetCode:
    @staticmethod
    def filename_from_url(url: str) -> str:
        num = input("Number: ")
        name = url.split("/")[4].replace("-", "_")
        return f"{num}_{name}.py"


@click.group()
@click.option("--template-dir", default="./templates")
@click.pass_context
def cli(ctx: click.Context, template_dir: str):
    ctx.obj["template"] = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir)
    )


@cli.command()
@click.pass_context
@click.argument("url")
def leetcode(ctx: click.Context, url: str):
    file_path = path.join("leetcode", LeetCode.filename_from_url(url))
    if path.exists(file_path):
        print("File already exists")
        return 1

    templates: jinja2.Environment = ctx.obj["template"]
    templ = templates.get_template("leetcode.j2")
    result = templ.render()

    with open(file_path, mode="w", encoding="utf8") as f:
        f.write(result)


if __name__ == "__main__":
    cli(obj={})
