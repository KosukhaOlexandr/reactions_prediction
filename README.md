# Reactions prediction
A project that show the process of building a model that predicts emoji reactions to the news on Telegram channels.

Project structure: 
1. Retrieving the data using Pyrogram in create_dataset.py -> 
2. Removing unnecessary columns and records in clear_dataset.py -> 
3. Conversion from .json fromat to csv dataframe, preprocessing the text and reactions in Colab notebook "Preprocessing" ->
4. Building models: notebooks "Model" and "Model without stopwords"
