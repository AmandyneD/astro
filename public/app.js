const result = document.querySelector("#result");
const hint = document.querySelector("#hint");
const form = document.querySelector("#form");
const birth = document.querySelector("#birth");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  result.textContent = "";
  hint.textContent = "Calcul en cours…";

  const date = birth.value; // "YYYY-MM-DD"
  try {
    const res = await fetch("/api/zodiac", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ date })
    });

    const data = await res.json();

    if (data.error) {
      hint.textContent = "";
      result.textContent = data.error;
      return;
    }

    hint.textContent = "";
    result.textContent = `Ton signe est : ${data.sign} ♈️`;
  } catch (err) {
    hint.textContent = "";
    result.textContent = "Erreur : impossible de contacter l’API.";
    console.error(err);
  }
});
