var hobbies = document.querySelectorAll(".hobby-container img");

hobbies.forEach(hobby => {
  hobby.parentElement.addEventListener("mouseover", () => {
    const altText = hobby.getAttribute('alt');
    const hobby_label = document.createElement('div');
    hobby_label.classList.add('hobby_label');
    hobby_label.textContent = altText;
    hobby.parentNode.parentNode.insertBefore(hobby_label, hobby.parentNode.nextSibling);
  });
  hobby.parentElement.addEventListener('mouseout', () => {
    const hobby_label = hobby.parentNode.parentNode.querySelector('.hobby_label');
    if (hobby_label) {
      hobby_label.parentNode.removeChild(hobby_label);
    }
  });
});