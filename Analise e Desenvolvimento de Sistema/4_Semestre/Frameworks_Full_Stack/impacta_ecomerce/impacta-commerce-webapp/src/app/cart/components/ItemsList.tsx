import Item from "./item";

function ItemsList(props) {

    let rows = [];

    props.products.forEach((product, index) => {
        rows.push(<Item key={index} product={product} />);
    });

    return <div>{rows}</div>;
}

export default ItemsList;