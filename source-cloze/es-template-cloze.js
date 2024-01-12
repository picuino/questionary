/*
Copyright (c) 2022 Carlos Félix Pardo Martín

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

*/


const time_between_clues = 1000;
var questions_pages = 0;
var gap_selected = 0;
var page = 0;
var gaps_total = 0;
var gaps_values = [];
var points_total = 0;
var gaps_not_solved = 0;
var watermark = 0;
var interval;
var timeout_clue = 0;
var timeout_last_score = 0;
var final_score_interval;

if (!String.prototype.format) {
   String.prototype.format = function() {
      var args = arguments;
      return this.replace(/{(\d+)}/g, function(match, number) {
         return typeof args[number] != 'undefined'
            ? args[number]
            : match;
      });
   };
}

page_reset();

function page_reset() {
   if (final_score_interval) {
      clearInterval(final_score_interval);
   }
   page = 0;
   points_total = 0;
   if (show_max > 0 && show_max < questions_encoded.length) {
      questions_sorted = questions_sort(show_max);
   }
   else {
      questions_sorted = questions_sort(questions_encoded.length);
   }
   question_numpages = questions_sorted.length;
   gaps_total = questions_gaps();
   gaps_values = get_gaps_values();
   gaps_tries = get_gaps_tries();
   gaps_not_solved = 0;
   fill_question_text(page);
   message_hide();
   hud_show();
}

function bin_atob(str) {
   return decodeURIComponent(atob(str).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));
}

function questions_sort(len) {
   new_questions = JSON.parse(JSON.stringify(questions_encoded));
   questions_sorted = new Array(len);
   for(i=0; i<len; i++) {
      rnd = Math.floor(Math.random() * new_questions.length);
      questions_sorted[i] = new_questions[rnd];
      questions_sorted[i]["Cloze"] = bin_atob(questions_sorted[i]["Cloze"]);
      for(var j=0; j < questions_sorted[i]["Gaps"].length; j++) {
         for(var k=0; k < questions_sorted[i]["Gaps"][j].length; k++) {
            questions_sorted[i]["Gaps"][j][k] = bin_atob(questions_sorted[i]["Gaps"][j][k]);
         };
      };
      new_questions.splice(rnd, 1);
   }
   return questions_sorted;
}

function get_gaps_values() {
   var gaps_values = [];
   for(var page=0; page<questions_sorted.length; page++) {
      gaps_values.push([]);
      for(var num_gap=0; num_gap<questions_sorted[page]["Gaps"].length; num_gap++) {
         gaps_values[page].push(string_to_binary_array(questions_sorted[page]["Gaps"][num_gap][0]));
      };
   };
   return gaps_values;
}

function get_gaps_tries() {
   var gaps_tries = [];
   for(var page=0; page<questions_sorted.length; page++) {
      gaps_tries.push([]);
      for(var num_gap=0; num_gap<questions_sorted[page]["Gaps"].length; num_gap++) {
         gaps_tries[page].push(num_tries);
      };
   };
   return gaps_tries;         
}

function string_to_binary_array(str, chr) {
   array = [];
   if (str.length == 1) {
      array.push(100);
      return array;
   }

   // Valor de las sucesivas letras de una palabra
   for(var i=0; i<str.length; i++) {
      const func = "Lineal";
      if (func === "Exponencial") {
         // Exponencial
         array.push(100 * Math.pow(2, str.length-i-1) / (Math.pow(2, str.length) - 1));
      }
      else {
         // Lineal
         array.push(100 * (1.0 - i / (2*str.length-2)) / (0.75 * str.length));
      };
   };
   return array;
}

function add_terms(array) {
   sum = 0;
   for(var i=0; i<array.length; i++) {
      sum += array[i];
   }
   return sum;
}

function questions_gaps() {
   var gaps = 0;
   for(var page=0; page<questions_sorted.length; page++) {
      gaps += questions_sorted[page]["Gaps"].length;
   };
   return gaps;
};

