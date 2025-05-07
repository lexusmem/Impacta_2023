import styles from './styles/styles.module.css'

function Installment(props) {
    const fees = props.installment.hasFee ? 'com juros' : 'sem juros';

    return (
        <p>
            em {props.installment.number}x de R$ {props.installment.total} {fees}
        </p>
    );

}

function ProductListItem(props) {
    const defaltProductImage = "https://placehold.co/150x150?text=Produto&font=roboto";

    return (
        <div className={styles.rowItem}>
            <img src={defaltProductImage} className="flex-shrink-0 me-3" />
            <div className={styles.itemText}>
                <a href="#" className="stretched-link">
                    <h3 className="mt-0">{props.product.title}</h3>
                </a>
                <h4>R$ {props.product.amount}</h4>
                <Installment installment={props.product.installments} />
            </div>
        </div>
    );
}

export default function ProductsForSaleList() {
    const json_products = [
        {
            title: "Caneca Personalizada de Porcelana",
            amount: 123.45,
            installments: { number: 3, total: 41.15, hasFee: true },
        },
        {
            title: "Caneca de Tulipa",
            amount: 123.45,
            installments: { number: 3, total: 41.15 },
        },
    ];

    const products = json_products.map((x, index) => (
        <ProductListItem product={x} key={index} />
    ));

    return <div className={styles.container}>{products}</div>;

}