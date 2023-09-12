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
const datetimeScore = Number(sessionStorage.getItem('datetimeScore')).toFixed(0);
const mostRecentScore = calculateScore((sessionStorage.getItem('mostRecentScore') ^ datetimeScore) & 0xFFFF) + "%";


var watermark=1;

function setFinalScore() {
  var title2 = title;
  if (title2 === null) {
     var title2 = "Test no realizado.";
  } 

  if (watermark == 1) {
     endDiv.innerHTML = "";
     endDiv.insertAdjacentHTML("afterbegin", "<h1 style=\"font-size:48px\">" + title2
     + "</h1> <h1 style=\"font-size:80px\">" + mostRecentScore 
     + "</h1> <h1>- - - - - -</h1> <p style=\"margin-top:64px\"></p> <a class=\"btn\""
     + "href=\"index.html\">Índice de los Test</a>");

     watermark = 2;
  } 
  else if (watermark == 2) {
     endDiv.innerHTML = "";
     endDiv.insertAdjacentHTML("afterbegin", "<h1 style=\"font-size:48px\">" + title2
     + "</h1> <h1 style=\"font-size:80px\">" + mostRecentScore 
     + "</h1> <h1>= = = = =</h1> <p style=\"margin-top:64px\"></p> <a class=\"btn\"" 
     + "href=\"index.html\">Índice de los Test</a>");

     watermark = 1;
  }
};

function calculateScore(val) {
   dateInterval = Date.now() - datetimeScore;
   if ((dateInterval > 0) && (dateInterval < 1000*300)) {
      if (val>0x8000) return val-0x10000;
      else return val;
   }
   return 0;
}

const result = setFinalScore();

const interval = setInterval(setFinalScore, 500);