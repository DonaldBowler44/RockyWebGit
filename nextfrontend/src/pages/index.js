import Image from "next/image";
import { useState, useEffect } from "react";
import styles from "../styles/index.module.css"
import rockyFace from "../../public/images/rockyface.png";
import apolloFace from "../../public/images/apolloface.png";
import ivanFace from "../../public/images/ivanface.png";
import langFace from "../../public/images/langface.png";
import tommyFace from "../../public/images/tommyface.jpg";
import masonFace from "../../public/images/masonface.jpg";
import adonisFace from "../../public/images/adonisface.png";
import dannyFace from "../../public/images/wheelerface.png";
import rickyFace from "../../public/images/rickyface.png";
import viktorface from "../../public/images/viktorface.png";
import damienFace from "../../public/images/damianface.png";
import { charInfo } from "@/api";
import { charResults } from "@/api";

export default function HomePage() {
    useEffect(() => {
        const fetchData = async () => {
            const characters = await Promise.all(
                data.map(async (character) => {
                    const characterInfo = await charInfo(character.id);
                    return {
                        ...character,
                        ...characterInfo
                    };
                })
            );
            setData(characters);
        };

        fetchData();
    }, []);

    const [data, setData] = useState([
        {
            id: 1,
            name: "Rocky Balboa",
            img: rockyFace,
            stance: "southpaw",
        },
        {
            id: 2,
            name: "Apollo Creed",
            img: apolloFace,
            stance: "orthodox"
        },
        {
            id: 3,
            name: "Ivan Drago",
            img: ivanFace,
            stance: "southpaw"
        },
        {
            id: 4,
            name: "Clubber Lang",
            img: langFace,
            stance: "southpaw"
        },
        {
            id: 5,
            name: "Tommy Gun",
            img: tommyFace,
            stance: "orthodox"
        },
        {
            id: 6,
            name: "Mason Dixon",
            img: masonFace,
            stance: "orthodox"
        },
        {
            id: 7,
            name: "Adonis Creed",
            img: adonisFace,
            stance: "orthodox"
        },
        {
            id: 8,
            name: "Danny Wheeler",
            img: dannyFace,
            stance: "orthodox"
        },
        {
            id: 9,
            name: "Ricky Conlan",
            img: rickyFace,
            stance: "orthodox"
        },
        {
            id: 10,
            name: "Viktor Drago",
            img: viktorface,
            stance: "orthodox"
        },
        {
            id: 11,
            name: "Damien Anderson",
            img: damienFace,
            stance: "orthodox"
        },
    ]);
    const [selectedCharacter, setSelectedCharacter] = useState(data[0]);

    //this is for the second character menu
    const [selectCharTwo, setSelectedCharTwo] = useState(data[0]);

    //this is results usestate
    const [result, setResult] = useState(null);

    const getCharacter = async (character) => {
        const characterInfo = await charInfo(character.id);
        console.log('Character Data', character);
        setSelectedCharacter({ ...character, ...characterInfo });
    };

    //second getChar
    const getCharTwo = async (character) => {
        const characterInfo = await charInfo(character.id);
        console.log('Character DataTwo', character);
        setSelectedCharTwo({ ...character, ...characterInfo })
    };

    const calcCharStanceColor = (stance) => {
        if (stance === "Southpaw") {
            return 'bg-rose-500'
        } else if (stance === 'Orthodox') {
            return 'bg-cyan-500'
        } else if (stance === 'SouthpawOrthodox (Rocky II)') {
            return 'bg-rose-500'
        } else {
            return 'bg-rose-500'
        }
    };

    const handleResultsClick = async () => {
        // Retrieve Ids of selected char.s
        const id1 = selectedCharacter.id;
        const id2 = selectCharTwo.id;

        // call the charresults funct
        const resultData = await charResults(id1, id2);

        setResult(resultData);
    }

    return (
        <>
            <div className="container mx-auto">
                <main>
                    <div classname="boxerone"><h1 style={{ color: 'white' }}>For Boxer 1:</h1></div>
                    <section className="grid grid-cols-6">
                        {data.map((character) => (
                            <div
                                key={character.id}
                                className="character-profile border-solid border-2 border-black"
                                onClick={() => getCharacter(character)}
                            >
                                <div className={styles.imageContainer}>
                                    <Image
                                        src={character.img}
                                        alt={character.name}
                                        style={{ objectFit: "cover", width: "100%", height: "100%" }}
                                    />
                                </div>

                                <div className={calcCharStanceColor(character.stance)}>
                                    <p className="text-white text-center font-bold uppercase">
                                        {character.name}
                                    </p>
                                </div>
                            </div>
                        ))}
                    </section>
                    <div classname="boxerone"><h1 style={{ color: 'white' }}>For Boxer 2:</h1></div>
                    <section className="grid grid-cols-6">
                        {data.map((character) => (
                            <div
                                key={character.id}
                                className="character-profileTwo border-solid border-2 border-black"
                                onClick={() => getCharTwo(character)}
                            >
                                <div className={styles.imageContainer}>
                                    <Image
                                        src={character.img}
                                        alt={character.name}
                                        style={{ objectFit: "cover", width: "100%", height: "100%" }}
                                    />
                                </div>

                                <div className={calcCharStanceColor(character.stance)}>
                                    <p className="text-white text-center font-bold uppercase">
                                        {character.name}
                                    </p>
                                </div>
                            </div>
                        ))}
                    </section>
                </main>

                {/* this is where double div starts */}
                <div className={styles.doubleheadercont}>
                    <div className="header">
                        <div>
                            <div className="boxerone"><h1 style={{ color: 'black' }}>Boxer 1:</h1></div>
                            {selectedCharacter ? (
                                <div key={selectedCharacter.id}>
                                    <h1>{selectedCharacter.name}</h1>
                                    <h1>{selectedCharacter.stance}</h1>
                                    <p>{selectedCharacter.height}</p>
                                    <p>{selectedCharacter.weight}</p>
                                    <p>Total fights: {selectedCharacter.total_fights}</p>
                                    <p>Wins: {selectedCharacter.wins}</p>
                                    <p>Wins by KO: {selectedCharacter.wins_by_ko}</p>
                                    <p>Losses: {selectedCharacter.losses}</p>
                                    <p>Draws: {selectedCharacter.draws}</p>
                                </div>
                            ) : (
                                <div>
                                    <p>Loading...</p>
                                </div>
                            )}
                        </div>
                    </div>
                    {/* for button and results div */}
                    <div className={styles.butandResultstab}>
                        <button className={styles.buttStyle} onClick={handleResultsClick}>Results</button>
                        <div className={styles.resTab}>
                            {result ? (
                                // This works through the parsing of the json object
                                <div>
                                    <h2>Results:</h2>
                                    <p>Boxer One: {result.characterOne}</p>
                                    <p>Winning Probability: {result.characterOne_E_A_Value}</p>
                                    <p>Updated ELO Rating: {result.characterOne_upR_A_Value}</p>
                                    <p>Boxer Two: {result.characterTwo}</p>
                                    <p>Winning Probability: {result.characterTwo_E_B_Value}</p>
                                    <p>Updated ELO Rating: {result.characterTwo_upR_B_Value}</p>
                                </div>
                            ) : (
                                <p>No results yet.</p>
                            )}
                            {/* characterOne, characterTwo, characterOne_E_A_Value, characterTwo_E_B_Value, characterOne_upR_A_Value, characterTwo_upR_B_Value */}
                        </div>
                    </div>
                    {/* for char two */}
                    <div className="header">
                        <div>
                            <div className="boxerone"><h1 style={{ color: 'black' }}>Boxer 2:</h1></div>
                            {selectCharTwo ? (
                                <div key={selectCharTwo.id}>
                                    <h1>{selectCharTwo.name}</h1>
                                    <h1>{selectCharTwo.stance}</h1>
                                    <p>{selectCharTwo.height}</p>
                                    <p>{selectCharTwo.weight}</p>
                                    <p>Total fights: {selectCharTwo.total_fights}</p>
                                    <p>Wins: {selectCharTwo.wins}</p>
                                    <p>Wins by KO: {selectCharTwo.wins_by_ko}</p>
                                    <p>Losses: {selectCharTwo.losses}</p>
                                    <p>Draws: {selectCharTwo.draws}</p>
                                </div>
                            ) : (
                                <div>
                                    <p>Loading...</p>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
                {/* this is where double header divs go */}
            </div>
        </>
    );
}