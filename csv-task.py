import argparse
import csv
import logging
import os


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(asctime)s  %(message)s')
logger = logging.getLogger("csv-task")

BASEDIR = os.path.abspath(os.path.dirname(__file__))
NEW_COLUMN_NAME = "price_edited"


def process_file(input_file: str, output_file: str):
    with open(input_file, "r", newline="\n", encoding="utf-8") as infile, \
            open(output_file, "w", newline="", encoding="utf-8") as outfile:
        csv_reader = csv.reader(infile, delimiter="\t")
        csv_writer = csv.writer(outfile, delimiter=",")

        header = next(csv_reader)
        header.append(NEW_COLUMN_NAME)
        csv_writer.writerow(header)

        for row in csv_reader:
            # fill the column value from the “search_price” column
            try:
                new_value = float(row[7])
            except ValueError:
                new_value = None

            row.append(new_value)
            csv_writer.writerow(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run csv-task.py")
    parser.add_argument("--infile", required=True, help="Iinput TSV file")
    parser.add_argument("--out", required=True, help="Output CSV file")

    args = parser.parse_args()
    input_file = os.path.join(BASEDIR, args.infile)
    output_file = os.path.join(BASEDIR, args.out)
    logger.info(f"Run csv-task with: {args.infile}, {args.out}")

    if os.path.exists(input_file):
        try:
            process_file(input_file, output_file)
            logger.info("Run csv-task finished successfully")
        except Exception as ex:
            logger.error(f"Failed to process file: {args.infile}", exc_info=True)
    else:
        logger.error(f"Input file not found: {args.infile}")
