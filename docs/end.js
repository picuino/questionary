//
// Copyright (c) 2021 James Q Quick
// https://github.com/jamesqquick/Build-A-Quiz-App-With-HTML-CSS-and-JavaScript
//
// Copyright (c) 2021 Carlos Pardo
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

const endDiv = document.getElementById('end');
const title = sessionStorage.getItem('mostRecentTitle');
const mostRecentScore = Number(sessionStorage.getItem('mostRecentScore')).toFixed(0) + "%";

var watermarkLenght=3;

function setFinalScore() {
  if (watermarkLenght == 3) {
     endDiv.innerHTML = "";
     endDiv.insertAdjacentHTML("afterbegin", "<h1>" + title + "</h1> <h1>" + mostRecentScore + "</h1> <h1>- - -</h1>");
     watermarkLenght = 4;
  } 
  else {
     endDiv.innerHTML = "";
     endDiv.insertAdjacentHTML("afterbegin", "<h1>" + title + "</h1> <h1>" + mostRecentScore + "</h1> <h1>- - - -</h1>");
     watermarkLenght = 3;
  }
};

const result = setFinalScore();

const interval = setInterval(setFinalScore, 1000);