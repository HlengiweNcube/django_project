document.addEventListener("DOMContentLoaded", function () {
    var startDate = document.getElementById("id_start_date");
    var endDate = document.getElementById("id_end_date");

    if (startDate && endDate) {
        function validateDateRange() {
            if (!startDate.value || !endDate.value) {
                endDate.setCustomValidity("");
                return;
            }

            if (new Date(endDate.value) < new Date(startDate.value)) {
                endDate.setCustomValidity("End date cannot be before start date.");
            } else {
                endDate.setCustomValidity("");
            }
        }

        startDate.addEventListener("change", validateDateRange);
        endDate.addEventListener("change", validateDateRange);
    }

    var password1 = document.getElementById("id_password1");
    var password2 = document.getElementById("id_password2");

    if (password1 && password2) {
        function validatePasswordMatch() {
            if (!password2.value) {
                password2.setCustomValidity("");
                return;
            }

            if (password1.value !== password2.value) {
                password2.setCustomValidity("Passwords do not match.");
            } else {
                password2.setCustomValidity("");
            }
        }

        password1.addEventListener("keyup", validatePasswordMatch);
        password2.addEventListener("keyup", validatePasswordMatch);
    }
});
