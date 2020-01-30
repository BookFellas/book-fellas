let search = $('#input-search')

$('#button-search').on('click', function(btn){
    btn.preventDefault();
    if (search.val() != "") {
        $('#status').html('Loading...');
        seedDB(search.val());
    }
})

$('#input-search').on('keyup', function(key) {
    key.preventDefault();
    if (key.keyCode === 13 && search.val() != "") {
        $('#status').html('Loading...');
        seedDB(search.val());
    }
})

function seedDB (link) {
    $.ajax({
        url: '/seed_db/',
        method: 'GET',
        datatype: 'json',
        data: {
            link: link + '&maxResults=40'
        },
        success: (data) => {
            if (data.status === 'ok') {
                $('#status').html('Database has been updated successfully');
            } else {
                $('#status').html('Failed to seed the database!');
            }
            
        },
        error: (err) => {
            console.log(err);
            $('#status').html('Failed to seed the database!');
        }
    });
}
$('.add-to-cart').on('submit', function(e){
    e.preventDefault()
    $.ajax({
        url: '/books/',
        method: 'POST',
        data: ,
        success: (data) =>{
            $('.alert').alert()
            $('.alert').html('Successfully added to the cart')
        },
        error: () => {
            console.log(err);
            $('.alert').alert()
            $('.alert').html('Out of Stock')
        }
    })
}
