
console.log("JS Loaded");
document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");

    searchInput.addEventListener("keyup", function () {

        let filter = searchInput.value.toLowerCase();

        let rows = document.querySelectorAll("#productTable tr");

        rows.forEach(function(row) {

            let text = row.textContent.toLowerCase();

            if (text.includes(filter)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }

        });

    });

});