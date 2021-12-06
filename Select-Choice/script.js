const tagsEl = document.getElementById("tags");
const textarea = document.getElementById("textarea");

// Automatically have user inside text box
textarea.focus();

textarea.addEventListener("keyup", (e) => {
  createTags(e.target.value);

  if (e.key === "Enter") {
    // Clear input after 10ms
    setTimeout(() => {
      e.target.value = "";
    }, 10);

    randomSelect();
  }
});

textarea.addEventListener("keyup", (e) => {
  createTags(e.target.value);
});

function createTags(input) {
  // split = seperate index according to comma
  // filter = pass through items that match the filter
  // map = add item to array
  const tags = input
    .split(",")
    .filter((tag) => tag.trim() !== "")
    .map((tag) => tag.trim());

  // Clear tags element
  tagsEl.innerHTML = "";

  // Place create tag element for each element in array
  tags.forEach((tag) => {
    const tagEl = document.createElement("span");
    tagEl.classList.add("tag");
    tagEl.innerText = tag;
    tagsEl.appendChild(tagEl);
  });
}

function randomSelect() {
  const times = 30;

  const interval = setInterval(() => {
    const randomTag = pickRandomTag();
  }, 100);
}

function pickRandomTag() {
  const tags = document.querySelectorAll(".tag");
  return tags[Math.floor(Math.rondom() * tags.length)];
}

function highlightTag(tag) {
  tag.classList.add("highlight");
}
function unHighlightTag(tag) {
  tag.classList.remove("highlight");
}
