history.replaceState(null, '', 'bar5.html');
// rename the url 

jQuery.getJSON(window.Shopify.routes.root + 'products/orange-new-flame-slinky-skirt-set.js', function(product) {
  console.log((product));
} );

// AJAX request in shopify

$( ".FlexonEm" ).load(" .FlexonEm > *" );
//Refresh
