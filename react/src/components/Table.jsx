import { Table } from 'semantic-ui-react';

const AutoTable = ({ table, cols, className }) => (
	<Table basic className={className}>
		<Table.Header>
			<Table.Row>
				{cols.map(col => (
					<Table.HeaderCell key={col}>{col}</Table.HeaderCell>
				))}
			</Table.Row>
		</Table.Header>
		<Table.Body>
			{table.map((row, i) => (
				<Table.Row key={i}>
					{row.map((value, index) => (
						<Table.Cell key={index}>{value}</Table.Cell>
					))}
				</Table.Row>
			))}
		</Table.Body>
	</Table>
);

export default AutoTable;
