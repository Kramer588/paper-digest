/* paper-digest 1.2.0 · quiz.js — 选择题即时反馈 + 自由回忆对比 */
(function () {
  function initQuiz(root) {
    var q = root.querySelector(".q");
    var labels = root.querySelectorAll("label");
    var explain = root.querySelector(".explain");
    labels.forEach(function (lb) {
      lb.addEventListener("click", function () {
        labels.forEach(function (x) { x.style.background = ""; });
        lb.style.background = lb.dataset.correct === "true" ? "#e8f6ee" : "#fdecec";
        if (explain) explain.classList.add("show");
      });
    });
  }
  document.querySelectorAll("[data-quiz]").forEach(initQuiz);

  // 自由回忆：显示参考要点（默认隐藏），让用户先写再对照
  document.querySelectorAll("[data-recall]").forEach(function (box) {
    var id = box.getAttribute("data-recall");
    var ref = document.getElementById(id + "-ref");
    var btn = box.parentElement.querySelector("[data-show-ref]");
    if (btn && ref) btn.addEventListener("click", function () { ref.hidden = !ref.hidden; });
  });

  // data-write：英文写作练习，显示参考句与自检清单
  document.querySelectorAll("[data-write]").forEach(function (box) {
    var btn = box.querySelector("[data-show-model]");
    var model = box.querySelector(".model");
    if (btn && model) btn.addEventListener("click", function () {
      model.hidden = !model.hidden;
      btn.textContent = model.hidden ? "查看参考句与自检" : "收起参考";
    });
  });
})();