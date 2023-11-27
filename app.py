from flask import Flask, request, jsonify
from NLP import load_nlp_model, process_input, extract_information

app = Flask(__name__)

# Load the spaCy language model
nlp = load_nlp_model()

@app.route('/process_input', methods=['POST'])
def process_input_route():
    try:
        # Get JSON data from the request
        data = request.get_json()
        user_input = data.get('user_input')

        # Process the user input
        doc = process_input(nlp, user_input)

        # Extract information
        intent, entities, named_entities, dependencies = extract_information(doc)

        # Return the results as JSON
        result = {
            'intent': intent,
            'entities': entities,
            'named_entities': named_entities,
            'dependencies': dependencies
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
