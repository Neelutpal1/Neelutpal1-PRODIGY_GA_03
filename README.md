# Neelutpal1-PRODIGY_GA_03

# 🧠 Markov Chain Text Generator
This project is a flexible and lightweight **Markov chain-based text generator**, developed as part of a **Generative AI internship**. It analyzes a text corpus and generates new, semi-random sentences based on learned word transitions.

# 📂 Project Structure
<pre>
├── main.py # Entry point for training/generating
├── src/
│   └── markov_generator.py # Core Markov logic
├── data/
│   └── input.txt # Sample training text
├── sample_output_seeded.txt # Sample output (fixed seed)
├── sample_output_random.txt # Sample output (no seed)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore
└── LICENSE
</pre> ```

# 🚀 How to Run
Make sure Python 3.7+ is installed.
# 📦 Install Dependencies
pip install -r requirements.txt
▶️ Run Text Generation
# Basic usage
python main.py --input data/input.txt

# Custom length and diversity
python main.py --input data/input.txt --length 200 --diversity 0.9

# Avoid repeating phrases
python main.py --input data/input.txt --avoid-repeats

# Fixed output using seed
python main.py --input data/input.txt --seed 42
Redirect output to file if needed:
python main.py --input data/input.txt > output.txt

⚙️ Command-Line Arguments
Argument	Description	Default
--input / -i	           Path to training text file	data/input.txt
--order / -o	           Markov chain order (2–4)	3
--length / -l	           Number of words to generate	120
--min-sentences          Minimum number of full sentences	4
--avoid-repeats	         Prevent repeated n-gram phrases	False
--diversity	             Creativity level (0.1 to 1.0)	0.6
--seed	                 Seed for reproducible results	None

📝 Sample Output
🔁 Without Seed (Random)
Each run gives different results:
Dogs lick their noses to enhance scent detection. 
Foxes sometimes play with dog toys in the wild. 
That golden retriever really enjoys swimming in lakes. 
The swift fox remains endangered in some areas.

🎯 With Seed (--seed 42)
Using a fixed seed gives predictable output:
python main.py --input data/input.txt --length 120 --seed 42
Nocturnal. That fox is stealthily stalking an unsuspecting mouse!

📥 Input Format
Plain text file with punctuated sentences (e.g., data/input.txt)
Example:
Dogs are loyal companions. Foxes are clever and stealthy. 
The red fox adapts well to cities.

📤 Output
The model produces semi-random sentences based on the input. Output size and tone vary based on the order and diversity parameters.
🧪 Dependencies
Only one extra dependency:
numpy
Install using:
pip install -r requirements.txt
requirements.txt content:
nginx

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Developed by Neelutpal as part of a Generative AI Internship Project.
