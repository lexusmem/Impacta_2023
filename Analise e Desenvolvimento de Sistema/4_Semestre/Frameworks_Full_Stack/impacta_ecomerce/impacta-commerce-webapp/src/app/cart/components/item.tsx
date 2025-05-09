import ItemQuantity from "./ItemQuantity";

function Item(props) {
    const defaultProductImage = "https://placehold.co/150x150?text=Produto&font=roboto";

    return (
        <div className="container my-2">
            <div className="row">
                <div className="col-2">
                    <img src={defaultProductImage} className="img-thumbnail" />
                </div>
                <div className="col-6 py-5">
                    <h5>{props.product.title}</h5>
                </div>
                <div className="col-2 py-5">
                    <ItemQuantity product={props.product} />
                </div>
                <div className="col-2 py-5 text-end">
                    <h4>R$ {props.product.unitPrice * props.product.qty}</h4>
                </div>
            </div>
        </div>
    );
}

export default Item;