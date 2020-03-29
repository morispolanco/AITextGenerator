"""
Function to define special tokens (ie : CTRL code) and update the model and tokenizer
"""

def add_special_tokens(model, tokenizer):
    """
    update in place the model and tokenizer to take into account special tokens
    :param model: GPT2 model from huggingface
    :param tokenizer: GPT2 tokenizer from huggingface
    """

    tokenizer.add_special_tokens({'pad_token': '[PAD]',
                                  'eos_token': '[EOS]',
                                  'additional_special_tokens': ['[P1]',
                                                                '[P3]',
                                                                '[S]',
                                                                '[M]',
                                                                '[L]',
                                                                '[T]',
                                                                '[Sum]',
                                                                '[Ent]']})

    model.resize_token_embeddings(len(tokenizer))