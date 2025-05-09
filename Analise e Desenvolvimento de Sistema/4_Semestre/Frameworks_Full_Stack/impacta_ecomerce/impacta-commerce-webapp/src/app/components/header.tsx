import Link from 'next/link';
import { FaShoppingCart } from 'react-icons/fa';

interface HeaderProps {
    // Você pode passar props para o seu header se precisar de informações dinâmicas
}

const Header: React.FC<HeaderProps> = () => {
    return (
        <header className='p-6 md:p-6 lg:p-6'>
            <div className="bg-white py-1 px-3 flex items-center justify-between border">
                <div>
                    <Link href="/" className="text-black-800 hover:text-blue-500 text-decoration: underline">
                        PRODUTOS
                    </Link>
                </div>

                <div className="flex items-center space-x-2">
                    <FaShoppingCart className="mr-2" />
                    <Link href="/cart" className="text-black-1000 hover:text-blue-500 flex items-center ">
                        <span className='text-decoration: underline'>CARRINHO DE COMPRAS</span>
                    </Link>
                </div>
            </div>
            <div className="flex-grow text-center bg-gray-200 py-20 border-b border-l border-r">
                <h1 className="text-xl font-semibold text-black-1000">Impacta Commerce</h1>
            </div>
        </header>
    );
};

export default Header;