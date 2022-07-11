import React, { useState } from 'react'

import { useLocation } from "react-router-dom";

function UserFriends() {
    const data = useLocation()
    const userData = data.state

    return (

        <div className='container'>
            <div className="user_info mb-4">
                <div className='row'>
                    <div className='col-3'>
                        <img src={`https://api.codetabs.com/v1/proxy?quest=${userData.profile_pic_url}`} className="rounded-circle" />
                    </div>
                    <div className='col-9'>
                        <div className="user_header_info mb-1">
                            <h2>{userData.username}</h2>
                            <div className="row">
                                <div className="col">
                                    <span><b>{userData.edge_owner_to_timeline_media.count}</b> gönderi</span>
                                </div>
                                <div className="col">

                                </div>
                                <div className="col">
                                    <span><b>{userData.edge_follow.count}</b> takip</span>
                                </div>
                            </div>
                        </div>
                        <div className="user_footer_info">
                            <span><b>{userData.full_name}</b></span>
                            <br />
                            <span>{userData.biography}</span>
                            {userData.external_url != null && <a href={userData.external_url_linkshimmed}>
                                <br />
                                <span>{userData.external_url}</span>
                            </a>}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default UserFriends
