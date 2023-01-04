history.replaceState(null, '', 'bar5.html');
// rename the url 

jQuery.getJSON(window.Shopify.routes.root + 'products/orange-new-flame-slinky-skirt-set.js', function(product) {
  console.log((product));
} );

// AJAX request in shopify

$( ".FlexonEm" ).load(" .FlexonEm > *" );
$('.Product').load(document.URL +  ' .Product>*');
////////////////////////////////////////////////////////////
<script type="text/javascript">
function recp() {
  setInterval(function() 
  {
    $("#result").load(location.href+ ' #my');
  });
}
</script>

<div id="result">
  <div id="my"><?php echo date('a:i:s'); ?></div>
</div>
////////////////////////////////////////////////////////////
//Refresh

$jq(".color_item").click(function(e) {
    
    e.preventDefault();
    console.log("Hello");
});
// No Page refresh on click



// REFRESH ORDER SUMMARY
jQuery.getJSON('/cart.js', function(cart) {
        let cartData = cart.items;
        document.dispatchEvent(new CustomEvent('cart:build' , {bubbles: true})); 
        document.dispatchEvent(new CustomEvent('cart:refresh', {
            bubbles: true,
             detail: cartData
        })); 
   });
