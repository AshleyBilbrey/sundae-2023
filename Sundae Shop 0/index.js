import express from 'express';
import bodyParser from 'body-parser'
import cookieParser from 'cookie-parser'
//import ejs from 'ejs';

const app = express();
const port = 3007;

app.set('view engine', 'ejs');
app.set('views', './views');
app.use(express.static("./static"))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(cookieParser())

const flavorList = {
  "vanilla": { name: "Vanilla", price: "3.49" },
  "chocolate": { name: "Chocolate", price: "3.49" },
  "strawberry": { name: "Strawberry", price: "4.99" },
  "neapolitan": { name: "Neapolitan", price: "4.49" },
  "rockyou": { name: "Rocky You.txt Road", price: "6.49" },
  "intel": { name: "Intel Chocolate Chip", price: "5.49" },
  "amd": { name: "AMD Chocolate Chip", price: "5.49" },
  "nvidia": { name: "Nvidia Chocolate Chip", price: "5.49" },
  "flag": { name: "Flag Fudge", price: "129.99" }
}

app.get('/', (req, res) => {
  let cart = getCartInfo(req.cookies['session'])
  res.render("index.ejs", { flavorList: flavorList, message: "", cartCount: cart.numItems ? cart.numItems : cart.numItems ? cart.numItems : 0 });
});

app.post('/', (req, res) => {
  try {
    let sendMessage = "";
    let cart = getCartInfo(req.cookies['session']);


    // Verify Validity
    for (const item in req.body.items) {

      if (!flavorList[item]) {
        sendMessage = "Something went wrong.";
        return res.render("index.ejs", { flavorList: flavorList, message: sendMessage, cartCount: cart.numItems ? cart.numItems : 0 });
      }

      if (!Number.isInteger(req.body[item]) || req.body[item] > 5 || req.body[item] < 1) {
        sendMessage = "Something went wrong.";
        return res.render("index.ejs", { flavorList: flavorList, message: sendMessage, cartCount: cart.numItems ? cart.numItems : 0 });
      }

    }

    // Alter Cart
    console.log(req.body)
    for (const item in req.body) {
      console.log(item)
      console.log(req.body[item])
      console.log(Number(req.body[item]))
      console.log(cart)
      console.log(item in cart.items)
      if (!(item in cart.items)) {
        console.log(req.body[item])
        cart.items[item] = Number(req.body[item]);
      } else {
        cart.items[item] = Number(cart.items[item]) + Number(req.body[item]);
      }

      if(!cart.numItems) {
        cart.numItems = Number(req.body[item]);
      } else {
        cart.numItems = Number(cart.numItems) + Number(req.body[item]);
      }
    }

    res.cookie("session", setCartInfo(cart));
    sendMessage = "Successfully added to cart!"
    return res.render("index.ejs", { flavorList: flavorList, message: sendMessage, cartCount: cart.numItems ? cart.numItems : 0 });
  } catch (e) {
    console.log(e)
    return res.send("Something went wrong.")
  }

})

function getCartInfo(cookie) {
  console.log(cookie)
  if(!cookie) return {items: {}, numItems: 0}
  let decoded = atob(cookie);
  let json = JSON.parse(decoded);
  return json;
}

function setCartInfo(cart) {
  console.log(cart)
  let jsonString = JSON.stringify(cart);
  let encoded = btoa(jsonString);
  return encoded;
}

app.get("/cart", (req, res) => {
  let cart = getCartInfo(req.cookies['session']);
  res.render("cart.ejs", { cart: cart, flavorList: flavorList })
})

app.get("/checkout", (req, res) => {
  let cart = getCartInfo(req.cookies['session']);
  res.clearCookie("session");
  if(cart.items.flag && cart.items.flag > 0) {
    res.render("checkout.ejs", {message: "Thank you for your order. moo{sk1p_g0_d0_n0t_coll3ct_sund43}"})
  } else {
    res.render("checkout.ejs", {message: "Thank you for your order."})
  }
})

app.get("/clearcart", (req, res) => {
  res.clearCookie("session");
  res.redirect("/")
}) 

app.use((req, res, next) => {
  res.status(404).send("The catgirl you are looking for is in another castle.")
})

app.listen(port, () => {
  console.log(`Sundae Shop listening on port ${port}`);
});