function final_score_fill() {
   // Load values
   title = sessionStorage.getItem("last_questions_title");
   if (title === null) {
      title = "Puntuación no almacenada";
   }
   points = sessionStorage.getItem("last_questions_points");
   if (points === null) {
      points = 0;
   }

   // Hide HUD
   var hud_element = document.getElementById("hud_id");
   hud_element.style.display = "none";

   // Big header
   var header_element = document.getElementById("header_id");
   header_element.innerHTML = title;
   header_element.style.fontSize = "48px";
   header_element.style.paddingTop = "32px";

   // Show points
   var question_frame_element = document.getElementById("question_frame_id");
   if (watermark == 1) {
      question_frame_element.innerHTML = "";
      question_frame_element.insertAdjacentHTML("afterbegin", "<h1 style=\"font-size:80px\">"
      + Math.round(points) + "%"
      + "</h1> <h1>- - - - - - -</h1>");
      watermark = 2;
   }
   else {
      question_frame_element.innerHTML = "";
      question_frame_element.innerHTML = "";
      question_frame_element.insertAdjacentHTML("afterbegin", "<h1 style=\"font-size:80px\">"
      + Math.round(points) + "%"
      + "</h1> <h1>= = = = = =</h1>");
      watermark = 1;
   }
   buttons_final_score_fill();
};

function buttons_questions_fill() {
   var buttons_frame_element = document.getElementById("buttons_id");
   buttons_frame_element.innerHTML = ''
   + '<button class="func_button" onclick="check_answers()">Comprobar</button>'
   + '<button class="func_button" onclick="show_clue()">Pista</button>'
   + '<button class="func_button" onclick="next_page()">Siguiente</button>'
   + '<br><button class="func_button" onclick="last_score()">Puntuación anterior</button>';
}

function buttons_final_score_fill() {
   var buttons_frame_element = document.getElementById("buttons_id");
   buttons_frame_element.innerHTML = '<button class="func_button" onclick="page_reset()">Reiniciar</button>';
}

function message_show(message) {
   var message_text_element = document.getElementById("message_text_id");
   message_text_element.innerHTML = message;
   var message_element = document.getElementById("message_id");
   message_element.style.display = "inline";
   var button_element = document.getElementById("message_button_id");
   button_element.focus();
}

function message_hide() {
   var message_element = document.getElementById("message_id");
   var message_text_element = document.getElementById("message_text_id");
   message_text_element.innerHTML = "";
   message_element.style.display = "none";

   focus_empty_gap();
}

function focus_empty_gap() {
   var num_gaps = 0;
   var gaps_length = questions_sorted[page]["Gaps"].length;

   while (1) {
      var gap_element = document.getElementById("gap_{0}".format(gap_selected));
      if (gap_element) {
         gap_element.focus();
         break;
      }
      gap_selected += 1;
      if (gap_selected > gaps_length) {
         gap_selected = 0;
      }
      num_gaps += 1;
      if (num_gaps > 100) {
         break;
      }
   }
}

function next_page() {
   message_hide();

   // Check gaps
   var gaps_not_solved = count_blank_answers();

   // Check if all gaps are filled
   if (gaps_not_solved > 0) {
      if (gaps_not_solved == 1) {
         message_show("Aún falta 1 hueco por resolver.");
      }
      else {
         message_show("Aún faltan " + gaps_not_solved + " huecos por resolver.");
      };
      return;
   };

   // Go to next page or final page
   page++;
   if (page < questions_sorted.length) {
      hud_show();
      fill_question_text(page);
   }
   else {
      sessionStorage.setItem('last_questions_title', questions_title);
      sessionStorage.setItem('last_questions_points', points_total);
      final_score_interval = setInterval(final_score_fill, 500);
   }

   // Init variables
   gap_selected = 0;
};

