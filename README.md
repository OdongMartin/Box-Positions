# BOX Positions — Sample Storage Utilities

Short summary
- Script  to extract box/position mappings from CSV exports of the sample storage system.


Quick usage

- Command-line (extract from a directory of CSVs and write output):
  - Example: python3 box_pos.py "Raw sputum" output.csv
  - The script header documents usage; see [box_pos.py](box_pos.py).


Notes and tips
- The script detects header rows via the header token (e.g., `UG_PID`) and uses column indices to print `PID,BOX,POSITION`.


If you want, I can:
- Add a short contribution section and examples.
- Convert the notebook logic into a reusable module or unit tests for the extraction logic.
