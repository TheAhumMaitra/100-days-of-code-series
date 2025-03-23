const toggle = document.getElementById("darkmode");

toggle.addEventListener("click", () => {
  const isDark = document.body.classList.toggle("dark-mode");
  toggle.textContent = isDark ? "light_mode" : "dark_mode";
  localStorage.setItem("mode", isDark ? "dark" : "light");
});

window.addEventListener("load", () => {
  const savedMode = localStorage.getItem("mode");
  const isDark = savedMode === "dark";
  document.body.classList.toggle("dark-mode", isDark);
  toggle.textContent = isDark ? "light_mode" : "dark_mode";
});
