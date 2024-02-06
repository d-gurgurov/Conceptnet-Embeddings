import argparse

from embs_retrofitter import EmbeddingsRetrofitter
from ppmi_generator import PPMIGenerator
from data_fetcher import DataFetcher

def get_user_input():
    get_lang_codes()

    language_code = input("Enter language code: ")
    output_dir = input("Enter output file for CN dump: ")
    glove_path = input("Enter path to GloVe embeddings file (type 'no' for no emb-s): ")
    ppmi_path = input("Build PPMI embeddings? (yes/no): ")
    ppmi_dim = int(input("Enter PPMI dimension: "))

    return language_code, output_dir, glove_path, ppmi_path, ppmi_dim

def get_lang_codes():
    response = input("Do you want to see all language codes? (yes/no): ").lower()
    if response == 'yes':
        ppmi_generator = DataFetcher(language='dummy')
        ppmi_generator.get_language_codes()

def main():
    
    parser = argparse.ArgumentParser(description='Program for aligning and retrofitting embeddings from different sources')

    parser.add_argument('--language', type=str, default='mt', help='Language code for processing embeddings')
    parser.add_argument('--output', type=str, default='mt_cn', help='Output name for conceptnet data (press enter to stay in current directory)')
    parser.add_argument('--glove', type=str, default=None, help='Path to GloVe embeddings text file (300)')
    parser.add_argument('--ppmi', type=str, default='./output', help='Path to PPMI embeddings text file')
    parser.add_argument('--ppmi_dim', type=int, default=300, help='Desired dimension for PPMI embeddings')

    args = parser.parse_args()

    if not all(vars(args).values()):
        print("Not all arguments provided, requesting input interactively:")
        language, output, glove, ppmi, ppmi_dim = get_user_input()
    else:
        language, output, glove, ppmi, ppmi_dim = args.language, args.output, args.glove, args.ppmi, args.ppmi_dim

    # fetching data from conceptnet and saving as json
    data_fetcher = DataFetcher(language=language)
    fetched_data = data_fetcher.fetch_and_format_edges()
    data_fetcher.save_edges_to_file(fetched_data, output)
    data_fetcher.extract_all_edges(fetched_data)
    print(data_fetcher.extract_language_distribution(fetched_data))

    # processing ConceptNet data, building PPMI embeddings, and saving as txt
    ppmi_generator = None
    if ppmi:
        ppmi_generator = PPMIGenerator(language=language, ppmi_dim=ppmi_dim)
        fetched_data = ppmi_generator.read_from_json(f'{output}{language}.json')
        fetched_data = ppmi_generator.process_conceptnet_data(fetched_data)
        ppmi_generator.save_to_txt(fetched_data)

    # retrofitting embeddings, performing transformations, and saving results
    embeddings_retrofitter = None
    if glove!="no" and ppmi:
        # retrofit_choice = input("Do you want to perform retrofitting of GloVe embeddings? (yes/no): ").lower()
        # if retrofit_choice == 'yes':
        embeddings_retrofitter = EmbeddingsRetrofitter(glove=glove, ppmi=ppmi, language=language)
        aligned_embeddings = embeddings_retrofitter.align_embeddings_transform_matrix()
        embeddings_retrofitter.save_to_txt(aligned_embeddings)

if __name__ == '__main__':
    main()
