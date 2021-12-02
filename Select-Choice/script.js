const tagEl = document.getElementById("tags");
const textarea = document.getElementById("textarea");

// Automatically have user inside text box
textarea.focus();

textarea.addEventListener("keyup", (e) => {
  createTags(e.target.value);
});

function createTags(input) {
  // split = seperate index according to comma
  //
  const tags = input
    .split(",")
    .filter((tag) => tag.trim() !== "")
    .map((tag) => tag.trim());

  console.log(tags);
}
