##########################################
# GAEL's TEST FILE, PLEASE DO NOT MODIFY #
##########################################

from src.torch_loader import DatasetFromRepo
from src.torch_loader import VectorizeParagraph
from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer


JSON_FILE_PATH = "data/ent_sum/"

if __name__ == "__main__":
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    vectorize_paragraph = VectorizeParagraph(tokenizer, block_size=1020)

    tokenizer.add_special_tokens({'pad_token': '[PAD]',
                                  'eos_token': '[EOS]',
                                  'additional_special_tokens': ['[P1]', '[P3]', '[S]', ' [M]',
                                                                '[L]', '[T]', '[Sum]', '[Ent]']})

    novels_dataset = DatasetFromRepo(path=JSON_FILE_PATH, transform=vectorize_paragraph)

    model = GPT2LMHeadModel.from_pretrained('gpt2')
    model.resize_token_embeddings(len(vectorize_paragraph.tokenizer))

    output = model(novels_dataset[0])
    print(output[0].shape)

