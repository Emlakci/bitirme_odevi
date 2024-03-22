import { toggleMenus } from "./header.js";
import { changeBrowserLocation } from "./productDetails.js";
import { changeMainImg } from "./shoppingPage.js";

// for activating & de-activating the hamburger menu list
toggleMenus('hamburgerMenu', '.hmbrgr-div')

// for change the product's image in the productDetailPage
changeMainImg();

// for change the Browser url adress to product Details page
changeBrowserLocation();

