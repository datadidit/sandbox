'use client'
import { useState } from "react";
import { ChevronDown, ChevronUp } from "lucide-react";

const DESCENDING = "desc"
const ASCENDING = "asc"

const getTableHeader = (column, sortField, sortDirection) => {
    let columnValue = column.name

    if(column.key == sortField && sortDirection == DESCENDING){
        return (
            <div className="flex justify-center space-x-2" key={column.key}>
                {column.name} <ChevronDown/>
            </div>
        )
    }else if(column.key == sortField && sortDirection == ASCENDING){
        return (
            <div className="flex justify-center space-x-2" key={column.key}>
                <div>
                    {column.name}
                </div>
                <ChevronUp/>
            </div>
        )
    }
    return (
        <div key={column.key}>
            {column.name}
        </div>
    )
}

const BasicTable = ({columns, data}) => {
    // console.log(`Data = ${JSON.stringify(data)}`)
    // const rows = data.forEach((entry, idx) => {
    //     return
    // })
    const [tableData, setTableData] = useState(data)
    const [sortDirection, setSortDirection] = useState("")
    const [sortField, setSortField] = useState("")

    const handleColumnClick = (column, event) => {
        console.log(`click tracked on ${sortField} direction ${sortDirection}`)
        setSortField(column.key)
        let sortDirUpdate = (sortDirection == "" || sortDirection == DESCENDING) ? ASCENDING : DESCENDING;
        console.log(sortDirUpdate)
        setSortDirection(sortDirUpdate)
        // Call function to sort data.
        const sortedData = [...data].sort((a, b) => {
            let a_value = a[column.key].toString()
            let b_value = b[column.key].toString()
            if(sortDirection == ASCENDING)
                return a_value.localeCompare(b_value)
            else
                return b_value.localeCompare(a_value)
        })

        console.log(`Sorted Data by column ${column.key} \n ${JSON.stringify(data)}`)
        // Update data via setTableData
        setTableData(sortedData)
    }

    console.log("I think data should be updated!")
    return (
        <div>
            <header className="p-5 text-center">
                <h1>Very Simple Basic Table with Row Coloring</h1>
            </header>
            <table className="table-auto w-full">
                <thead
                    className="bg-gray-400"
                >
                <tr>
                    {columns.map((column) => (
                        <th
                            key={column.key}
                            onClick={e => handleColumnClick(column, e)}
                        >
                            {getTableHeader(column, sortField, sortDirection)}
                        </th>
                    ))}
                </tr>
                </thead>
                <tbody>
                {tableData.map((entry, idx) => {
                    return (
                        <tr
                            className="odd:bg-white-100 even:bg-gray-200"
                            key={idx}>
                            {columns.map((column) => {
                                // console.log(`Making it into TR ${entry}`)
                                return (
                                    <td
                                        className="px-4 text-center"
                                        key={column.key}>
                                        {entry[column.key]}
                                    </td>
                                )
                            })}
                        </tr>
                    )
                })}
                </tbody>
            </table>
        </div>
    )
}

export default BasicTable