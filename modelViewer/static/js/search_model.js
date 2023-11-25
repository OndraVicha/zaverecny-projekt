document.addEventListener('DOMContentLoaded', function() {
    var modelCards = document.querySelectorAll('.w3-card-3');

    modelCards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            var details = card.querySelector('.model-details');
            details.style.display = 'block';
        });

        card.addEventListener('mouseout', function() {
            var details = card.querySelector('.model-details');
            details.style.display = 'none';
        });
    });
});

function changeBackgroundColor(element) {
    element.style.backgroundColor = "#2d2c2c";
    element.style.boxShadow = "0px 0px 30px red";
}

function restoreBackgroundColor(element) {
    element.style.backgroundColor = "";
    element.style.boxShadow = "";
}
