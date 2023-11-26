import spacy #type:ignore

def load_nlp_model(language="en_core_web_sm"):
    """
    Load the spaCy language model.

    Parameters:
    - language (str): Language code (default is English).

    Returns:
    - spacy.Language: Loaded spaCy language model.
    """
    return spacy.load(language)

def process_input(nlp, user_input):
    """
    Process user input using the spaCy language model.

    Parameters:
    - nlp (spacy.Language): Loaded spaCy language model.
    - user_input (str): User input text.

    Returns:
    - spacy.Doc: Processed spaCy Doc object.
    """
    return nlp(user_input)

def extract_information(doc):
    """
    Extract intent, entities, named entities, and dependencies from a spaCy Doc.

    Parameters:
    - doc (spacy.Doc): Processed spaCy Doc object.

    Returns:
    - tuple: Tuple containing intent, entities, named entities, and dependencies.
    """
    intent = None
    entities = []
    named_entities = []
    dependencies = []

    for token in doc:
        if token.pos_ == "VERB":
            intent = token.lemma_

        if token.ent_type_:
            entities.append((token.text, token.ent_type_))

        if token.ent_iob_ == "B":
            named_entities.append((token.text, token.ent_type_))

        # Dependency parsing information
        dependencies.append((token.text, token.dep_, token.head.text))

    return intent, entities, named_entities, dependencies

def main(language):
    

    # Load the spaCy language model
    nlp = load_nlp_model(language.strip().lower())

    # Example usage
    user_input = input("Enter user input: ")
    
    # Process the user input
    doc = process_input(nlp, user_input)

    # Extract information
    intent, entities, named_entities, dependencies = extract_information(doc)

    # Print the results
    print("Intent:", intent)
    print("Entities:", entities)
    print("Named Entities:", named_entities)
    print("Dependencies:", dependencies)

if __name__ == "__main__":
    main(language = input("Enter the language code (e.g., en, es, fr): "))