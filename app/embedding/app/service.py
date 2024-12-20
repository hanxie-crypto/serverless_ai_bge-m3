
from FlagEmbedding import BGEM3FlagModel
from config import  bge_m3_dir


M3_MODEL = 'm3_model'



class ModelManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ModelManager, cls).__new__(cls)
            cls._instance.models = {}
        return cls._instance
    
    def get_model(self, model_name, def_name, path, **kwargs):
        if model_name not in self.models:
            try:
                self.models[model_name] = def_name(path, **kwargs)
            except KeyError:
                raise EnvironmentError("A dependent environment variable might not be set.")
            except Exception as e:
                raise RuntimeError(f"Failed to initialize the model '{model_name}': {e}")
        return self.models[model_name]
    
model_manager = ModelManager()


def encode_m3(sentences: str):
    model_m3 = model_manager.get_model(M3_MODEL, BGEM3FlagModel, bge_m3_dir, use_fp16=True)
    data = model_m3.encode(sentences,
                            batch_size=12, 
                            max_length=8192, # If you don't need such a long length, you can set a smaller value to speed up the encoding process.
                            )['dense_vecs'].tolist()
    return [{"object": "embedding", "embedding": e, "index": i} for i, e in enumerate(data)]

def encode_m3_v2(sentences: str):
    model_m3 = model_manager.get_model(M3_MODEL, BGEM3FlagModel, bge_m3_dir, use_fp16=True)
    data = model_m3.encode(sentences,
                            batch_size=12, 
                            max_length=8192, # If you don't need such a long length, you can set a smaller value to speed up the encoding process.
                            )['dense_vecs'].tolist()
    return [{"object": "embedding", "embedding": data, "index": 0}]



def compare_sentences(source_sentence:str,compare_to_sentences: str | list[str]):
    source_sentence = [source_sentence]
    if isinstance(compare_to_sentences, str):
        compare_to_sentences = [compare_to_sentences]
    model_m3 = model_manager.get_model(M3_MODEL, BGEM3FlagModel, bge_m3_dir, use_fp16=True)
    embeddings_1 = model_m3.encode(source_sentence, 
                            batch_size=12, 
                            max_length=8192, # If you don't need such a long length, you can set a smaller value to speed up the encoding process.
                            )['dense_vecs']
    embeddings_2 = model_m3.encode(compare_to_sentences)['dense_vecs']
    similarity = embeddings_1 @ embeddings_2.T
    list_array = similarity.tolist()
    return list_array[0]