function last_score() {
   if (timeout_last_score === 1) {
      final_score_interval = setInterval(final_score_fill, 500);
   }
   else {
      timeout_last_score = 1;
      setTimeout(reset_timeout_last_score, 400);
      return;
   }
}

function reset_timeout_last_score() {
   timeout_last_score = 0;
}

function questions_page_gaps(page) {
   return questions_sorted[page]["Gaps"].length;
}

function fill_question_text(page) {
   message_hide();
   points_page = 0;

   // Fill header
   var header_element = document.getElementById("header_id");
   header_element.innerHTML = questions_title;
   header_element.style.fontSize = "32px";
   header_element.style.paddingTop = "0px";

   // Fill question frame HTML
   var question_frame_element = document.getElementById("question_frame_id");
   question_frame_element.innerHTML = ''
   + '<div class="question_image_div" id="question_image_div_id"><img src=""></div>'
   + '<div class="question_text" id="question_text_id"></div>';

   // Read variables
   var question_text = questions_sorted[page]["Cloze"];
   var question_image = questions_sorted[page]["Image"][0];
   var question_image_size = questions_sorted[page]["Image"][1];

   // Image
   image_code = '<img class="question_image" src="{0}"{1}>';
   if (question_image_size) {
      var image_values = [question_image, ' width="{0}"'.format(question_image_size)];
   }
   else {
      var image_values = [question_image, ''];
   };
   image_code_formatted = image_code.format(...image_values);
   var question_image_element = document.getElementById("question_image_div_id");
   if (question_image) {
      question_image_element.innerHTML = image_code_formatted;
   }
   else {
      question_image_element.innerHTML = "";
   };

   // Question text
   var gaps_length = questions_sorted[page]["Gaps"].length;
   var gaps_not_solved = gaps_length;
   var gap_span = new Array(gaps_length);
   gap_span_code = '<span class="gap_span" id="gap_span_{0}">'
   + '<input type="text" autocomplete="off" class="gap_box" id="gap_{0}" '
   + 'size="12" onfocus="select_gap({0})" onkeypress="onkeypress_handle({0}, event)"></span>';
   for (var i=0; i<=gaps_length; i++) {
      gap_span[i] = gap_span_code.format(i);
   };
   var question_text_formatted = question_text.format(...gap_span);
   var question_text_element = document.getElementById("question_text_id");
   question_text_element.innerHTML = question_text_formatted;

   // Buttons
   buttons_questions_fill();
   clearInterval(interval);

   // Focus first gap
   var gap_element = document.getElementById("gap_0");
   if (gap_element) {
      gap_element.focus();
   }
}

function hud_show() {
   // Show HUD
   var hud_element = document.getElementById("hud_id");
   hud_element.style.display = "flex";

   // Page HUD
   var hud_page_element = document.getElementById("hud_page_id");
   hud_page_element.innerHTML = 'Página {0}/{1}'.format(page + 1, questions_sorted.length);

   var progress_bar_full_element = document.getElementById("progress_bar_full_id");
   var width = ((page + 1) / questions_sorted.length) * 100;
   progress_bar_full_element.style.width = `${width}%`;

   // Points
   var score_element = document.getElementById("score");
   score_element.innerHTML = Math.round(points_total);
};

function onkeypress_handle(gap, event) {
   if (event.keyCode == 13) {
      event.preventDefault();
      check_answers();
   };
};

function check_answers() {
   message_hide();

   gaps_not_solved = count_blank_answers();

   if (gaps_not_solved > 0) {
      if (gaps_not_solved == 1) {
         message_show("Aún falta 1 hueco por resolver.");
      }
      else {
         message_show("Aún faltan " + gaps_not_solved + " huecos por resolver.");
      };
   }
   else {
      message_show("Todos los huecos están resueltos."
      + "<br>Pulsa <strong>Siguiente</strong> para continuar.");
   }
};

