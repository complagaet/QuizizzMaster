let questions = document.querySelectorAll('div[id^="question-"]');

let quizData = [];

questions.forEach(question => {
    let questionTextElement = question.querySelector('.qtext');
    let questionText = questionTextElement ? questionTextElement.innerText.trim() : "Question text not found";

    let answerElements = question.querySelectorAll('.answer > div');
    let answers = [];

    answerElements.forEach(answerElement => {
        let answerTextElement = answerElement.querySelector('div[data-region="answer-label"] p') || answerElement.querySelector('div[data-region="answer-label"] div');
        let answerText = answerTextElement ? answerTextElement.innerText.trim() : "Answer text not found";

        let radioButton = answerElement.querySelector('input[type="radio"]');

        answers.push(answerText);
    });

    quizData.push({
        question: questionText,
        answers: answers
    });
});

for (let i = 0; i < quizData.length; i++) {
    quizData[i].correctAnswer = []
    let rawCorrectAnswer = document.getElementsByClassName("feedback")[i].children[0].innerText.replace("The correct answer is: ", "");
    quizData[i].correctAnswer.push(rawCorrectAnswer)
}

console.log(JSON.stringify(quizData))
copy(JSON.stringify(quizData))