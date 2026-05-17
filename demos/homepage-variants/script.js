const links = Array.from(document.querySelectorAll("[data-variant-link]"));
const sections = Array.from(document.querySelectorAll("[data-variant]"));
const requestedVariant = new URLSearchParams(window.location.search).get("variant");

if (requestedVariant) {
  document.body.dataset.previewVariant = requestedVariant;
}

const setActive = () => {
  const midpoint = window.scrollY + window.innerHeight / 2;
  const active = sections.find((section) => {
    const top = section.offsetTop;
    const bottom = top + section.offsetHeight;
    return midpoint >= top && midpoint < bottom;
  });

  if (!active) return;

  links.forEach((link) => {
    const selected = link.dataset.variantLink === active.dataset.variant;
    link.classList.toggle("is-active", selected);
    if (selected) {
      link.setAttribute("aria-current", "page");
    } else {
      link.removeAttribute("aria-current");
    }
  });
};

setActive();
window.addEventListener("scroll", setActive, { passive: true });
window.addEventListener("resize", setActive);
