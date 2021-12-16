var place = 0;

document.addEventListener("DOMContentLoaded", function (event) {
  //the event occurred

  var element = document.getElementsByClassName("handle");
  var st = element.length;
  var place = st;
  console.log(place);
  for (let i = 0; i < st; i++) {
    let handle = element[i].getAttribute("data-value");

    //console.log(handle);
    let p = "/products/" + handle + ".js";
    let stuff = element[i];
    //console.log(stuff);

    jQuery
      .getJSON(p)

      .done(function (product) {
        //console.log(product);
        var x = product.images.at(-1);
        var address = "https:" + x;

        var index = address.search(".jpg");

        var addressSml =
          address.slice(0, index) + "_600x600" + address.slice(index);

        stuff.style.backgroundImage = `url('${addressSml}')`;
      })
      .fail(function (product) {
        stuff.parentElement.parentElement.remove();
        place--;
      });
  }

  var btn = document.getElementById("gsloadmore");

  btn.onclick = function () {
    var time = setInterval(() => {
      var element = document.getElementsByClassName("handle");

      if (element.length > place) {
        //the event occurred

        var stop = element.length;

        var start = place;

        for (let i = start; i < stop; i++) {
          let handle = element[i].getAttribute("data-value");

          //console.log(handle);
          let p = "/products/" + handle + ".js";
          let stuff = element[i];
          //console.log(stuff);

          jQuery
            .getJSON(p)

            .done(function (product) {
              //console.log(product);
              var x = product.images.at(-1);
              var address = "https:" + x;

              var index = address.search(".jpg");

              var addressSml =
                address.slice(0, index) + "_600x600" + address.slice(index);

              stuff.style.backgroundImage = `url('${addressSml}')`;
            })
            .fail(function (product) {
              stuff.parentElement.parentElement.remove();
              place--;
            });
        }
        place = stop;
        clearInterval(time);
      }
    }, 100);
  };
});
