import numpy as np
from sklearn.linear_model import LinearRegression

class EmbeddingsRetrofitter:
    def __init__(self, glove, ppmi, language):
        """
        Initialize the EmbeddingsRetrofitter object with GloVe and PPMI embeddings.

        Args:
        - glove: Path to the GloVe embeddings text file.
        - ppmi: Path to the PPMI embeddings text file.
        """
        self.glove = self.read_embeddings_from_text(glove)
        self.ppmi = self.read_embeddings_from_text(ppmi)
        self.language = language

    def read_embeddings_from_text(self, file_path):
        """
        Read embeddings from a text file.

        Args:
        - file_path: Path to the text file containing embeddings.

        Returns:
        A dictionary of word embeddings.
        """
        embeddings = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(' ')
                if len(parts) > 301:
                    phrase = ' '.join(parts[:-300])
                    embedding = np.array([float(val) for val in parts[-300:]])
                    embeddings[phrase] = embedding
                else:
                    word = parts[0]
                    embedding = np.array([float(val) for val in parts[1:]])
                    embeddings[word] = embedding
        return embeddings


    def align_embeddings_transform_matrix(self):
        """
        Align and retrofit embeddings from different sources by finding a transformation matrix.

        Returns:
        Transformed embeddings using the alignment matrix.
        """
        common_words = [word for word in self.glove if word in self.ppmi and len(self.glove[word]) == 300]

        print(f'{len(common_words)} common words found between the embedding spaces.')

        model_1 = np.array([self.glove[word] for word in common_words])
        model_2 = np.array([self.ppmi[word] for word in common_words])

        model = LinearRegression()  
        model.fit(model_1, model_2)
        transformation_matrix = model.coef_.T

        transformed_embeddings = {word: np.dot(self.glove[word], transformation_matrix) for word in self.glove}

        return transformed_embeddings
    
    def save_to_txt(self, embeddings):
        """
        Save embeddings to a text file.

        Args:
        - embeddings: Embeddings to be saved.
        - output_dir: Path to the output directory.
        """
        with open(f'/retrofitted_embeddings_{self.language}.txt', 'w', encoding='utf-8') as file:
            for word, embedding in embeddings.items():
                file.write(word + ' ' + ' '.join([str(val) for val in embedding]) + '\n')
        print(f'Retrofitted embeddings saved!')