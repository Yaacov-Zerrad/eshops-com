// var user = '{{ user }}'
// var product = '{{ product }}'
// $('#id_product').val(product);
// $('#id_quantity').val(1);
// $('#id_user').val(user);

// // var slug = '{{ product.slug }}'
// // $('#slug').val(slug);

// // not googggggggggggggggggggggggggggggggggggggggggggggggggggggddddddddddddddddddddddddddddddddddd
// //  a cause du liebn faut changer avec create_post

//         $('#form').submit(function(event) {
//             event.preventDefault();
//             console.log('click');
//             var item_id = this.id.toString();
//             console.log('submit', item_id);


//             // AJAX for posting
//             var serializedData = $(this).serialize();

//         console.log("create post is working!") // sanity check
//             $.ajax({
//             // envoi les donnee ver db
//             type: 'POST',
//             url: "{% url 'shop:add_article' %}",
//             data: serializedData,


//             success: function (response) {
//                 // on successfull creating object
//                 // 1. clear the form.
//                 // $('#form').trigger('reset');
//                 // // 2. focus to nickname input 
//                 // $("#id_title").focus();
//                 console.log('succec in db');

//                 //display the newly friend to table.
//                 // var instance = JSON.parse(response["instance"]);
//                 // var fields = instance[0]["product"];
//                 // $("#my_articles tbody").prepend(
//                 //     `<tr>
//                 //     <td>${fields["title"]||""}</td>
//                 //     // <td>${fields["quantity"]||""}</td>
//                 //     </tr>`
//                 // )
//             },
//             error: function (response) {
//                 // alert the error if any error occured
//                 alert(response["responseJSON"]["error"]);
//             }
//         })
//     })








    


// <!-- <script>
// $(document).on('mouseenter', '.add', function(e){
// // preventing from page reload and default actions
// e.preventDefault();
// let id = $(this).attr('id')
// var type= $(this).attr("data-id");
// id = '#'+id
// console.log('id:', id);

// // serialize the data for sending the form data.
// // make POST ajax call
// $(id).submit(function(event) {
//     console.log('click');
//     event.preventDefault();


//     var serializedData = $(this).serialize();
//     console.log("create post is working!", serializedData) // sanity check
//     event.preventDefault();
    
//     let formData = new FormData();
//     formData.append('slug', 'dfg');
//     //formData.append('b', document.querySelector("#b").value);

//     let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     const request = new Request('{% url "shop:slug_article" %}', {
//         method: 'POST',
//         body: formData
//     });
//     fetch(request)
//         .then(response => response.json())
//         .then(result => {
//             const resultElement = document.querySelector("#ajax");
//             resultElement.innerHTML = result["operation_result"];
//         })
//     })


// });

// </script> -->

// <!-- <script>


// console.log('js marche');





// $(document).on('submit',function(e){
// console.log('submit');

// // preventing from page reload and default actions
// e.preventDefault();

// let item_slug =  e.target.id
// console.log(item_slug);

// // serialize the data for sending the form data.
// var serializedData = $(this).serialize();
// console.log('dfgh',serializedData);

// $.ajax({
// // envoi les donnee ver db
// type: 'POST',
// url: "{% url 'shop:add_user_article' %}",
// data: serializedData,

// success: function (response) {
//     // on successfull creating object
//     // 1. clear the form.
//     $("#article_form").trigger('reset');
//     // 2. focus to nickname input 
//     $("#id_title").focus();
//     console.log('succec in db');

//     //display the newly friend to table.
//     var instance = JSON.parse(response["instance"]);
//     var fields = instance[0]["fields"];
//     $("#my_articles tbody").prepend(
//         `<tr>
//         <td>${fields["title"]||""}</td>
//         <td>${fields["quantity"]||""}</td>
//         </tr>`
//     )
// },
// error: function (response) {
//     // alert the error if any error occured
//     alert(response["responseJSON"]["error"]);
// }
// });

// });


// </script> -->