function count_blank_answers() {
   // Leer gaps y comprobar que son correctos
   var gaps_length = questions_sorted[page]["Gaps"].length;
   var gaps_not_solved = gaps_length;
   for (var num_gap=0; num_gap<gaps_length; num_gap++) {
      var gap_element = document.getElementById("gap_{0}".format(num_gap));
      if (gap_element === null || gap_element === 'undefined' ) {
         gaps_not_solved -= 1;
         continue;
      };
      var gap_text = gap_element.value.toLowerCase().trim();
      gap_text.replace(/\s\s+/g, ' ');
      if (gap_text === "") {
         continue;
      };
      var answer = test_answer_correct(page, num_gap, gap_text);
      if (answer !== false) {
         var gap_span_element = document.getElementById("gap_span_{0}".format(num_gap));
         gap_span_element.innerHTML = answer;
         points_total += add_terms(gaps_values[page][num_gap]) / gaps_total;
         hud_show();
         gaps_not_solved -= 1;
      }
      else {
         if (gaps_tries[page][num_gap] === 1) {
            var gap_span_element = document.getElementById("gap_span_{0}".format(num_gap));
            gap_span_element.innerHTML = questions_sorted[page]["Gaps"][num_gap][0];
            gaps_not_solved -= 1;   
         }
         else if (gaps_tries[page][num_gap] > 1) {
            gaps_tries[page][num_gap] -= 1;
         }
      }
   };
   return gaps_not_solved;
}

function test_answer_correct(page, num_gap, gap_text) {
   var num_answers = questions_sorted[page]["Gaps"][num_gap].length;
   for (var j=0; j<num_answers; j++) {
      var answer = questions_sorted[page]["Gaps"][num_gap][j];
      if (gap_text === answer.toLowerCase()) {
         return answer;
      };
   };
   return false;
}

function select_gap(num) {
   gap_selected = num;
};

function reset_timeout_clue() {
   timeout_clue = 0;
}

function show_clue() {
   message_hide();
   if (timeout_clue !== 0) {
      return;
   }
   timeout_clue = 1;
   setTimeout(reset_timeout_clue, time_between_clues);

   var gaps_visited = 0;
   var gaps_length = questions_sorted[page]["Gaps"].length;
   if (gap_selected < 0 || gap_selected >= gaps_length) {
      gap_selected = 0;
   };
   while (true) {
      while (true) {
         if (gaps_visited >= gaps_length) {
            message_show("Todos los huecos están resueltos."
            + "<br>Pulsa <strong>Siguiente</strong> para continuar.");
            return;
         }
         if (gap_selected >= gaps_length) {
            gap_selected = 0;
         }
         var correct_answer = questions_sorted[page]["Gaps"][gap_selected][0];
         var gap_element = document.getElementById("gap_{0}".format(gap_selected));
         if (gap_element === null) {
            gap_selected += 1;
            gaps_visited += 1;
            continue;
         }
         else {
            break;
         };
      }
      var gap_text = gap_element.value.toLowerCase();
      var i = 0;
      while (true) {
         if (i >= correct_answer.length) {
            if (gap_text.length > correct_answer.length) {
               // Correct gap answer with more letters
               gap_element.value = gap_element.value.substr(0, correct_answer.length);
               gap_selected++;
               return;
            }
            // next gap
            gap_selected++;
            if (gap_selected >= gaps_length) {
               return; // No gap to fill
            };
            // Go to next gap
            break;
         };
         if (i >= gap_text.length) {
            gap_text = correct_answer.substr(0, i+1);
            gap_element.value = gap_text;
            gaps_values[page][gap_selected][i] = 0;
            return;
         };
         if (gap_text.charAt(i).toLowerCase() !== correct_answer.charAt(i).toLowerCase()) {
            gap_text = correct_answer.substr(0, i+1);
            gap_element.value = gap_text;
            gaps_values[page][gap_selected][i] = 0;
            return;
         };
         i++;
      };
   };
};
