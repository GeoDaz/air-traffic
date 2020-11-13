import { useEffect, useState } from 'react';
import { Header, Loader, Segment } from 'semantic-ui-react';
import TableObject from '../components/TableObject';

const AirportBoard = ({ airport }) => {
	const [flights, setFlights] = useState([]);

	useEffect(() => {
		if (airport) {
			fetch('http://localhost:5000/api/airports/' + airport.faa)
				.then(response => response.json())
				.then(response => {
					if (response.flights) setFlights(response.flights);
				})
				.catch(e => console.error(e));
		}
	}, [airport]);

	return (
		<Segment color="blue">
			<Header>Vols au départ de l'aéroport {airport.name}</Header>
			{flights.length ? (
				<TableObject
					table={flights}
					cols={[
						{ key: 'flight', content: 'Vol' },
						{ key: 'origin', content: 'Départ' },
						{ key: 'dest', content: 'Destination' },
						{ key: 'airline', content: 'Compagnie' },
						{ key: 'plane', content: 'Avion' },
						{ key: 'date', content: 'Date' },
					]}
				/>
			) : (
				<Loader active inline="centered" />
			)}
		</Segment>
	);
};

export default AirportBoard;
