import { useEffect, useState } from 'react';
import { Container, Header, Loader, Tab } from 'semantic-ui-react';
import AirportBoard from '../components/AirportBoard';

const HomePage = () => {
	const [airports, setAirports] = useState([]);

	useEffect(() => {
		console.log('load airports');
		fetch('http://localhost:5000/api/airports/origin')
			.then(response => response.json())
			.then(response => {
				if (response.airports) setAirports(response.airports);
			})
			.catch(e => console.error(e));
	}, []);

	return (
		<Container className="home">
			<Header as="h1">Home</Header>
			{airports.length ? (
				<Tab
					panes={airports.map(airport => ({
						menuItem: airport.name,
						render: () => (
							<Tab.Pane>
								<AirportBoard key={airport.faa} airport={airport} />
							</Tab.Pane>
						),
					}))}
				/>
			) : (
				<Loader active inline="centered" />
			)}
		</Container>
	);
};

export default HomePage;