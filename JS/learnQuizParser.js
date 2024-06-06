let quizData = []

for (let q of document.getElementsByClassName("problem")) {
  let questionElement = q.children[0].children[0].children

  let question = {
    question: "",
      answers: [],
      correctAnswer: []
  }

  for (let i of questionElement) {
    if (i.nodeName === "P") {
      question.question += `${i.innerHTML} `
    } else {
      for (let j of i.children[0].children) {
        j.innerText !== "" ? question.answers.push(j.innerText) : undefined
        try {
          if (j.lastElementChild.classList.contains("choicegroup_correct")) {
            question.correctAnswer.push(j.innerText)
          }
        } catch (e) { }
      }
    }
  }

  quizData.push(question)
}

document.getElementById("SchATData").innerHTML += `<br><div id="learnParsedData">${JSON.stringify(quizData)}</div>`
