import argparse
import csv
import logging
import os
import re

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(asctime)s  %(message)s')
logger = logging.getLogger("regex-task")

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def process_file(input_file: str, output_file: str):
    with open(input_file, "r", newline="\n", encoding="utf-8") as infile, \
            open(output_file, "w", newline="", encoding="utf-8") as outfile:
        csv_reader = csv.reader(infile, delimiter="\t")
        csv_writer = csv.writer(outfile, delimiter=",")
        skipped_rows = 0
        for row in csv_reader:
            line = " ".join(row)
            # try find all the knit products with jumpers
            # or any other products, otherwise skipp the product
            pattern = r"(?!.*knit(?!.*jumper))"
            if re.match(pattern, line):
                csv_writer.writerow(row)
            else:
                skipped_rows += 1

        logger.info(f"Processed the CSV file, {skipped_rows} - knit products without jumpers skipped")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run csv-task.py")
    parser.add_argument("--infile", required=True, help="Iinput TSV file")
    parser.add_argument("--out", required=True, help="Output CSV file")

    args = parser.parse_args()
    input_file = os.path.join(BASEDIR, args.infile)
    output_file = os.path.join(BASEDIR, args.out)
    logger.info(f"Run regex-task with: {args.infile}, {args.out}")

    if os.path.exists(input_file):
        try:
            process_file(input_file, output_file)
            logger.info("Run regex-task finished successfully")
        except Exception as ex:
            logger.error(f"Failed to process file: {args.infile}", exc_info=True)
    else:
        logger.error(f"Input file not found: {args.infile}")
