import {useState, useEffect} from "react";
import {IconChevronLeft, IconChevronRight} from "@tabler/icons-react";

const Slide = ({images}) => {
    const [currentIndex, setCurrentIndex] = useState(0);

    useEffect(() => {
        const timer = setTimeout(() => {
            goNext();
        }, 5000);

        return () => clearTimeout(timer); // Esto limpia el timer si el componente se desmonta
    }, [currentIndex]); // Este efecto se vuelve a ejecutar cada vez que currentIndex cambia

    const goPrev = () => {
        if (currentIndex === 0) {
            setCurrentIndex(images.length - 1);
        } else {
            setCurrentIndex(currentIndex - 1);
        }
    };

    const goNext = () => {
        if (currentIndex === images.length - 1) {
            setCurrentIndex(0);
        } else {
            setCurrentIndex(currentIndex + 1);
        }
    };

    return (
        <div className="relative w-full h-full"> {/* Cambiado de h-96 a h-full */}
            {images.map((image, index) => (
                <img
                    key={index}
                    src={image}
                    alt={`Slide ${index}`}
                    className={`absolute w-full h-full object-cover transition-opacity duration-300 ${currentIndex === index ? 'opacity-100' : 'opacity-0'}`}
                />
            ))}
            <button
                className="absolute top-1/2 left-0 transform -translate-y-1/2 bg-black bg-opacity-50 text-white p-2"
                onClick={goPrev}>
                <IconChevronLeft/>
            </button>
            <button
                className="absolute top-1/2 right-0 transform -translate-y-1/2 bg-black bg-opacity-50 text-white p-2"
                onClick={goNext}>
                <IconChevronRight/>
            </button>

        </div>
    );
}

export default Slide;
