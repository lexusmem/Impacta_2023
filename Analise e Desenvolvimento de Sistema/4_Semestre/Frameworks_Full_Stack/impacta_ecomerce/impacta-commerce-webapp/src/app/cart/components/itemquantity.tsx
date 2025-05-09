function ItemQuantity(props) {
    return (
        <div className="input-group mb-3">
            <button className="btn btn-outline-secondary" type="button">
                -
            </button>
            <input
                type="number"
                className="form-control text-center"
            />
            <button className="btn btn-outline-secondary" type="button">
                +
            </button>
        </div>
    );
}
export default ItemQuantity;