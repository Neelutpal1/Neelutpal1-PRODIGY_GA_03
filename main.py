from src.markov_generator import MarkovChain

def load_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    text = load_data("data/input.txt")
    mc = MarkovChain(order=2)
    mc.train(text)
    output = mc.generate(300)
    print("Generated Text:\n", output)

if __name__ == "__main__":
    main()
