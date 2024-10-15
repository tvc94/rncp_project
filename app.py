from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load your data from the CSV file
file_path = '/Users/tovancao/Ironhack/rncp_project/API/watches_website_api.csv'

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    df = pd.DataFrame()  # Return an empty DataFrame if the file is not found
    print("CSV file not found!")

# Clean up Price: Remove currency symbols/commas, convert to float, handle NaNs
def clean_price(price):
    try:
        return float(price.replace('€', '').replace(',', '').strip())
    except (ValueError, AttributeError):
        return 0.0  # Default to 0.0 if conversion fails

df['Price'] = df['Price'].fillna('0').astype(str).apply(clean_price)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #1c1c1c;  /* Dark grey background */
                color: #f4f4f4;  /* Light grey text */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                text-align: center;
                padding: 20px;
                background-color: #2c2c2c;  /* Darker grey for container */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);  /* Slight shadow */
                border-radius: 8px;
                max-width: 600px;
                width: 100%%;
            }
            h1 {
                color: #ffffff;  /* White heading */
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            h2 {
                color: #cccccc;  /* Lighter grey for subheading */
                font-size: 1.5em;
                margin-bottom: 20px;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            ul li {
                margin: 15px 0;
            }
            a {
                text-decoration: none;
                color: #3498db;  /* Blue links for contrast */
                font-size: 1.2em;
            }
            a:hover {
                color: #2980b9;  /* Darker blue on hover */
            }
            .endpoint-description {
                color: #bbbbbb;  /* Light grey for endpoint description */
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Watch API Home Page!</h1>
            <h2>Available Endpoints:</h2>
            <ul>
                <li><a href="/api/watches">Get all watches</a></li>
                <li>
                    <a href="/api/watches/&lt;brand&gt;">Get watches by brand</a>
                    <div class="endpoint-description">(replace <code>&lt;brand&gt;</code> with the actual brand name)</div>
                </li>
                <li>
                    <a href="/api/watches/price?min=&lt;min_price&gt;&amp;max=&lt;max_price&gt;">Get watches by price range</a>
                    <div class="endpoint-description">(replace <code>&lt;min_price&gt;</code> and <code>&lt;max_price&gt;</code> with your values)</div>
                </li>
                <li>
                    <a href="/api/watches/special-edition">Get special edition watches</a>
                    <div class="endpoint-description">See all watches marked as special edition</div>
                </li>
            </ul>
        </div>
    </body>
    </html>
    """


@app.route('/api/watches', methods=['GET'])
def get_watches():
    """Get a list of all watches."""
    data = df.to_dict(orient='records')
    return jsonify(data)

@app.route('/api/watches/<brand>', methods=['GET'])
def get_watches_by_brand(brand):
    """Get watches filtered by brand name."""
    filtered_data = df[df['Brand'].str.contains(brand, case=False, na=False)]
    if filtered_data.empty:
        return jsonify({"error": "Brand not found"}), 404
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/api/watches/price', methods=['GET'])
def get_watches_by_price_range():
    """Get watches within a specified price range."""
    min_price = request.args.get('min', default=0, type=float)
    max_price = request.args.get('max', default=99999, type=float)
    filtered_data = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/api/watches/special-edition', methods=['GET'])
def get_special_edition_watches():
    """Get all special edition watches."""
    # Filter for rows where 'SpecialEdition' is exactly 'Special Edition'
    special_edition_data = df[df['Special Edition'] == 'Special Edition']
    
    if special_edition_data.empty:
        return jsonify({"error": "No special edition watches found"}), 404
    
    return jsonify(special_edition_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
