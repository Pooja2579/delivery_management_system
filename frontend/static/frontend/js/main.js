$(document).ready(function() {
    $('#fetch-parcels').click(function() {
        $.ajax({
            url: '/api/parcels/',
            method: 'GET',
            success: function(data) {
                // Update UI with fetched data
                console.log(data);
            }
        });
    });
});

function loadPage(page) {
    $.get(`/pages/${page}`, function(data) {
        $('#main-content').html(data);
    });
}
