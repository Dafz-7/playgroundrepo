// Start with a count of 0
let count = 0;

// Select the elements
let count_display = document.getElementById("count");
let decrease_button = document.getElementById("decrease");
let increase_button = document.getElementById("increase");
let reset_button = document.getElementById("reset");

// Update the display function
function update_display() {
    count_display.innerText = count;

    if (count > 0) {
        count_display.style.color = "green";
    } else if (count < 0) {
        count_display.style.color = "red";
    } else {
        count_display.style.color = "black";
    }
}

// Button actions
increase_button.onclick = function() {
    count++;
    update_display();
};

decrease_button.onclick = function() {
    count--;
    update_display();
};

reset_button.onclick = function() {
    count = 0;
    update_display();
};