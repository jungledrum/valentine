

var page = require('webpage').create();
var args = require('system').args;

var url = args[1]
// console.log(url)

page.open(url, function (status) {
    page.includeJs("http://cdn.staticfile.org/jquery/2.1.0/jquery.min.js", function() {

        var product = page.evaluate(function() {
            var price = $(".tm-price").text()
            var name = $(".tb-detail-hd").find("h3").text().trim()
            var banner = $(".tm-brand").find("em").text()
            var images = []
            $("#J_UlThumb").find("img").each(function(){
                images.push($(this).attr("src"))
            })
            var product = {
                "price": price,
                "name": name,
                "banner": banner,
                "images": images
            }
            return product
        });
        // console.log(product.price);
        // console.log(product.name);
        // console.log(product.banner);
        // console.log(product.images);
        product_json = JSON.stringify(product)
        console.log(product_json)
        phantom.exit()
      });    

});
