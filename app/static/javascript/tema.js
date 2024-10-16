// Script para alternar entre dark e light themes
const toggleButton = document.getElementById("theme-toggle");
const htmlElement = document.documentElement;

// Função para definir o tema
function setTheme(theme) {
  htmlElement.classList.remove("light", "dark");
  htmlElement.classList.add(theme);
  localStorage.setItem("theme", theme);
}

// Função para aplicar o tema inicial com base na preferência do usuário
function applyInitialTheme() {
  const savedTheme = localStorage.getItem("theme");
  const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;

  if (savedTheme) {
    setTheme(savedTheme);
  } else {
    setTheme(prefersDarkScheme ? "dark" : "light");
  }
}

// Função para alternar o tema
toggleButton.addEventListener("click", () => {
  if (htmlElement.classList.contains("dark")) {
    setTheme("light");
  } else {
    setTheme("dark");
  }
});

// Aplicar o tema ao carregar a página
window.onload = applyInitialTheme;
