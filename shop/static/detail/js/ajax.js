// var user = '{{ user }}'
// var product = '{{ product }}'
// $('#id_product').val(product);
// $('#id_quantity').val(1);
// $('#id_user').val(user);

// var slug = '{{ product.slug }}'
// $('#slug').val(slug);

if (typeof form !== 'undefined'){
    console.log('form');
    console.log(form);
    // add article
    add(form)
}else{
    console.log('no form');
}
    

    function add(form){
        $(form).submit(
        function(event) {
        event.preventDefault();
        console.log('click');
        var item_id = this.id.toString();
        console.log('submit', item_id);


        // AJAX for posting
        var serializedData = $(this).serialize();

    console.log("create post is working!") // sanity check
        $.ajax({
        // envoi les donnee ver db
        type: 'POST',
        url: "create_post",
        data: serializedData,


        success: function (response) {
            // on successfull creating object
            // 1. clear the form.
            // $('#form').trigger('reset');
            // // 2. focus to nickname input 
            // $("#id_title").focus();
            console.log('succec in db');

            // display the newly friend to table.
            var instance = JSON.parse(response["instance"]);
            var fields = instance[0]["fields"];

            // $("#my_articles tbody").prepend(
            //     `<tr>
            //     <td>${fields["title"]||""}</td>
            //     // <td>${fields["quantity"]||""}</td>
            //     </tr>`
            // )
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    })
    })}


// for refresh db for Cart

$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type:'GET',
            url:"get_data_cart",
            success: function(response){
                console.log(response);
            },
            error: function(response){
                console.log('error');
            }
        })
    }, 2500)
})
