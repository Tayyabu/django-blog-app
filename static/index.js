const subject = document.querySelector("#subject");
const subjects_list = ["Python", "Django", "Flask", "NodeJs", "React", "Redux"];
let text_i = 0;
let word_i = 0;
let word = subjects_list[word_i];
let timer = 300;

let new_text = "";

setInterval(() => {
  new_text += word.charAt(text_i);

  subject.textContent = new_text;

  text_i++;

  if (text_i > word.length) {
    text_i = 0;

    new_text = "";

    word_i++;

    if (word_i > subjects_list.length - 1) {
      word_i = 0;
      text_i = 0;
    }

    word = subjects_list[word_i];
  }
}, timer);

window.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("article").forEach((el) => {
    el.classList.add("translate-x-0");
  });
});

window.addEventListener("load", () => {
  document.querySelectorAll("article").forEach((el) => {
    if (!el.classList.contains("translate-x-0")) {
      el.classList.toggle("translate-x-0");
    }
  });
});









