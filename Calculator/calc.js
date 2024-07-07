let display = document.getElementById('display');

function clearDisplay() {
    display.innerText = '';
}

function deleteLast() {
    display.innerText = display.innerText.slice(0, -1);
}

function appendNumber(number) {
    display.innerText += number;
}

function appendOperator(operator) {
    display.innerText += ` ${operator} `;
}

function calculateResult() {
    try {
        let expression = display.textContent;

        // Replace percentage symbol (%) with /100 for evaluation
        expression = expression.replace(/%/g, '/100');

        // Evaluate the expression
        let result = eval(expression);

        // Check if the result is a number
        if (!isNaN(result)) {
            // Round result to 5 decimal places for precision
            result = Math.round((result + Number.EPSILON) * 1e5) / 1e5;
            display.textContent = result;
        } else {
            display.textContent = 'Error';
        }
    } catch (error) {
        display.textContent = 'Error';
    }
}
