import click
import pandas as pd

FILE_FORMATS = ["csv", "excel", "parquet"]

READ_FUNCTION_BY_FORMAT = {
    "csv": lambda x: pd.read_csv(x),
    "parquet": lambda x: pd.read_parquet(x),
    "excel": lambda x: pd.read_excel(x),
}

WRITE_FUNCTION_BY_FORMAT = {
    "csv": lambda df, x: df.to_csv(x, index=False),
    "parquet": lambda df, x: df.to_parquet(
        x, index=False, engine="pyarrow", use_deprecated_int96_timestamps=True
    ),
    "excel": lambda df, x: df.to_excel(x, index=False),
}


@click.command()
@click.argument("inputfile", type=click.Path(exists=True))
@click.option(
    "-f",
    "--format",
    "format_",
    default=None,
    help="Format to convert the file.",
    required=True,
    type=click.Choice(FILE_FORMATS, case_sensitive=False),
)
@click.option("-o", "--output", default=None, help="Output filename.", type=str)
@click.option(
    "--force-str",
    is_flag=True,
    help="Force string type in table.",
)
def cli(inputfile, format_, output, force_str):
    if not inputfile.endswith(tuple(FILE_FORMATS)):
        raise click.ClickException(
            f"Input file format not supported, use: {FILE_FORMATS}"
        )

    input_format = inputfile.split(".")[-1]

    df = READ_FUNCTION_BY_FORMAT[input_format](inputfile)

    if force_str:
        df = df.astype(str)

    if output:
        WRITE_FUNCTION_BY_FORMAT[format_](df, output)
    else:
        output = inputfile.replace(input_format, format_)
        if format_ == "excel":
            output = output.replace(".excel", ".xlsx")
        WRITE_FUNCTION_BY_FORMAT[format_](df, output)

    click.echo(f"File saved: {output}")


if __name__ == "__main__":
    cli()
