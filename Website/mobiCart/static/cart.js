let carts = document.querySelectorAll(".addtocart");

let products=[
    {
        name:'Apple Airpods',
        tag:'airpods',
        price:14900,
        inCart:0
    },
    {
        name:'Apple Airpods Pro',
        tag:'airpodspro',
        price:24900,
        inCart:0
    }
    ]

for (let i = 0; i < carts.length; i++)
    {
        carts[i].addEventListener('click',() =>
        {
              cartNumber(products[i]);   
              totalCost(products[i]);
        })
    }

function cartNumber(product)
{
    
    let productNumber = localStorage.getItem('cartNumber');
    
    
    productNumber=parseInt(productNumber);
    
    if( productNumber)
        {
            localStorage.setItem('cartNumber', productNumber+1);
            //document.querySelector('.club1 span').textContent = productNumber + 1;
        }
    else
        {
            localStorage.setItem('cartNumber', 1);
            //document.querySelector('.club1 span').textContent = 1;
        }
    setItems(product);
}
function setItems(product)
{
    let cartItems = localStorage.getItem('productInCart');
    cartItems = JSON.parse(cartItems);
    
    
    if(cartItems != null)
        {
            if(cartItems[product.tag] == undefined)
                {
                    cartItems ={
                        ...cartItems,
                        [product.tag]:product
                    }
                }
            cartItems[product.tag].inCart += 1;
        }
    else{
        
    product.inCart = 1;
    
     cartItems = {
         [product.tag]: product
         }
    }
    localStorage.setItem("productInCart", JSON.stringify(cartItems));
}

function totalCost(product)
{
    //console.log("product price:",product.price);
    let cartCost = localStorage.getItem('totalCost');
    
    console.log("My cart cost is:", cartCost);
    
    if(cartCost != null)
        {
            cartCost = parseInt(cartCost);
            localStorage.setItem('totalCost', cartCost + product.price);
        }
    else
        {
            localStorage.setItem("totalCost", product.price);
        }
    
}

function displayCart()
{
   let cartItem = localStorage.getItem("productInCart");
    cartItem = JSON.parse(cartItem);
    //
    //console.log(typeof cartItem);
    let productContainer = document.querySelector(".products-container");
    //console.log(productContainer);
    console.log(cartItem);
    if(cartItem && productContainer)
        {
            console.log("running");
            /*productContainer.innerHTML ='';
            Object.values(cartItem).map(item =>{
                productContainer.innerHTML += `
     <div class="product">
        <button type="button" id="remove">REMOVE ITEM</button>
<img src="./images/$(item.tag).jpg">
<span>$(item.name)</span>
</div>
     `
            });
            
       */ }
}
//displayCart();