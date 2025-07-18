class Question:
    """A class to represent a question with its options and answer."""

    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}, Options: {self.options}, Answer: {self.answer}"

