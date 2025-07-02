let slides = [];
let currentIndex = 0;

const container = document.getElementById("slide-container");
const arrows = document.getElementById("arrow-controls");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const confirmBtn = document.getElementById("confirmBtn");

// Load slides
fetch("slides.json")// path changing to real json
    .then(res => res.json())
    .then(data => {
        slides = data.map(slide => ({ ...slide, confirmed: false })); // add confirmed flag
        renderSlide(currentIndex);
    })
    .catch(err => {
        console.error("Fehler beim Laden der Slides:", err);
    });

function renderSlide(index) {
    const slide = slides[index];

    container.innerHTML = `
    <div class="slide-card">
      <h1 class="fw-bold">${slide.title}</h1>
      <p>📅 ${slide.day}</p>
      <p>📍 ${slide.address}</p>
      <p>👥 ${slide.participants}</p>
      ${slide.confirmed ? `<p class="text-success fw-semibold mt-3">✅ Zugestimmt</p>` : ""}
    </div>
  `;

    container.appendChild(arrows); // Reattach arrows inside slide container

    // Reset animation
    const card = container.querySelector('.slide-card');
    card.classList.remove("slide-card");
    void card.offsetWidth;
    card.classList.add("slide-card");

    // Show/hide arrows
    prevBtn.style.visibility = index === 0 ? "hidden" : "visible";
    prevBtn.style.opacity = index === 0 ? "0" : "1";

    nextBtn.style.visibility = index === slides.length - 1 ? "hidden" : "visible";
    nextBtn.style.opacity = index === slides.length - 1 ? "0" : "1";
}

prevBtn.addEventListener("click", () => {
    if (currentIndex > 0) {
        currentIndex--;
        renderSlide(currentIndex);
    }
});

nextBtn.addEventListener("click", () => {
    if (currentIndex < slides.length - 1) {
        currentIndex++;
        renderSlide(currentIndex);
    }
});

confirmBtn.addEventListener("click", () => {
    slides[currentIndex].confirmed = !slides[currentIndex].confirmed;
    renderSlide(currentIndex);
});