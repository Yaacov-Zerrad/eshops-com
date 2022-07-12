

// // for refresh db for Cart
// item_nbr = ''
// $(document).ready(function(){
//     setInterval(function(){
//         console.log('refresh ready');
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
//                 // for num cart
//                 let length = response.articles.length
//                 $('#cart').empty()
//                 document.getElementById('cart').append(length)
//                 // for total qte
//                 $('#id_qte').val(length)
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


//         function refresh(){
//         console.log('refrech submit'),
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
//     }

// refresh()

//     item_nbr = ''
//     $(document).ready(function(){
//         setInterval(refresh()
//             , 1500)
//     })

// //  popover


// var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
// var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
//     return new bootstrap.Popover(popoverTriggerEl, {html:true}), 
// document.getElementById('cart-popo').setAttribute('data-bs-content', item_nbr)
// })
