//
// Copyright (c) 2021 Carlos Pardo
//
// Copyright (c) 2021 James Q Quick
// https://github.com/jamesqquick/Build-A-Quiz-App-With-HTML-CSS-and-JavaScript
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//

const question = document.getElementById('question');
const questionImage = document.getElementById('questionImage');
const choiceContainers = Array.from(document.getElementsByClassName('choice-container'));
const choices = Array.from(document.getElementsByClassName('choice-text'));
const progressText = document.getElementById('progressText');
const scoreText = document.getElementById('score');
const progressBarFull = document.getElementById('progressBarFull');
const timeBeforeNextQuestion = 1800;
const on = Date.now();

var options = [];
let currentQuestionNumChoices = 0;
let acceptingAnswers = false;
let acceptingScore = false;
let choicesClass = [];
let score = 0;
let questionCounter = 0;
let availableQuestions = [];
let correctAnswer = 0;
let caoq = 0;
let c2aoq = 0;
let maxQuestions = 0;
let questions = [];
let suffleQuestions = true;

var questionBank = sessionStorage.getItem('questionBank');
questionBankMax = sessionStorage.getItem('questionBankMax');


fetch(questionBank)
    .then((res) => {
        return res.json();
    })
    .then((loadedQuestions) => {
        questions = loadedQuestions;
        startGame();
    })
    .catch((err) => {
        console.error(err);
    });


startGame = () => {
    questionCounter = 0;
    score = ((4<<32)+(0x64C2))^on;
    availableQuestions = [...questions];

    options = query_read();
    console.log("Options=", options);
    if (options.indexOf("maxQuestions") >= 0) {
       questionBankMax = questions.length;
    }
    if (options.indexOf("noShuffle") >= 0) {
       suffleQuestions = false;
    }

    if (questionBankMax <= 0 || questionBankMax > questions.length) {
       questionBankMax = questions.length;
    }
    console.log("Number of questions=", questionBankMax);

    getNewQuestion();
};

      
getNewQuestion = () => {
    if (availableQuestions.length === 0 || questionCounter >= questionBankMax) {
        sessionStorage.setItem('mostRecentTitle', sessionStorage.getItem('questionBankTitle'));
        datetimeScore = Date.now();
        sessionStorage.setItem('datetimeScore', datetimeScore);        
        sessionStorage.setItem('mostRecentScore', ((score^on)>>16)^datetimeScore);
        return window.location.assign('end.html');
    }

    questionCounter++;
    progressText.innerText = `Question ${questionCounter}/${questionBankMax}`;
    progressBarFull.style.width = `${(questionCounter / questionBankMax) * 100}%`;

    //shuffle questions
    var questionIndex;
    if (suffleQuestions) {
      questionIndex = Math.floor(Math.random() * availableQuestions.length);
    }
    else {
      questionIndex = 0;
    }
    
    var currentQuestion = availableQuestions[questionIndex];
    currentQuestionNumChoices = currentQuestion.choices.length;
    
    //shuffle choices
    var numbersIndex = 0;
    var numbers = shuffle(currentQuestion.choices.length);
    caoq = Math.floor(Math.random() * 65536) & 0b1111110000111111;
    c2aoq = Math.floor(Math.random() * 16);
    correctAnswer = ((numbers.indexOf('1') + 1) ^ c2aoq) * 64 + caoq;
    
    // Set question, image and choices
    question.innerText = bin_atob(currentQuestion.question);
    questionImage.src = currentQuestion.image;
    questionImage.width = currentQuestion.image_width;
    choiceContainers.forEach(visibleElements);
    choices.forEach((choice) => {
      choice.innerText = bin_atob(currentQuestion['choices'][numbers[numbersIndex]-1]);
      numbersIndex++;
    });
    currentQuestion = {};

    availableQuestions.splice(questionIndex, 1);
    acceptingAnswers = true;
    acceptingScore = true;
    choicesClass = [];
};


function visibleElements(element, index, array) {
    if (index < currentQuestionNumChoices) {
        element.style.display = "";
    }
    else {
        element.style.display = "none";
    }
}


function cleanClass(element, index, array) {
   element[0].classList.remove(element[1]);
}


choices.forEach((choice) => {
   choice.addEventListener('click', (e) => {
      if (!acceptingAnswers)
         return;

      const selectedChoice = e.target;
      const selectedAnswer = Math.floor(selectedChoice.dataset['number']);
      console.log('Selected ' + selectedAnswer);
      var t=Math.floor(correctAnswer/64);t^=c2aoq;t&=15;
      const classToApply = selectedAnswer == t ? 'correct' : 'incorrect';
      var t= 0;
      selectedChoice.parentElement.classList.add(classToApply);
      choicesClass.push([selectedChoice.parentElement, classToApply]);

      if (acceptingScore) {
         acceptingScore = false;

         if (classToApply === 'correct') {
            incrementScore(100.0 / questionBankMax);
         }
         else {
            incrementScore( -(100 / (currentQuestionNumChoices - 1)) / questionBankMax);
         }
      }

      if (classToApply === 'correct') {
          acceptingAnswers = false;
          setTimeout(() => {
             choicesClass.forEach(cleanClass);
             getNewQuestion();
          }, timeBeforeNextQuestion);
      }
   });
});


incrementScore = (num) => {
    score = (score^on)+((num*100)<<16);
    scoretext = (score>>16)&0xFFFF;
    score ^= on;
    if (scoretext > 0x8000) {
       scoretext -= 0x10000;
    }
    scoreText.innerText = (scoretext/100.0).toFixed(0) + "%";
};


function bin_atob(str) {
   if (str == null || typeof str === 'undefined') {
      return str;
   }
   return decodeURIComponent(atob(str).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
   }).join('')).trim();
}


function shuffle(numItems) {
  var array1, array2, index;

  array1 = [];
  for(i = 1; i <= numItems; i++) {
     array1.push(i.toString());
  }

  array2 = [];
  for(i = 1; i <= numItems; i++) {
     index = Math.floor(Math.random() * array1.length);
     array2.push(array1[index]);
     array1.splice(index, 1);
  }

  return array2;
}


// Read query string from URL
function query_read() {
   var url = document.location.href.split('?');
   if (url.length < 2)
      return [];
   var options = url[1].split('&');
   return options;
}
