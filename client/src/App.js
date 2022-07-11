import { BrowserRouter, Link, Navigate, Route, Routes } from 'react-router-dom'

import Home from './pages/Home'
import UserProfile from './pages/UserProfile'
import UserFriends from './pages/UserFriends'

function App() {

    return (
        <div className='App'>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/user_profile" element={<UserProfile />} />
                    <Route path="/user_friends" element={<UserFriends />} />
                </Routes>
            </BrowserRouter>
        </div>
    )
}


export default App
