import requests
import json

class DataFetcher:
    def __init__(self, language):
        """
        Initialize the DataFetcher object with a specified language.

        Args:
        - language: A string representing the language code.
        """
        self.language = str(language)

    def get_language_codes(self):
        """
        Retrieve all language codes from ConceptNet.

        Returns:
        A dictionary containing language code to language name pairs.
        """
        language_codes = {'aa': 'Afar', 'ab': 'Abkhazian', 'abe': 'Western Abenaki', 'adx': 'Amdo Tibetan', 'ady': 'Adyghe', 'ae': 'Avestan', 'af': 'Afrikaans', 'aii': 'Assyrian Neo-Aramaic', 'ain': 'Ainu', 'akk': 'Akkadian', 'akz': 'Alabama', 'alt': 'Southern Altai', 'am': 'Amharic', 'an': 'Aragonese', 'ang': 'Old English', 'ar': 'Arabic', 'arc': 'Aramaic', 'arn': 'Mapuche', 'ast': 'Asturian', 'av': 'Avar', 'axm': 'Middle Armenian', 'az': 'Azerbaijani', 'ba': 'Bashkir', 'bal': 'Baluchi', 'be': 'Belarusian', 'bg': 'Bulgarian', 'bi': 'Bislama', 'bm': 'Bambara', 'bn': 'Bengali', 'bo': 'Tibetan', 'br': 'Breton', 'ca': 'Catalan', 'ccc': 'Chamicuro', 'ce': 'Chechen', 'ceb': 'Cebuano', 'ch': 'Chamorro', 'chk': 'Chuukese', 'chl': 'Cahuilla', 'cho': 'Choctaw', 'chr': 'Cherokee', 'cic': 'Chickasaw', 'cim': 'Cimbrian', 'cjs': 'Shor', 'co': 'Corsican', 'cop': 'Coptic', 'crh': 'Crimean Turkish', 'cs': 'Czech', 'csb': 'Kashubian', 'cu': 'Church Slavic', 'cv': 'Chuvash', 'cy': 'Welsh', 'da': 'Danish', 'dak': 'Dakota', 'de': 'German', 'dje': 'Zarma', 'dlm': 'Dalmatian', 'dsb': 'Lower Sorbian', 'dua': 'Duala', 'dum': 'Middle Dutch', 'dv': 'Divehi', 'ee': 'Ewe', 'egl': 'Emilian', 'egx': 'Egyptian languages', 'egy': 'Ancient Egyptian', 'el': 'Greek', 'en': 'English', 'enm': 'Middle English', 'eo': 'Esperanto', 'es': 'Spanish', 'esu': 'Central Yupik', 'et': 'Estonian', 'eu': 'Basque', 'fa': 'Persian', 'ff': 'Fula', 'fi': 'Finnish', 'fil': 'Filipino', 'fj': 'Fijian', 'fo': 'Faroese', 'fon': 'Fon', 'fr': 'French', 'frk': 'Frankish', 'frm': 'Middle French', 'fro': 'Old French', 'frp': 'Franco-Provençal', 'frr': 'Northern Frisian', 'fur': 'Friulian', 'fy': 'Western Frisian', 'ga': 'Irish', 'gag': 'Gagauz', 'gd': 'Scottish Gaelic', 'gl': 'Galician', 'gmh': 'Middle High German', 'gml': 'Middle Low German', 'gn': 'Guarani', 'goh': 'Old High German', 'got': 'Gothic', 'grc': 'Ancient Greek', 'gsw': 'Swiss German', 'gu': 'Gujarati', 'gv': 'Manx', 'ha': 'Hausa', 'hak': 'Hakka', 'haw': 'Hawaiian', 'hbo': 'Ancient Hebrew', 'he': 'Hebrew', 'hi': 'Hindi', 'hil': 'Hiligaynon', 'hit': 'Hittite', 'hke': 'Hunde', 'hsb': 'Upper Sorbian', 'ht': 'Haitian Creole', 'hu': 'Hungarian', 'hy': 'Armenian', 'ia': 'Interlingua', 'ie': 'Interlingue', 'ii': 'Yi', 'ilo': 'Ilocano', 'io': 'Ido', 'is': 'Icelandic', 'ist': 'Istriot', 'it': 'Italian', 'iu': 'Inuktitut', 'ja': 'Japanese', 'jbo': 'Lojban', 'jv': 'Javanese', 'ka': 'Georgian', 'kbd': 'Kabardian', 'khb': 'Tai Lü', 'ki': 'Kikuyu', 'kim': 'Tofa', 'kjh': 'Khakas', 'kk': 'Kazakh', 'kl': 'Kalaallisut', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'koy': 'Koyukon', 'krc': 'Karachay-Balkar', 'krl': 'Karelian', 'ku': 'Kurdish', 'kum': 'Kumyk', 'kw': 'Cornish', 'ky': 'Kyrgyz', 'la': 'Latin', 'lad': 'Ladino', 'lb': 'Luxembourgish', 'li': 'Limburgish', 'lij': 'Ligurian', 'liv': 'Livonian', 'lkt': 'Lakota', 'lld': 'Ladin', 'lmo': 'Lombard', 'ln': 'Lingala', 'lo': 'Lao', 'lt': 'Lithuanian', 'ltg': 'Latgalian', 'lv': 'Latvian', 'lzz': 'Laz', 'mch': 'Maquiritari', 'mdf': 'Moksha', 'mg': 'Malagasy', 'mga': 'Middle Irish', 'mh': 'Marshallese', 'mi': 'Maori', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mn': 'Mongolian', 'mr': 'Marathi', 'ms': 'Malay', 'mt': 'Maltese', 'mul': 'Multilingual', 'mwl': 'Mirandese', 'my': 'Burmese', 'myv': 'Erzya', 'na': 'Nauru', 'nah': 'Nahuatl languages', 'nan': 'Min Nan Chinese', 'nap': 'Neapolitan', 'nci': 'Classical Nahuatl', 'nds': 'Low German', 'ne': 'Nepali', 'nhn': 'Central Nahuatl', 'nl': 'Dutch', 'nmn': '!Xóõ', 'no': 'Norwegian', 'nog': 'Nogai', 'non': 'Old Norse', 'nov': 'Novial', 'nrf': 'Jèrriais', 'nv': 'Navajo', 'oc': 'Occitan', 'odt': 'Old Dutch', 'ofs': 'Old Frisian', 'oge': 'Old Georgian', 'oj': 'Ojibwa', 'oma': 'Omaha-Ponca', 'or': 'Oriya', 'orv': 'Old Russian', 'os': 'Ossetic', 'osp': 'Old Spanish', 'osx': 'Old Saxon', 'ota': 'Ottoman Turkish', 'pa': 'Punjabi', 'pal': 'Pahlavi', 'pap': 'Papiamento', 'pcd': 'Picard', 'peo': 'Old Persian', 'pi': 'Pali', 'pjt': 'Pitjantjatjara', 'pl': 'Polish', 'pms': 'Piedmontese', 'ppl': 'Pipil', 'prg': 'Prussian', 'pro': 'Old Provençal', 'ps': 'Pashto', 'pt': 'Portuguese', 'qu': 'Quechua', 'qya': 'Quenya', 'raj': 'Rajasthani', 'rap': 'Rapa Nui', 'rm': 'Romansh', 'ro': 'Romanian', 'roa-opt': 'Old Portuguese', 'rom': 'Romany', 'ru': 'Russian', 'rue': 'Rusyn', 'rup': 'Aromanian', 'rw': 'Kinyarwanda', 'sa': 'Sanskrit', 'sah': 'Sakha', 'sc': 'Sardinian', 'scn': 'Sicilian', 'sco': 'Scots', 'sd': 'Sindhi', 'se': 'Northern Sami', 'ses': 'Koyraboro Senni', 'sga': 'Old Irish', 'sh': 'Serbo-Croatian', 'shh': 'Shoshoni', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'sm': 'Samoan', 'smn': 'Inari Sami', 'sms': 'Skolt Sami', 'so': 'Somali', 'sq': 'Albanian', 'srn': 'Sranan Tongo', 'st': 'Sotho', 'stq': 'Saterland Frisian', 'su': 'Sundanese', 'sux': 'Sumerian', 'sv': 'Swedish', 'sw': 'Swahili', 'swb': 'Comorian', 'syc': 'Classical Syriac', 'szl': 'Silesian', 'ta': 'Tamil', 'te': 'Telugu', 'tet': 'Tetum', 'tg': 'Tajik', 'th': 'Thai', 'ti': 'Tigrinya', 'tk': 'Turkmen', 'tpi': 'Tok Pisin', 'tpw': 'Tupi', 'tr': 'Turkish', 'tt': 'Tatar', 'twf': 'Northern Tiwa', 'txb': 'Tokharian B', 'ty': 'Tahitian', 'tyv': 'Tuvinian', 'udm': 'Udmurt', 'ug': 'Uyghur', 'uga': 'Ugaritic', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 'vec': 'Venetian', 'vep': 'Veps', 'vi': 'Vietnamese', 'vo': 'Volapük', 'vot': 'Votic', 'wa': 'Walloon', 'wae': 'Walser', 'war': 'Waray', 'wau': 'Waurá', 'wo': 'Wolof', 'wym': 'Wymysorys', 'xcl': 'Classical Armenian', 'xh': 'Xhosa', 'xmf': 'Mingrelian', 'xno': 'Anglo-Norman', 'xpr': 'Parthian', 'xto': 'Tokharian A', 'xwo': 'Oirat', 'yi': 'Yiddish', 'yo': 'Yoruba', 'yua': 'Yucateco', 'za': 'Zhuang', 'zdj': 'Ngazidja Comorian', 'zh': 'Chinese', 'zu': 'Zulu', 'zza': 'Zaza'}
        for code, lang in language_codes.items():
                    print(code + ":", lang)

    def extract_words(self):
        """
        Extract words related to the specified language from ConceptNet.

        Returns:
        A list of words extracted from ConceptNet.
        """
        limit = 1000
        extracted_words = []

        for iteration in range(100):
            offset = iteration * limit
            start_url = f"https://api.conceptnet.io/query?start=/c/{self.language}&offset={offset}&limit={limit}"
            response = requests.get(start_url)

            if response.status_code == 200:
                try:
                    data = response.json()

                    for edge in data['edges']:
                        start_node = edge['start']
                        end_node = edge['end']

                        if 'language' in start_node and start_node['language'] == self.language:
                            extracted_words.append(start_node['term'])

                        if 'language' in end_node and end_node['language'] == self.language:
                            extracted_words.append(end_node['term'])

                    if 'view' in data and 'nextPage' not in data['view']:
                        break
                except requests.exceptions.JSONDecodeError as e:
                    print(f"Error decoding JSON in iteration {iteration}: {e}")
                    continue  # Skip to the next iteration
            else:
                print(f"Error in iteration {iteration}: {response.status_code}")

        extracted_words = set(extracted_words)
        extracted_words = list(extracted_words)
        
        print(f"{len(extracted_words)} unique words extracted in the {self.language} language!")

        return extracted_words


    def fetch_and_format_edges(self):
        """
        Retrieve edges related to a specific word from ConceptNet.

        Args:
        - word: A string representing the word to fetch edges for.

        Returns:
        A dictionary containing edges related to the specified word.
        """
        words = self.extract_words()
        print("Starting to fetch edges... (may take a while)")
        words_edges = {}

        for word in words:
            word_url = f"https://api.conceptnet.io{word}"
            response = requests.get(word_url)
            data = response.json()

            extracted_data = {}

            if 'edges' in data:
                for edge in data['edges']:
                    start_node = edge['start']
                    info = {
                        'uri': edge['@id'],
                        'rel': edge['rel']['label'],
                        'start': start_node['term'],
                        'end': edge['end']['term'],
                        'dataset': edge['dataset'],
                        'sources': [source['contributor'] for source in edge['sources']],
                        'license': edge['license'],
                        'weight': edge['weight'],
                        'surfaceText': edge.get('surfaceText', None),
                        'surfaceStart': start_node.get('label', None),
                        'surfaceEnd': edge['end'].get('label', None)
                    }
                    edges = extracted_data.get(word, [])
                    edges.append(info)
                    extracted_data[word] = edges
            words_edges.update(extracted_data)

        words_edges = self.clean_word_keys(words_edges)
        print("Fetching done!")

        return words_edges


    def _clean_key(self, key_word):
        """
        Helper function to clean keys from prefixes.

        Args:
        - key_word: A string representing the key word to clean.

        Returns:
        The cleaned key word.
        """
        key_word = key_word.replace(f'/c/{self.language}/', '')
        key_word = key_word.replace('_', ' ')
        return key_word


    def clean_word_keys(self, maltese_edges_dict):
        """
        Clean the keys of the edges dictionary.

        Args:
        - edges_dict: A dictionary containing word keys and their edges.

        Returns:
        A cleaned dictionary with updated word keys.
        """
        cleaned_dict = {}
        for word, edges in maltese_edges_dict.items():
            # splitting the word using slashes and take the last part
            cleaned_word = word.split('/')[-1]
            cleaned_word = self._clean_key(cleaned_word)
            cleaned_dict[cleaned_word] = edges
        return cleaned_dict
    

    def save_edges_to_file(self, edges, filename):
        """
        Save the edges to a JSON file.

        Args:
        - edges: A dictionary containing edges to be saved.
        - filename: A string representing the filename to save the edges.
        """
        with open(f'{filename}{self.language}.json', 'w', encoding='utf-8') as json_file:
            json.dump(edges, json_file, ensure_ascii=False, indent=4)
            print("Edges saved to file!")


    def extract_all_edges(self, extracted_words_and_edges):
        """
        Extract all possible edges from the provided words and edges.

        Args:
        - extracted_words_and_edges: A dictionary containing words and their edges.

        Returns:
        A set of all possible edges extracted.
        """
        all_edges = set()

        for word, edges in extracted_words_and_edges.items():
            for edge in edges:
                rel = edge['rel']
                all_edges.add(rel)

        print("Printing all existing edges for the current language:")
        return all_edges
    

    def extract_language_distribution(self, extracted_words_and_edges):
        """
        Extract language distribution for edges for a specific language in ConceptNet.

        Args:
        - extracted_words_and_edges: A dictionary containing words and their edges.

        Returns:
        A dictionary with language distribution for the provided words.
        """
        language_distribution = {}

        for word, edges in extracted_words_and_edges.items():
            languages = set()

            for edge in edges:
                rel = edge['rel'].split('/')[-1]
                end_language = edge['end'].split('/')[-2]

                if end_language != self.language:
                    languages.add(end_language)

            for lang in languages:
                language_distribution[lang] = language_distribution.get(lang, 0) + 1

        print("Printing language distribution of the edges for the current language:")
        return language_distribution
