import argparse
import random
from markov_generator import MarkovGenerator

def main():
    # Command-line argument parser
    parser = argparse.ArgumentParser(
        description='Enhanced Markov Text Generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--input', default='data/input.txt', 
                        help='Path to input text file for training')
    parser.add_argument('-o', '--order', type=int, default=3, 
                        choices=range(2, 5), metavar='[2-4]',
                        help='Order of the Markov chain (higher = more coherent)')
    parser.add_argument('-l', '--length', type=int, default=120,
                        help='Target word count of the generated output')
    parser.add_argument('--min-sentences', type=int, default=4,
                        help='Minimum number of complete sentences to generate')
    parser.add_argument('--avoid-repeats', action='store_true',
                        help='Avoid repeating the same phrase during generation')
    parser.add_argument('--diversity', type=float, default=0.6,
                        help='Diversity level: 0.1 (safe) to 1.0 (creative)')
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed for reproducibility')
    
    args = parser.parse_args()

    # Load and clean input text
    print(f"Loading training data from {args.input}...")
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            text = ' '.join(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        print("Error: Input file not found")
        return

    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    print(f"Training data: {word_count} words, {sentence_count} sentences")
    
    print(f"\nTraining Markov generator (order={args.order})...")

    # Set seed for reproducibility if specified
    random.seed(args.seed if args.seed is not None else random.randint(0, 1000))

    # Initialize and train the generator
    generator = MarkovGenerator(
        order=args.order,
        avoid_repeats=args.avoid_repeats,
        diversity=max(0.1, min(1.0, args.diversity))
    )
    generator.train(text)

    print(f"\nGenerating text (~{args.length} words, min {args.min_sentences} sentences)...\n")

    # Generate and display the result
    generated = generator.generate(
        target_length=args.length,
        min_sentences=args.min_sentences
    )
    print(generated + "\n")

if __name__ == "__main__":
    main()
