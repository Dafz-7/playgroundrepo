// Start with a count of 0
let count = 0;

// Select the elements
let countDisplay = document.getElementById("count");
let decreaseButton = document.getElementById("decrease");
let increaseButton = document.getElementById("increase");
let resetButton = document.getElementById("reset");
let clearButton = document.getElementById("clear");
let stepInput = document.getElementById("stepSize");

// Save step size whenever user changes it
stepInput.addEventListener("input", () => {
    localStorage.setItem("counterStepInput", stepInput.value);
});

// Load saved value and timestamp if they exist
let savedCount = localStorage.getItem("counterValue");
let savedTimestamp = localStorage.getItem("counterTimestamp");
let savedStepInput = localStorage.getItem("counterStepInput");

// 1. Restore step size FIRST (so we don't overwrite it)
if (savedStepInput != null) {
    stepInput.value = savedStepInput;
}

// 2. Restore count/timestamp
if (savedCount != null) {
    count = parseInt(savedCount);
}

// 3. Render without re-saving step size on first paint
updateDisplay(false);

if (savedTimestamp != null) {
    document.getElementById("lastUpdated").innerText = "Last updated: " + savedTimestamp;
}

// Update the display function
function updateDisplay(saveStep = true) {
    countDisplay.innerText = count;

    // Save the current count
    localStorage.setItem("counterValue", count);

    // Save the timestamp
    let now = new Date().toLocaleString();
    localStorage.setItem("counterTimestamp", now);

    // Tells whether to save step size
    if (saveStep) {
        localStorage.setItem("counterStepInput", stepInput.value);
    }

    // Update the timestamp display
    document.getElementById("lastUpdated").innerText = "Last Updated: " + now;

    if (count > 0) {
        countDisplay.style.color = "green";
    } else if (count < 0) {
        countDisplay.style.color = "red";
    } else {
        countDisplay.style.color = "black";
    }

    // Trigger pop animation reliably
    countDisplay.classList.remove("pulse");
    requestAnimationFrame(() => {
        countDisplay.classList.add("pulse");
    });
}

// Helper function to get step value safely
function getStep() {
    return parseInt(stepInput.value) || 1;
}

// Button actions
increaseButton.onclick = function() {
    count += getStep();
    updateDisplay();
};

decreaseButton.onclick = function() {
    count -= getStep();
    updateDisplay();
};

resetButton.onclick = function() {
    count = 0;
    updateDisplay();
};

clearButton.onclick = function() {
    localStorage.removeItem("counterValue");
    localStorage.removeItem("counterTimestamp");
    localStorage.removeItem("counterStepInput");
    count = 0;
    stepInput.value = 1;

    // Reset display manually
    updateDisplay(false);
    document.getElementById("lastUpdated").innerText = "Last updated: -";
};

// Keyboard controls
document.addEventListener("keydown", (e) => {
    // Ignore keypresses if user is typing in an input (future-proofing)
    const tag = document.activeElement.tagName.toLowerCase();
    if (tag === "input" || tag === "textarea") return;

    if (e.key === "ArrowUp") {
        count += getStep();
        updateDisplay();
    } else if (e.key === "ArrowDown") {
        count -= getStep();
        updateDisplay();
    } else if (e.key.toLowerCase() === "r") {
        count = 0;
        updateDisplay();
    } else if (e.key.toLowerCase() === "c") {
        localStorage.removeItem("counterValue");
        localStorage.removeItem("counterTimestamp");
        localStorage.removeItem("counterStepInput");
        count = 0;
        stepInput.value = 1;

        // Update UI without re-saving step size
        updateDisplay(false);
        document.getElementById("lastUpdated").innerText = "Last updated: -";
    }
});