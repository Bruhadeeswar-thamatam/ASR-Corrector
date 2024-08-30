class Agent(object):
    def __init__(self, phoneme_table, vocabulary) -> None:
        """
        Your agent initialization goes here. You can also add code but don't remove the existing code.
        """
        self.phoneme_table = phoneme_table
        self.vocabulary = vocabulary
        self.best_state = None
    def make_list(self):
        words_list=self.best_state.split()
        return words_list
    def make_phonetic_correction(self):
        phoneme_table=self.phoneme_table
        reversed_phoneme_table={}
        for key in phoneme_table:
            for value in phoneme_table[key]:
                if value in reversed_phoneme_table:
                    reversed_phoneme_table[value]=[key]
                else:
                    reversed_phoneme_table[value].append(key)
        return reversed_phoneme_table

    def asr_corrector(self, environment):
        """
        Your ASR corrector agent goes here. Environment object has following important members.
        - environment.init_state: Initial state of the environment. This is the text that needs to be corrected.
        - environment.compute_cost: A cost function that takes a text and returns a cost. E.g., environment.compute_cost("hello") -> 0.5

        Your agent must update environment.best_state with the corrected text discovered so far.
        """
        self.best_state = environment.init_state
        cost = environment.compute_cost(environment.init_state)
        words_list=self.make_list(self.best_state)
        phonetic_corrections=self.make_phonetic_correction()
        n=len(words_list)
        for i in range(n):
            present_word=words_list[i]
            corrected_word=""
            present_wordlength=len(present_word)
            index=0
            while(index<present_wordlength):
                local_cost=environment.compute_cost(self.best_state)
                for key in phonetic_corrections:
                    prefix_length=min(len(key),present_wordlength-index)
                    prefix_word=present_word[index:prefix_length]
                    if prefix_word==key:


            



