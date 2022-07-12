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
            // refresh()---------------------------------------------------------------------------
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


// // for refresh db for Cart
// item_nbr = ''
// $(document).ready(function(){
//     setInterval(function(){
//         $.ajax({
//             type:'GET',
//             url:"get_data_cart",
//             success: function(response){
//                 //console.log(response);
//                 // empty pour rendre vide
//                 $('#items_listation').empty()
//                 // $('#items').append('<h5>Cart list</h5>')
//                 // console.log(response)
//                 let item_nbr = ''
//                 let item_str =  `<h5> Cart list</h5>`
//                 for(key in response.articles){
//                     // console.log('fd:', response.articles[key].product);
//                     // var temp = 
//                     // `<h5 >${response.articles[key].product}, nbr:${response.articles[key].quantity}</h5>`
//                     // $('#items').append(temp);

//                     item_nbr = `<tr>
//                                     <th scope="row">${response.articles[key].product}</th>
//                                     <th>  ${response.articles[key].quantity}</th>
//                                     <th >$ ${response.articles[key].product}</th>
//                                     </tr>`
//                     $('#items_listation').append(item_nbr);

//                     item_popo =`${response.articles[key].product}  x ${response.articles[key].quantity}<br>`

//                     item_str +=item_popo
//                     // $('#items').append(temp);
//                 }
//                 document.getElementById('cart-popo').setAttribute('data-bs-content', item_str)
//                 },
//             error: function(response){
//                 console.log('error');
//             }
//         })
//     }, 1500)
// })



// //  popover


// var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
// var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
//     return new bootstrap.Popover(popoverTriggerEl, {html:true}), 
// document.getElementById('cart-popo').setAttribute('data-bs-content', item_nbr)
// })
