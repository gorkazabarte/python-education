from random import shuffle


class Question:
    """ Question class representing the basic question """

    def __init__(
            self,
            question_text: str,
            choices: list[str, ...],
            correct_choice: str | list[str, ...]
    ) -> None:
        self.question_text = question_text
        self.choices = choices
        self.correct_choice = str(correct_choice)
        self.selected_answer = None

    def __str__(self) -> str:
        """ Pretty print the question """

        output: str = self.question_text + '\n\n'
        for index, choice in enumerate(shuffle(self.choices)):
            output += f'{index + 1.} {choice}\n'

        return output

    def select(self, choice: int) -> None:
        """ Select an answer from the choices """

        self.selected_answer = str(choice)

    def grade(self) -> bool:
        """ Determine if the answer is correct """

        return self.selected_answer == self.correct_choice


class TrueFalseQuestion(Question):
    """ TrueFalseQuestion representing a binary question """

    def __init__(
            self,
            question_text: str,
            correct_choice: str
    ):
        question_text = self.__prefix_if_necessary(question_text)
        super().__init__(question_text, [True, False], correct_choice)
        self.selected_answer = None

    @staticmethod
    def __prefix_if_necessary(question_text: str) -> str:
        """ Add True/False at the beginning if necessary """

        return (
            question_text
            if question_text.lower().startswith("false") or question_text.lower().startswith("true")
            else f'True/False {question_text}'
        )


class MultipleSelectQuestion(Question):

    def __init__(
            self,
            question_text: str,
            choices: list[str, ...],
            correct_choices: list[str, ...]
    ):
        question_text = self.add_suffix()
        super().__init__(question_text, choices, correct_choices)
        self.correct_choices = self.__sorted_string_list(correct_choices)
        self.selected_answer = None

    def select(self, choices) -> None:
        self.selected_answer = self.__sorted_string_list(choices)

    def add_suffix(self) -> str:
        """ Add MultipleChoice at the end of the question """

        return f'{self.question_text} (select {len(self.correct_choices)})'

    @staticmethod
    def __sorted_string_list(list_of_items: list) -> list:
        return list(sorted(map(str, list_of_items)))
