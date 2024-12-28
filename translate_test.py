import translators as ts
from huggingface_hub import InferenceClient
import argparse
my_key='hf_**************************'


# langres= ts.get_languages('google')
# # text=json.dump(langres)
# print(langres)
# with open( 'lang.txt' ,'w') as file:

#     file.write(text)
def translate_prompt(prompt):
# prompt='What does disciplinary action mean?'
# chin_prompt='a ho te dah an black hero UG People Defence Force an si?'
    # res = ts.translate_text(prompt, translator='google', to_language='cnh')
# print(res)

# chin_text='Interest nih zeitindah rian a ttuan ti kha na chim kho lai maw?'
    res = ts.translate_text(prompt, translator='google',from_language='cnh', to_language='en')
    print(res)
    return res
def send_prompt(translate_prompt):
    client= InferenceClient(api_key=my_key)
    messages=[{"role": "user", "content": translate_prompt}]
    try:
        
        stream=client.chat.completions.create(model="google/gemma-2-2b-it",messages=messages,max_tokens=800,stream=False)

        
    # print(stream)
        output=stream.choices[0].message.content.strip()
        print(output+"\n\n-----------------------------------------------------------------------\n\n")

        res=ts.translate_text(output,'google',from_language='en',to_language='cnh')
        # print(res)
        return res
    except:
        print('Model is too busy')
# example_test="""Sushi, the beloved Japanese dish, has a rich history that spans centuries and has evolved from a preservation method into the culinary art we know today. Here's a brief story of how sushi developed:

# ### 1. **The Origins: Narezushi (Around 2nd Century BC - 8th Century AD)**
# Sushi's roots trace back to Southeast Asia, where a form of fish preservation called **narezushi** was practiced. Narezushi involved fermenting fish by packing it in rice to help preserve it. The rice was used to store the fish and naturally fermented, but it wasn't consumed. Instead, it was discarded after the fish had been cured.

# This method of preserving fish spread to Japan, where it evolved over time. The fermentation process gradually became shorter, and people started eating the rice alongside the fish, which became a precursor to the modern sushi we know.

# ### 2. **The Evolution: Edomae-zushi (19th Century)**
# By the Edo period (1603–1868), a key transformation occurred in the city of Edo (modern-day Tokyo). Here, sushi evolved into something more familiar to today's sushi lovers, particularly **Edomae-zushi** (meaning "from Edo"). The term "Edomae" refers to the fish caught in Tokyo Bay, and the sushi style began to focus on fresh, raw fish paired with vinegared rice.

# Around this time, **nigiri sushi**, which consists of a small mound of rice topped with a slice of fish, was born. The rice was seasoned with vinegar, sugar, and salt, giving it a tangy flavor. Nigiri was designed as a quick, ready-to-eat snack, convenient for the bustling, urban lifestyle of Edo. It became popular in street-side stalls and was often served as fast food in the busy city.

# ### 3. **The Influence of Modern Technology and Globalization**
# As sushi became more popular in Japan, it also began to spread internationally. The 20th century saw the rise of sushi outside Japan, particularly in the United States. The **California roll**—a maki sushi roll containing avocado and imitation crab meat—was invented in Los Angeles in the 1960s as a way to make sushi more appealing to Western tastes. This was a turning point in the history of sushi, as it began to be adapted with local ingredients and interpretations.

# In the 1980s and 1990s, sushi became a trendy food item worldwide, with sushi bars, conveyor-belt sushi restaurants, and all-you-can-eat sushi establishments popping up globally. Sushi moved from being a traditional Japanese dish to an international culinary phenomenon.

# ### 4. **Types of Sushi**
# There are many types of sushi today, and they come in various forms:

# - **Nigiri**: A small mound of vinegared rice topped with a slice of raw or cooked fish, sometimes with a dab of wasabi.
# - **Maki**: Rolled sushi, made by placing rice and fillings (such as fish, vegetables, or egg) on a sheet of nori (seaweed) and rolling it up. The roll is then sliced into pieces.
# - **Sashimi**: Thinly sliced raw fish served without rice, often served alongside soy sauce, wasabi, and pickled ginger.
# - **Temaki**: A cone-shaped hand roll made by wrapping fish, vegetables, and rice in nori.
# - **Chirashi**: A bowl of sushi rice topped with a variety of raw fish and garnishes.

# ### 5. **Sushi Today**
# Sushi is now enjoyed globally, with each region or country adding its own twist. Some countries even offer unique variations, like deep-fried sushi, sushi with cream cheese, or rolls with sweet sauces. However, traditional sushi with high-quality fish, fresh ingredients, and expert technique remains highly respected.

# In Japan, sushi remains a refined dish, often enjoyed during special occasions, at sushi restaurants, or in the form of sushi trains (conveyor belt sushi). Sushi chefs, or **itamae**, train for years to perfect the art of making sushi, emphasizing knife skills, fish selection, and rice preparation.

# ### 6. **Cultural Importance**
# Sushi plays a significant role in Japanese culture, symbolizing balance, aesthetics, and seasonality. Traditional sushi often reflects the Japanese philosophy of **wabi-sabi** (appreciation of simplicity and imperfection). Sushi also represents the country's deep connection to the sea and the importance of fresh, seasonal ingredients in Japanese cuisine.

# In recent years, sushi has been further celebrated in art, literature, and films. Its evolution from a humble preservation method to a global delicacy highlights not only the adaptability of food but also the cultural exchange that shapes global cuisine.

# ### In Summary
# Sushi's journey from a method of preserving fish in rice to becoming a worldwide culinary sensation reflects both its humble origins and its sophisticated evolution. It has transformed from a functional food to an art form, with traditional practices coexisting alongside modern interpretations. Today, sushi is a symbol of Japanese culture and a beloved food enjoyed around the globe. """

# res=ts.translate_text(example_test,'google',from_language='en',to_language='cnh')
# print(res)
# # ts.translate_text()

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