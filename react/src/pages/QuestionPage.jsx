import { useEffect, useState } from 'react';
import { Container, Loader, Segment } from 'semantic-ui-react';
import Table from '../components/Table';

const QuestionPage = () => {
	const [answers, setAnswers] = useState(null);
	const [graph, setGraph] = useState(null);

	useEffect(() => {
		fetch('http://localhost:5000/api/answers')
			.then(response => response.json())
			.then(json => {
				setAnswers(json);
			})
			.catch(e => console.error(e));
		fetch('http://localhost:5000/api/airlines/destination/count')
			.then(response => response.blob())
			.then(blob => {
				setGraph(URL.createObjectURL(blob));
			})
			.catch(e => console.error(e));
	}, []);

	return (
		<Container>
			{answers ? (
				<>
					<Segment>
						{/* QUESTION 2 */}
						<h5>
							2. Combien y-a-t-il d’aéroports, de compagnies, de
							destinations, d’avions et de fuseaux horaires ?
						</h5>
						<p>Il y a {answers['question_2'][0]} aéroports</p>
						<p>Il y a {answers['question_2'][1]} compagnies</p>
						<p>Il y a {answers['question_2'][2]} destinations</p>
						<p>Il y a {answers['question_2'][3]} fuseaux horaires</p>
					</Segment>
					<Segment>
						{/* QUESTION 3 */}
						<h5>
							3. Combien y-a-t-il de zones aux Etats-Unis où on ne passe pas
							à l’heure d’été (indice : colonne dst) ?
						</h5>
						<p>
							Il y a {answers['question_3']} fuseaux horaires aux Etats-Unis
							où on ne passe pas à l’heure d’été
						</p>
					</Segment>
					<Segment>
						{/* QUESTION 4 */}
						<h5>
							4. Quel est l’aéroport de départ le plus emprunté ? Quelles
							sont les 10 destinations les plus (moins) prisées ? Quelle
							sont les 10 avions qui ont le plus (moins) décollé ?
						</h5>
						<p>
							Aéroport de départ le plus emprunté:{' '}
							<b>{answers['question_4'][0]}</b>
						</p>
						<b>Les destinations les plus prisées:</b>
						<ul className="list-group">
							{answers['question_4'][1].map((destination, index) => (
								<li className="list-group-item" key={index}>
									{destination}
								</li>
							))}
						</ul>
						<b>Les destinations les moins prisées:</b>
						<ul className="list-group">
							{answers['question_4'][2].map((destination, index) => (
								<li className="list-group-item" key={index}>
									{destination}
								</li>
							))}
						</ul>
						<br />
						<b>Les Avions qui ont le plus décollés:</b>
						<ul className="list-group">
							{answers['question_4'][3].map((destination, index) => (
								<li className="list-group-item" key={index}>
									{destination}
								</li>
							))}
						</ul>
						<br />
						<b>Les Avions qui ont le moins décollés:</b>
						<ul className="list-group">
							{answers['question_4'][4].map((destination, index) => (
								<li className="list-group-item" key={index}>
									{destination}
								</li>
							))}
						</ul>
					</Segment>
					<Segment>
						{/* QUESTION 5 */}
						<h5>
							5. Trouver combien chaque compagnie a desservi de destination
							; combien chaque compagnie a desservie de destination par
							aéroport d’origine. Réaliser les graphiques adéquats qui
							synthétisent ces informations ?
						</h5>
						{!!graph && <img src={graph} alt="Graphe compagnie" />}
					</Segment>
					<Segment>
						{/* QUESTION 6 */}
						<h5>
							6.1) Trouver tous les vols ayant atterri à Houston (IAH ou
							HOU) (indice : 9313 vols)
						</h5>
						<Table
							table={answers['question_6'][0]}
							cols={['Flight', 'Origin', 'Destination', 'Time']}
						/>
						<h5>
							6.2) Combien de vols partent de NYC airports vers Seattle
							(indice : 3923 vols) ?
						</h5>
						<p>Il y a {answers['question_6'][1]} vols de NYC à Seattle.</p>
						<h5>
							6.3) Combien de compagnies desservent cette destination
							(indice : 5 compagnies) ?
						</h5>
						<p>
							Il y a {answers['question_6'][2]} compagnies desservent
							Seattle.
						</p>
						<h5>6.4) Combien d’avions “uniques” (indice : 935 avions) ?</h5>
						<p>
							Il y a {answers['question_6'][3]} avions uniques pour Seattle.
						</p>

						{/* QUESTION 7 */}
						<h5>
							7. Trouver le nombre de vols unique par destination voir
							l’aperçu. Trier les vols suivant la destination, l’aéroport
							d’origine, la compagnie dans un ordre alphabétique croissant
							(en réalisant les jointures nécessaires pour obtenir les noms
							des explicites des aéroports) ? indice : voir l’aperçu
						</h5>
						<Table
							table={answers['question_7']}
							cols={['Destination', 'Nombre de vols']}
						/>
					</Segment>
					<Segment>
						{/* QUESTION 8 */}
						<h5>
							8. Quelles sont les compagnies qui n'opèrent pas sur tous les
							aéroports d’origine ? Quelles sont les compagnies qui
							desservent l’ensemble de destinations ? Faire un tableau où
							l’on récupère l’ensemble des origines et des destinations pour
							l’ensemble des compagnies. indice
						</h5>
					</Segment>
					<Segment>
						{/* QUESTION 9 */}
						<h5>
							9. Quelles sont les destinations qui sont exclusives à
							certaines compagnies (indice : 28 destinations en toutalors
							que sur R on trouve 29 pourquoi) ?
						</h5>
					</Segment>
					<Segment>
						{/* QUESTION 10 */}
						<h5>
							10. Filtrer le vol pour trouver ceux exploités par United,
							American ou Delta (indice : 139 504 vols en tout) ?
						</h5>
					</Segment>
				</>
			) : (
				<Loader active inline="centered" />
			)}
		</Container>
	);
};

export default QuestionPage;
