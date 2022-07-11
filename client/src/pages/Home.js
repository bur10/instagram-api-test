import React, { useState } from 'react'
import { useNavigate } from "react-router-dom";


function Home() {

    const navigate = useNavigate()

    const [username, setUsername] = useState();
    const [password, setPassword] = useState();

    const [isLoading, setIsLoading] = useState(false)
    const [err, setErr] = useState('')

    const makeRequest = async (endpoint) => {
        setIsLoading(true)
        try {
            const response = await fetch(endpoint)

            if (!response.ok) {
                throw new Error(`Error! status: ${response.status}`)
            }

            const result = await response.json()
            return result
        } catch (err) {
            setErr(err.message)
        } finally {
            setIsLoading(false)
        }
    }

    const handleSignIn = async () => {
        // const rawResponse = await fetch('/login', {
        //     method: 'POST',
        //     body: JSON.stringify({
        //         "username": username,
        //         "password": password,
        //     })
        // });

        // const content = await rawResponse.json();
        // console.log(content)

        const rawResponse2 = await fetch(`/get_user/${username}`)
        const content2 = await rawResponse2.json()

        navigate("/user_profile", { state: content2.data })

    }

    return (
        <div>
            <input type="text" placeholder='kullanici adi' onChange={(e) => { setUsername(e.target.value) }} />
            <input type="text" placeholder='şifre' onChange={(e) => { setPassword(e.target.value) }} />

            <button onClick={handleSignIn}>Giriş Yap</button>

            {/* <input value={searchValue} onChange={(e) => { setSearchValue(e.target.value) }} />
            <Button onClick={handleSearch}>Search</Button>
            <Button onClick={() => { handleGetFollowers("45409005902") }}>Get Friends</Button> */}
            {/* <input value={usernameValue} onChange={(e) => { setUsernameValue(e.target.value) }} />
            <button onClick={handleInfoClick}>Get User Info</button>

            <button onClick={handleFollowersClick}>Get Followers</button> */}
            {/* {isLoading && <h2>Loading...</h2>} */}
            {/* {searchData && searchData.map((e) => {

                return <div>

                    <div onClick={() => handleUserProfileRequest(e.user.username)}>

                        <div className="row">
                            <div className="col-md-2">
                                <img src={`https://api.codetabs.com/v1/proxy?quest=${e.user.profile_pic_url}`}
                                    className="rounded-circle" width="150" height="150" />
                            </div>
                            <div className="col-md-10">
                                <h2>{e.user.username}</h2>
                                <span>{e.user.full_name}</span>
                            </div>
                        </div>

                    </div>


                </div>
            })} */}
        </div>
    )
}

export default Home
