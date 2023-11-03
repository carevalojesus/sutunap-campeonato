import {useEffect, useState} from "react";
import imagen1 from "../../public/images/pexels-franco-monsalvo-15365073.jpg";
import imagen2 from "../../public/images/pexels-franco-monsalvo-14030575.jpg";
import imagen3 from "../../public/images/pexels-franco-monsalvo-14030573.jpg";
import Slide from "../components/Slide.jsx";
import Header from "../components/Header.jsx";
import {getAllPhases, getAllGroups} from "../api/backend.api.js";
import PositionsTable from "../components/PositionsTable.jsx";

export default function HomePage() {

    const [phases, setPhases] = useState([]);
    const [groups, setGroups] = useState([]);
    const [selectedPhase, setSelectedPhase] = useState(null);


    /*useEffect(() => {
        async function loadPhases() {
            const res = await getAllPhases();
            setPhases(res.data)
        }

        async function loadGroups() {
            const res = await getAllGroups();
            setGroups(res.data)
        }

        loadPhases();
        loadGroups();
    }, []);
    */
    useEffect(() => {
        async function loadPhases() {
            const res = await getAllPhases();
            setPhases(res.data);

            // Establecer la primera fase como la seleccionada por defecto
            if (res.data && res.data.length > 0) {
                setSelectedPhase(res.data[0].id.toString());
            }
        }

        loadPhases();
    }, []);

    useEffect(() => {
        if (selectedPhase) {
            async function loadGroups() {
                const res = await getAllGroups();
                setGroups(res.data);
            }

            loadGroups();
        }
    }, [selectedPhase]);

    return (
        <>
            <div className="flex flex-col h-screen"> {/* Contenedor principal como flex */}
                <Header/>
                <div className="flex-grow"> {/* El slider ocupa el espacio restante */}
                    <Slide images={[
                        imagen1,
                        imagen2,
                        imagen3
                    ]}/>
                </div>
            </div>
            <main className="py-10">
                <div className="max-w-7xl mx-auto grid grid-cols-6 gap-x-4">
                    <div className="col-span-4">
                        <h2 className="uppercase font-bold text-lg text-gray-700 tracking-wide border-l-8 border-l-daintree-500 pl-2">COPA
                            SUTUNAP: Tabla de Posiciones</h2>
                        <div className="my-4 flex space-x-4">
                            <div className="flex-1">
                                <select
                                    id="phaseSelect"
                                    name="phaseSelect"
                                    className="mt-2 block w-full border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-daintree-600 sm:text-sm sm:leading-6"
                                    onChange={e => setSelectedPhase(e.target.value)}
                                    value={selectedPhase} // Establecer el valor seleccionado
                                >
                                    {
                                        phases.map((phase) => (
                                            <option key={phase.id} value={phase.id}>{phase.name}</option>
                                        ))
                                    }
                                </select>
                            </div>
                            <div className="flex-1">
                                <select
                                    id="groupSelect"
                                    name="groupSelect"
                                    className="mt-2 block w-full border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-daintree-600 sm:text-sm sm:leading-6"
                                >
                                    {
                                        groups.map((group) => {
                                            if (group.is_active && group.phase === parseInt(selectedPhase, 10)) { // Convierte selectedPhase a número para comparar
                                                return (
                                                    <option key={group.id} value={group.id}>{group.name}</option>
                                                )
                                            }
                                            return null;
                                        })
                                    }
                                </select>
                            </div>
                        </div>

                        <PositionsTable/>

                    </div>
                    <div className="col-sm-pull-2">
                        <h2>Hola</h2>
                    </div>
                </div>
            </main>
        </>
    )
}
