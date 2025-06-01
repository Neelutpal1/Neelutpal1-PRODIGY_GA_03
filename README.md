# Neelutpal1-PRODIGY_GA_03
# 🧠 Markov Chain Text Generator
This project is a simple yet flexible **Markov chain-based text generator** that produces coherent and semi-random text using a source corpus. It is designed as part of a Generative AI internship to demonstrate probabilistic language modeling.
The model uses **n-gram (Markov chain)** principles to learn word transitions from a text file and generate original sentences with adjustable creativity and coherence.

# 📂 Project Structure
├── main.py # CLI interface to train and generate text
├── markov_generator.py # Core Markov chain logic
├── data/
│ └── input.txt # Training text file (you can replace this)
└── output.txt # File where generated text is saved (optional)

## 🚀 How to Run
Make sure you have Python 3 installed, then run the following in terminal:
# Basic generation
python main.py --input data/input.txt
# Custom length and diversity
python main.py --input data/input.txt --length 200 --diversity 0.9
# Avoid repeating phrases
python main.py --input data/input.txt --avoid-repeats
# Reproducible output (fixed seed)
python main.py --input data/input.txt --seed 42
You can also redirect output to a file:
python main.py --input data/input.txt > output.txt

⚙️ Arguments
Argument	Description	Default
--input / -i	Path to training text file	data/input.txt
--order / -o	Markov chain order (2–4) for coherence	3
--length / -l	Approximate number of words to generate	120
--min-sentences	Minimum number of complete sentences to include	4
--avoid-repeats	Avoid repeating exact n-gram phrases	Off
--diversity	Creativity level: 0.1 (safe) to 1.0 (wild)	0.6
--seed	Random seed for reproducibility	Random

📥 Input
Plain text file (e.g., input.txt) with full sentences.
Format: natural language, preferably with punctuation to mark sentence ends.

Example snippet of input.txt:
Dogs are loyal and intelligent animals. Foxes are cunning and agile. 
Service dogs help humans in daily life. The red fox thrives in urban areas.

📤 Output
The generated output is a coherent paragraph of text based on the training input. It respects sentence boundaries and can be adjusted for length and creativity.
Example:
Foxes may use Earth's magnetic field for precise pouncing. 
The golden retriever loves swimming in lakes. 
Dogs tilt their heads to better understand human speech. 
The red fox is the most widespread carnivore species.

🧪 Dependencies
This project uses only standard libraries plus NumPy:
Python ≥ 3.7
NumPy ≥ 1.18

📚 License
MIT License. You are free to use, modify, and share this code.

✨ Acknowledgements
Inspired by Markov chain modeling examples and generative text tools like those by Allison Parrish.

🙋‍♂️ Author
Built by Neelutpal as part of a Generative AI Internship Project.
