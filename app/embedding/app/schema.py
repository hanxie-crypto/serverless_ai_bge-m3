from typing import List, Union, Dict, Any
from pydantic import BaseModel, Field


class EmbeddingRequest(BaseModel):
    sentences: Union[str, List[str]]=Field(alias="input")


class SimilarityRequest(BaseModel):
    sentences: List[str]=Field(alias="input")


class CompareSentencesRequest(BaseModel):
    source_sentence: Union[str, List[str]]=Field(alias="source")
    compare_to_sentences: Union[List[str],str]=Field(alias="compare_to")

class CompareSentencesResponse(BaseModel):
    data: Any
    object:str

class EmbeddingResponse(BaseModel):
    data: List[Dict[str, Any]]
    object:str

class SimilarityResponse(BaseModel):
    score: List[Dict[str, Any]]

class RerankRequest(BaseModel):
    query: str=Field(alias="query")
    compare_to_sentences:  List[str]=Field(alias="compare_to")

class RerankResponse(BaseModel):
    data: Any
    object:str

