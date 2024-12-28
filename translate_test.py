import translators as ts
from huggingface_hub import InferenceClient
import argparse
import os
from dotenv import load_dotenv

load_dotenv()
my_key=os.getenv('hf_key')

def translate_prompt(prompt):

    res = ts.translate_text(prompt, translator='google',from_language='cnh', to_language='en')
    print(res)
    return res
def send_prompt(translate_prompt):
    client= InferenceClient(api_key=my_key)
    messages=[{"role": "user", "content": translate_prompt}]
    try:
        stream=client.chat.completions.create(model="google/gemma-2-2b-it",messages=messages,max_tokens=800,stream=False)
        output=stream.choices[0].message.content.strip()
        print(output+"\n\n-----------------------------------------------------------------------\n\n")
        res=ts.translate_text(output,'google',from_language='en',to_language='cnh')
        return res
    except:
        print( "Model is too busy")
        return "Model is too busy"

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    args = parser.parse_args()
    # print(args.echo)
    if args.prompt is not None:
        translatedPrompt=translate_prompt(args.prompt)
        print(send_prompt(translatedPrompt)) 
    else:
        print('No Prompt Entered')