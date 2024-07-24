import image from '../../public/image.png'
const Navbar = ({ currentDashboard, changeDashboard }: { currentDashboard: string, changeDashboard: any }) => {
    return (
        <nav style={{ backgroundColor: '#077cc2' }}>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 justify-center items-center">
                <div className="flex items-center justify-between h-16">
                    <div className="flex items-center">
                        <div className="flex-shrink-0">
                            <img className="w-32 h-16" src={image} alt="Logo" />
                        </div>
                    </div>
                    <div className='justify-center items-center'>
                        <button onClick={() => changeDashboard(currentDashboard === "HR" ? "Manager" : "HR")} className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'>{currentDashboard}</button>
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;