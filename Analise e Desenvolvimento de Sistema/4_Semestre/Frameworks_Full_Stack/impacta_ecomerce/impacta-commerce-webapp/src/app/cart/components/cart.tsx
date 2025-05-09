import ItemsList from "./itemsList";
import Summary from "./summary";

const initialCartData = {
    "products": [
        {
            "title": "Caneca Personalizada de Porcelana",
            "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-pers-porc.jpg",
            "qty": 1,
            "unitPrice": 123.45
        },
        {
            "title": "Caneca Importada Personalizada em Diversas Cores",
            "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-import-colors.jpg",
            "qty": 2,
            "unitPrice": 123.45
        },
        {
            "title": "Caneca de Tulipa",
            "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-tuli.jpg",
            "qty": 1,
            "unitPrice": 123.45
        }
    ]
};

function Cart(props) {
    const cartData = props.cart || initialCartData;
    return (
        <div>
            <hr />
            <ItemsList products={cartData.products} />
            <hr />
            <Summary products={cartData.products} />
        </div>
    );
}
export default Cart;