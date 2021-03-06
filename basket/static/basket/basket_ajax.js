    console.log('static');
    //add in basket
    $(document).on('click', '#add-button', function (e) {
      e.preventDefault();
      $.ajax({
        type: 'POST',
        url: "{% url 'basket:basket_add' %}",
        data: {
          productid: $('#add-button').val(),
          // iuf is list deroulante for choices
        //   productqty: $('#select option:selected').text(),
          csrfmiddlewaretoken: "{{csrf_token}}",
          action: 'post'
        },
        // success: function (json) {
        success: function (json) {
          document.getElementById("basket-qty").innerHTML = json.qty
          console.log('success');
        },
        error: function (xhr, errmsg, err) {}
      });
    })
    
        //dimin in basket
    $(document).on('click', '#dimin-button', function (e) {
      e.preventDefault();
      $.ajax({
        type: 'POST',
        url: '{% url "basket:basket_dimin" %}',
        data: {
          productid: $('#dimin-button').val(),
        //   productqty: $('#select option:selected').text(),
          csrfmiddlewaretoken: "{{csrf_token}}",
          action: 'post'
        },
        // success: function (json) {
        success: function (json) {
          document.getElementById("basket-qty").innerHTML = json.qty
          console.log('success');
        },
        error: function (xhr, errmsg, err) {}
      });
    })
    
    
      // Delete Item
      $(document).on("click", ".delete-button", function (e) {
        e.preventDefault();
        var prodid = $(this).data("index");
        console.log(prodid);
        $.ajax({
          type: "POST",
          url: '{% url "basket:basket_delete" %}',
          data: {
            productid: $(this).data("index"),
            csrfmiddlewaretoken: "{{csrf_token}}",
            action: "post",
          },
          success: function (json) {
            console.log('success delete');
            // $('.product-item[data-index="' + prodid + '"]').remove();
    
            // if (json.qty == 0) {
            //   total = 0
            //   subtotal = 0
            // } else {
            //   total = (parseFloat(json.subtotal) + 11.50).toFixed(2);
            //   subtotal = json.subtotal
            // }
    
            // document.getElementById("subtotal").innerHTML = subtotal;
            document.getElementById("basket-qty").innerHTML = json.qty;
            // document.getElementById("total").innerHTML = total;
          },
          error: function (xhr, errmsg, err) {},
        });
      });
    

      // add Item
      $(document).on("click", ".add-button", function (e) {
        e.preventDefault();
        var prodid = $(this).data("index");
        console.log(prodid);
        $.ajax({
          type: "POST",
          url: '{% url "basket:basket_add" %}',
          data: {
            productid: $(this).data("index"),
            csrfmiddlewaretoken: "{{csrf_token}}",
            action: "post",
          },
          success: function (json) {
            console.log('success add');
            // $('.product-item[data-index="' + prodid + '"]').remove();
    
            // if (json.qty == 0) {
            //   total = 0
            //   subtotal = 0
            // } else {
            //   total = (parseFloat(json.subtotal) + 11.50).toFixed(2);
            //   subtotal = json.subtotal
            // }
    
            // document.getElementById("subtotal").innerHTML = subtotal;
            document.getElementById("basket-qty").innerHTML = json.qty;
            // document.getElementById("total").innerHTML = total;
          },
          error: function (xhr, errmsg, err) {},
        });
      });
    









// not besoin
  // Update Item
  $(document).on("click", ".update-button", function (e) {
    e.preventDefault();
    var prodid = $(this).data("index");
    $.ajax({
      type: "POST",
      url: '{% url "basket:basket_update" %}',
      data: {
        productid: $(this).data("index"),
        productqty: $("#select" + prodid + " option:selected").text(),
        csrfmiddlewaretoken: "{{csrf_token}}",
        action: "post",
      },
      success: function (json) {

        total = (parseFloat(json.subtotal) + 11.50).toFixed(2);
        document.getElementById("basket-qty").innerHTML = json.qty;
        document.getElementById("subtotal").innerHTML = json.subtotal;
        document.getElementById("total").innerHTML = total;
      },
      error: function (xhr, errmsg, err) {},
    });
  });