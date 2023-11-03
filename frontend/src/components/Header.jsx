import logo_sutunap from "../assets/logo_copa_sutunap.svg";
import {Link} from "react-router-dom";

const Header = () => {
    return (
        <>
            <header className="bg-gradient-to-r from-daintree-500 to-daintree-800 h-24 m-0 p-0">
                <div className="flex justify-center z-10">
                    <svg
                        className="rotate-180 relative z-40"
                        width="190.21"
                        height="155.58"
                        viewBox="0 0 190 155"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M95 0L190.21 58.75L152.5 155.58H37.5L0 58.75L95 0Z" fill="#0C536D"/>
                        <path d="M95 0L190.21 58.75L152.5 155.58H37.5L0 58.75L95 0Z" stroke="#0C536D"/>
                    </svg>
                    <img
                        src={logo_sutunap}
                        alt=""
                        className="absolute w-auto h-28 top-4 z-50"
                    />
                </div>
            </header>
            <nav className="h-12 w-full bg-daintree-950 m-0 p-0">
                <div className="max-w-7xl mx-auto flex items-center h-12 gap-x-8 italic text-daintree-100">
                    <Link to="/" className="text-white uppercase font-semibold text-base">Home</Link>
                    <Link to="/" className="text-white uppercase font-semibold text-base">Fixture</Link>
                    <Link to="/" className="text-white uppercase font-semibold text-base">Tabla de Posiciones</Link>
                    <Link to="/" className="text-white uppercase font-semibold text-base">Equipos</Link>
                </div>
            </nav>
        </>
    )
}

export default Header;