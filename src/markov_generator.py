import random
import numpy as np
from collections import defaultdict

class MarkovGenerator:
    def __init__(self, order=3, avoid_repeats=True, diversity=0.6):
        # Limit order to 2–4 to balance complexity and coherence
        self.order = max(2, min(4, order))
        self.avoid_repeats = avoid_repeats  # Avoid repeating the same word chains
        self.diversity = max(0.1, min(1.0, diversity))  # Diversity controls randomness
        self.model = defaultdict(dict)  # Holds the Markov chain: {state: {next_word: count}}
        self.start_states = []  # Starting word tuples (used to start sentences)

    def train(self, text):
        """Trains the Markov model on the given text."""
        words = text.split()
        for i in range(len(words) - self.order):
            state = tuple(words[i:i + self.order])  # Current word tuple (state)
            next_word = words[i + self.order]       # Next word after the state
            self.model[state][next_word] = self.model[state].get(next_word, 0) + 1

            # If the sentence ends here, consider next state a valid sentence start
            if words[i].endswith(('.', '!', '?')):
                self.start_states.append(state)

        # Fallback if no sentence-starting states found
        if not self.start_states:
            self.start_states = list(self.model.keys())

    def get_next_word(self, state):
        """Selects the next word from the given state using weighted probabilities."""
        if state not in self.model:
            return None

        words, counts = zip(*self.model[state].items())
        weights = np.array(counts, dtype=float)

        # Apply diversity to weight distribution (higher diversity = more randomness)
        weights = np.power(weights, 1.0 / (self.diversity + 0.1))
        weights /= weights.sum()

        return np.random.choice(words, p=weights)

    def generate(self, target_length=120, min_sentences=4):
        """Generates text of approximately `target_length` words and `min_sentences`."""
        generated = []
        sentences = 0
        used_phrases = set()

        # Start from a random state that likely starts a sentence
        current_state = random.choice(self.start_states)
        generated.extend(current_state)

        while len(generated) < target_length or sentences < min_sentences:
            next_word = self.get_next_word(current_state)

            if not next_word:
                current_state = random.choice(self.start_states)
                continue

            new_phrase = current_state + (next_word,)

            # Optionally skip repeated word patterns
            if self.avoid_repeats and new_phrase in used_phrases:
                continue

            generated.append(next_word)
            if self.avoid_repeats:
                used_phrases.add(new_phrase)

            # Slide the state window
            current_state = tuple(generated[-self.order:])

            # Count sentences when punctuation is found
            if next_word.endswith(('.', '!', '?')):
                sentences += 1
                if sentences >= min_sentences and len(generated) >= target_length:
                    break

        # Post-processing: ensure the text ends in a sentence
        result = ' '.join(generated)
        if not result.endswith(('.', '!', '?')):
            result += random.choice(['.', '!'])

        # Trim excess words but keep whole sentences
        words = result.split()
        if len(words) > target_length:
            last_punct = max(
                (i for i, word in enumerate(words)
                 if word.endswith(('.', '!', '?')) and i <= target_length),
                default=-1
            )
            if last_punct > 0:
                words = words[:last_punct + 1]

        return ' '.join(words)
