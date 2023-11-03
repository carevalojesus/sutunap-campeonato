import {useEffect, useState} from "react";
import {getAllTeams, getAllGroups} from "../api/backend.api.js";

const PositionsTable = () => {
    const [teams, setTeams] = useState([]);
    const [selectedGroup, setSelectedGroup] = useState(null);

    useEffect(() => {
        async function loadTeams() {
            const res = await getAllTeams();
            setTeams(res.data);
        }

        async function loadGroups() {
            const res = await getAllGroups();
            if(res.data.length > 0) {
                setSelectedGroup(res.data[0]);  // seleccionar el primer grupo por defecto
            }
        }

        loadTeams();
        loadGroups();
    }, []);

    const TeamRow = ({teamId, index}) => {
        const team = teams.find(t => t.id === teamId);
        if(!team) return null;  // si el equipo no se encuentra, no renderizar nada

        return (
            <div className="grid grid-cols-6 gap-4 py-2 items-center">
                <div className="text-lg font-bold">{String(index).padStart(2, '0')}</div>
                <div className="col-span-2 flex items-center">
                    <img src={team.logo} alt={`Logo de ${team.name}`} className="h-8 w-8 ml-2"/>
                    <span className="ml-2">{team.name}</span>
                </div>
                <div>17</div>   {/* Aquí podrías obtener los datos reales de cada equipo */}
                <div>36</div>
                <div>18</div>
                <div className="flex space-x-2">
                    <span className="bg-green-500 text-white p-1 rounded">10</span>
                    <span className="bg-yellow-500 text-white p-1 rounded">6</span>
                    <span className="bg-red-500 text-white p-1 rounded">1</span>
                </div>
            </div>
        );
    };

    if(!selectedGroup) return null;  // si no hay grupo seleccionado, no renderizar nada

    return (
        <div>
            <div className="bg-daintree-500 text-white font-bold p-2">
                <div className="grid grid-cols-6 gap-4">
                    <div>POS</div>
                    <div>EQUIPO</div>
                    <div>PJ</div>
                    <div>PTS</div>
                    <div>DG</div>
                    <div>RESULTADOS</div>
                </div>
            </div>
            <div className="border-t border-gray-200">
                {selectedGroup.teams.map((teamId, index) => (
                    <TeamRow key={teamId} teamId={teamId} index={index + 1}/>
                ))}
            </div>
        </div>
    )
}

export default PositionsTable;
