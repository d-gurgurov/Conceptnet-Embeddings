# ConceptNet Data Extractor & Embeddings Builder

## Overview

This application focuses on extracting data from ConceptNet for a specific language, saving the data into a JSON file, building PPMI embeddings from this data, and retrofitting additional GloVe embeddings (if provided) using the ConceptNet PPMI embeddings.

## Project Structure
    ├── LICENSE

    ├── README.md

    ├── extract_data.sh

    └── modules

        ├── data_fetcher.py

        ├── embs_retrofitter.py

        ├── main.py

        └── ppmi_generator.py


## Usage

### Data Extraction

To extract data for specific language codes, you can use the provided `extract_data.sh` script:

`bash ./extract_data.sh`

The script processes multiple language codes specified in the array and runs the main.py script for each language. Make sure to update the lang_codes array in the script with the desired language codes.

### Manual input

If you prefer manual input, run the main.py script directly:

`python3 .modules/main.py`

Follow the prompts to enter the language code, output file for ConceptNet dump, path to GloVe embeddings file (type 'no' for no embeddings), whether to build PPMI embeddings, and the desired PPMI dimension.

### Project Files
- `data_fetcher.py`: Module for fetching and formatting data from ConceptNet, saving data as JSON, and extracting language distribution.

- `ppmi_generator.py`: Module for processing ConceptNet data, building PPMI embeddings, and saving them as a text file.

- `embs_retrofitter.py`: Module for retrofitting GloVe embeddings using ConceptNet PPMI embeddings, performing transformations, and saving the results.

- `main.py`: Main script for interactive input, calling data fetching, PPMI generation, and embeddings retrofitting.

### Dependencies
- Python 3.x
- Required Python packages (install using pip install -r requirements.txt)

## Acknowledgments
- [ConceptNet](https://github.com/commonsense/conceptnet5/wiki/Languages)
- [GloVe Embeddings](https://nlp.stanford.edu/projects/glove/)