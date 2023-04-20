import argparse
import re
import os
import json
from pathlib import Path

from tqdm import tqdm
import torch

from module.summarize_model import SummarizeModel

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', '--transcribe-files',
        nargs='+'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='csebuetnlp/mT5_multilingual_XLSum'
    )
    parser.add_argument(
        '--device',
        type=str,
        default='cuda'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./summarize'
    )
    
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    device = args.device
    if 'cuda' in device and torch.cuda.is_available() == False:
        device = 'cpu'

    model = SummarizeModel(model_name=args.model,
                           tokenizer_name=args.model,
                           device=device)

    Path(args.output_dir).mkdir(parents=True, exist_ok=True)

    print("Summarizing...")
    for file in tqdm(args.transcribe_files, total=len(args.transcribe_files)):
        assert os.path.exists(file)
        file_stem = Path(file).stem
        
        with open(file, 'r') as f:
            transcript = json.load(f)
        
        summary = model.get_summary(text=transcript['text'])

        with open(os.path.join(args.output_dir,(file_stem + '.txt')), 'w') as f:
            f.write(summary)
    print("Finished.")

if __name__ == "__main__":
    main()