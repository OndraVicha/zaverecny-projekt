 $(document).ready(function () {
      // Přidání události pro změnu hodnocení
      $('.rating input').change(function () {
        const modelId = $(this).data('model-id');
        const ratingContainer = $(this).closest('.rating-container').find('.rating');
        rateModel(modelId, ratingContainer);
      });

      // Funkce pro odeslání hodnocení pomocí AJAX
      function rateModel(modelId, ratingContainer) {
        const rating = $('input[name="rating"]:checked').val();
        $.ajax({
          url: `/rate/${modelId}/`,
          method: 'POST',
          data: { rating: rating },
          success: function (data) {
            // Aktualizace zobrazení hvězdiček po úspěšném hodnocení
            displayStars(data.rating, ratingContainer);
          },
          error: function (error) {
            console.error('Failed to rate the model:', error);
          },
        });
      }

      // Funkce pro zobrazení hvězdiček
      function displayStars(rating, container) {
        container.empty();
        for (let i = 1; i <= 5; i++) {
          const star = $('<span class="icon">★</span>');
          if (i <= rating) {
            star.addClass('active');
          }
          container.append(star);
        }
      }
      $('.rate-model').click(function () {
        const modelId = $(this).closest('.rating-container').find('.rating').data('model-id');
        const ratingContainer = $(this).closest('.rating-container').find('.rating');
        rateModel(modelId, ratingContainer);
    });
    });