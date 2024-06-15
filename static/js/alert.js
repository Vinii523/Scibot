// alerts.js
function showMultipleAlerts() {
    var alertMessages = [
        'This is the first message.',
        'Here is the second message.',
        'And this is the third message.'
    ];

    function showAlert(index) {
        if (index < alertMessages.length) {
            alert(alertMessages[index]);
            showAlert(index + 1);
        }
    }

    showAlert(0);
}
