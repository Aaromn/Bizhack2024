import React, { useState } from 'react';
import { employeeData as users } from '../employeeData';

const ManagerDashboard: React.FC = () => {
    const [selectedUser, setSelectedUser] = useState<NonNullable<unknown> | null>(null);
    const [showPopup, setShowPopup] = useState(false);
    const handleNoticeClick = () => {
        setShowPopup(true);
    };

    const handlePopupClose = () => {
        setShowPopup(false);
    };
    const handleUserClick = (user: NonNullable<unknown>) => {
        setSelectedUser(user);
    };

    const handleDropdownClose = () => {
        setSelectedUser(null);
    };

    return (
        <div className="flex flex-col bg-gray-100 w-screen p-10">
            <h1 className="text-2xl font-bold m-4 text-center">Manager Dashboard</h1>

            <ul className="w-3/4 m-auto bg-white shadow-md rounded-lg">
                {users.map((user) => (
                    <li key={user.EmployeeID} className="border-b border-gray-200 last:border-b-0 w-full p-5 mb-3">
                        <button
                            className="w-full px-4 py-2 flex items-center justify-between text-left hover:bg-gray-100"
                            onClick={() => handleUserClick(user)}
                        >
                            <div className='flex items-center'>
                                <span className="text-gray-500 mr-2">👤</span>
                                <span className="text-gray-900">{user.Name}</span>
                            </div>
                            {/* Replace with actual user icon */}
                        </button>

                        {selectedUser === user && (
                            <div className="bg-white shadow-md rounded-b-lg overflow-hidden mb-5">
                                <div className="w-full px-4 py-2 flex items-center justify-between text-left hover:bg-gray-100">
                                    <span>User Details</span>
                                    <button onClick={handleDropdownClose}>Close</button>
                                </div>

                                <div className="p-4">
                                    {/* Replace with actual user details */}
                                    <div className="p-4 border-b border-gray-200">
                                        <p>Name: {user.Name}</p>
                                        <p>Emergency Contact: {user.EmergencyContact}</p>
                                        <p> <b>Skills: </b>{user.Skills.toString()} </p>
                                        <p> <b>Recommendations: </b>Suggest these courses to the employee:<br></br> {user.Recommendation?.toString()} <button className='px-4 m-1 text-left hover:bg-green-100 bg-green-200'>Notify</button></p>
                                        {user.WorkfromHome > 10 ? <p> <b>Short Fall Hours: </b>Yes <button className='px-4 m-1 text-left hover:bg-green-100 bg-green-200'>Notify</button></p> : <p> <b>Short Fall Hours: </b>No</p>}
                                        {/* Add more details as needed */}
                                    </div>

                                    {/* Add more dropdown sections as needed */}
                                </div>
                            </div>
                        )}
                    </li>
                ))}
            </ul>
            <div className="fixed bottom-0 left-0 right-0 bg-white p-4">
                <button className="rounded-full px-4 py-2 flex items-center justify-between text-left bg-green-400 hover:bg-green-300 border-" onClick={handleNoticeClick}>
                    Notice
                </button>

                {showPopup && (
                    <div className="fixed top-0 left-0 right-0 bottom-0 bg-gray-900 opacity-75">
                        <div className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-4">
                            <button className="absolute top-0 right-0 p-2" onClick={handlePopupClose}>
                                X
                            </button>
                            <h2 className="text-2xl font-bold mb-4">Notice</h2>
                            <p>Employee John Doe with id 4587123 needs to track his working hours as he has 5 hours of shortfall hours.
                            </p>
                            <button className="rounded-full px-4 py-2 flex items-center justify-between text-left bg-green-400 hover:bg-green-300 border">
                                Notify Employee via Mail
                            </button>
                        </div>
                    </div>
                )}
            </div>

        </div>
    );
};

export default ManagerDashboard;