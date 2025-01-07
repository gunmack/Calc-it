function appendToExpression(value) {
  const expr = document.getElementById("expression");
  expr.value += value;
}
function clearExpression() {
  document.getElementById("expression").value = " ";
}

function deleteLastCharacter() {
  const expr = document.getElementById("expression");
  expr.value = expr.value.slice(0, -1);
}

document.addEventListener("keydown", function (event) {
  const key = event.key;

  // Prevent default behavior for certain keys (like Enter and Backspace)
  if (key === "Enter" || key === "Backspace") {
    event.preventDefault();
  }

  // Numbers and symbols
  if (key >= "0" && key <= "9") {
    appendToExpression(key);
  }

  // Operators
  if (
    key === "+" ||
    key === "-" ||
    key === "*" ||
    key === "/" ||
    key === "(" ||
    key === ")"
  ) {
    appendToExpression(key);
  }

  // Decimal point
  if (key === ".") {
    appendToExpression(key);
  }

  // Backspace (DEL)
  if (key === "Backspace") {
    deleteLastCharacter();
  }

  // Evaluate expression with Enter
  if (key === "Enter") {
    // Submit form (since the button is a submit)
    document.querySelector("form").submit();
  }
});
