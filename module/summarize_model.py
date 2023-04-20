import re
import torch
from typing import Union

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class SummarizeModel:
    def __init__(self,
                 model_name: str,
                 tokenizer_name: str,
                 device: str,
                 padding: Union[str, bool]=True,
                 truncation: bool=True,
                 max_input_length: int=768,
                 max_summarize_length: int=100,
                 no_repeat_ngram_size: int=2,
                 num_beams: int=5
                 ) -> None:
        
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        
        self.device = device

        self.padding = padding
        self.truncation = truncation
        
        self.max_input_length = max_input_length
        self.max_summarize_length = max_summarize_length

        self.no_repeat_ngram_size = no_repeat_ngram_size
        self.num_beams = num_beams


    def _encode(self, text: str) -> dict:
        return self.tokenizer(text=text,
                              padding=self.padding,
                              truncation=self.truncation,
                              max_length=self.max_input_length,
                              return_tensors='pt')
    
    def _decode(self, token_ids: torch.tensor):
        return self.tokenizer.decode(token_ids=token_ids,
                                     skip_special_tokens=True,
                                     clean_up_tokenization_spaces=False)

    def _summarize(self, input_ids: torch.tensor) -> torch.tensor:
        return self.model.generate(input_ids=input_ids,
                                   max_length=self.max_summarize_length,
                                   no_repeat_ngram_size=self.no_repeat_ngram_size,
                                   num_beams=self.num_beams)[0]

    def get_summary(self, text: str) -> str:
        input_ids = self._encode(text=text)['input_ids'].to(self.device)
        output_ids = self._summarize(input_ids=input_ids)
        summary = self._decode(token_ids=output_ids)

        return summary