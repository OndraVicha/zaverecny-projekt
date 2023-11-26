document.addEventListener('DOMContentLoaded', function() {
    var modelCards = document.querySelectorAll('.w3-card-3');

    modelCards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            var details = card.querySelector('.model-details');
            var pageDetails = document.querySelector('.page-details');
            details.style.display = 'block';
            pageDetails.classList.add('active');
        });

        card.addEventListener('mouseout', function() {
            var details = card.querySelector('.model-details');
            var pageDetails = document.querySelector('.page-details');
            details.style.display = 'none';
            pageDetails.classList.remove('active');
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
