const questions = [
    {
        questions:"Which of the following is not a programming language?",
        answers:[
            {text:"Python" , correct: false},
            {text:"Java" , correct: false},
            {text:"HTML" , correct: true},
            {text:"C++" , correct: false}
        ]
    },
        {
     questions:"What does CSS stand for?",
        answers:[
            {text:"Computer Style Sheets" , correct: false},
            {text:"Creative Style Sheets" , correct: false},
            {text:"Cascading Style Sheets" , correct: true},
            {text:"Colorful Style Sheets" , correct: false}
        ]
    },
 {
    questions:"Which method is used to add an element at the end of an array in JavaScript?",
    answers:[
        {text:"push()", correct: true},
        {text:"pop()", correct: false},
        {text:"shift()", correct: false},
        {text:"unshift()", correct: false}
    ]
},
    {
     questions:"What is the main difference between let and var in JavaScript?",
        answers:[
            {text:"let is block-scoped, var is function-scoped" , correct: true},
            {text:"let is function-scoped, var is block-scoped" , correct: false},
            {text:"let is global-scoped, var is local-scoped" , correct: false},
            {text:"let is local-scoped, var is global-scoped" , correct: false}
        ]
    },
    {
     questions:"What does the === operator do in JavaScript?",
        answers:[
            {text:"It compares both value and datatype" , correct: true},
            {text:"It compares only value" , correct: false},
            {text:"It compares only datatype" , correct: false},
            {text:"It is not a valid operator in JavaScript" , correct: false}
        ]
    },

];
 const questionElement = document.getElementById("question");
 const answerButtons = document.getElementById("answer-buttons");
 const nextButton = document.getElementById("next-btn");

 let currentQuestionIndex = 0;
 let score = 0;

 function startQuiz(){
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerHTML = "Next";
    showQuestion();
 }

    function showQuestion(){
        resetState();
        let currentQuestion = questions[currentQuestionIndex];
        let questionNo = currentQuestionIndex + 1;
        questionElement.innerHTML = questionNo + "." + currentQuestion.questions;
        currentQuestion.answers.forEach(answer =>{
             const button = document.createElement("button");
             button.innerHTML = answer.text;
             button.classList.add("btn");
             answerButtons.appendChild(button);
             if(answer.correct){
                button.dataset.correct = answer.correct;
             }
             button.addEventListener("click",selectAnswer);

        });

    }

    function resetState(){
        nextButton.style.display = "none";
        while(answerButtons.firstChild){
            answerButtons.removeChild(answerButtons.firstChild)
        }
    }

    function selectAnswer(e){
        const selectedBtn = e.target;
        const isCorrect =  selectedBtn.dataset.correct === "true";
        if(isCorrect){
            selectedBtn.classList.add("correct");
            score++;
        }else{
            selectedBtn.classList.add("incorrect");
        }
        Array.from(answerButtons.children).forEach(button => {
            if(button.dataset.correct === "true"){
                button.classList.add("correct");
            }
            button.disabled =  true;
        } );
        nextButton.style.display = "block";

    }

    function showScore(){
        resetState();
        questionElement.innerHTML = `You scored ${score} out of ${questions.length}!`;
        nextButton.innerHTML = "Play Again";
        nextButton.style.display = "block";
    }

    function handleNextButton(){
        currentQuestionIndex++;
        if(currentQuestionIndex < questions.length){
            showQuestion();
        }else{
            showScore();
        }
    }
    nextButton.addEventListener("click",()=>{
      if(currentQuestionIndex < questions.length){
          handleNextButton();
      }else{
        startQuiz();
      }
    });
    startQuiz();


