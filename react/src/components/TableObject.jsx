// module
import { Table } from 'semantic-ui-react';

export const ASC = 'ascending';
export const DESC = 'descending';

/**
 * @prop {array} tableGiven
 * @prop {array} cols
 * @prop {jsx} children
 * @prop {string|undefined} className
 * @prop {array|undefined} sortable
 * @prop {function|undefined} handleSort
 * @prop {string|undefined} orderDirection
 */
export const TableLayout = ({
	cols,
	sortable = false,
	sortedCol,
	handleSort,
	className,
	children,
	orderDirection = ASC,
}) => (
	<Table basic className={className} sortable={sortable}>
		<Table.Header>
			<Table.Row>
				{cols.map(col => {
					if (col.sortable) {
						return (
							<Table.HeaderCell
								className="sortable"
								key={col.key}
								sorted={sortedCol === col.key ? orderDirection : null}
								onClick={e => handleSort(col.key)}
							>
								{col.content}
							</Table.HeaderCell>
						);
					}
					return (
						<Table.HeaderCell key={col.key}>{col.content}</Table.HeaderCell>
					);
				})}
			</Table.Row>
		</Table.Header>
		{/* Table body va peut-être devoir disparaître pour être géré par children */}
		<Table.Body>{children}</Table.Body>
	</Table>
);

export const CellValue = ({ value }) => {
	switch (typeof value) {
		case 'boolean':
			return (
				<Table.Cell positive={value} negative={!value}>
					{value ? 'Oui' : 'Non'}
				</Table.Cell>
			);
		case 'string':
		case 'number':
			return <Table.Cell>{value}</Table.Cell>;
		default:
			return <Table.Cell></Table.Cell>;
	}
};

/**
 * @prop {array} table
 * @prop {array} cols
 * @prop {string|undefined} className
 */
const TableObject = ({
	table = [],
	cols,
	sortable,
	sortedCol,
	handleSort,
	className,
	orderDirection,
}) => (
	<TableLayout
		className={className}
		cols={cols}
		sortable={sortable}
		sortedCol={sortedCol}
		handleSort={handleSort}
		orderDirection={orderDirection}
	>
		{table.map((el, i) => (
			<Table.Row key={i}>
				{cols.map(col => (
					<CellValue value={el[col.key]} key={col.key} />
				))}
			</Table.Row>
		))}
	</TableLayout>
);

export default TableObject;
