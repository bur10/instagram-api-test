import React, { useState, useEffect } from 'react'
import Button from "react-bootstrap/Button";
import Modal from '../components/Modal/Modal';
import '../index.css'
import InfiniteScroll from 'react-infinite-scroller';
import Popup from 'reactjs-popup';
import LoadingSpinner from '../components/LoadingSpinner';

import { useLocation } from "react-router-dom";


function UserProfile() {


    const data = useLocation()
    const userData = data.state
    const [userMedia, setUserMedia] = useState(userData.user.edge_owner_to_timeline_media.edges)
    const [mediaEndCursor, setMediaEndCursor] = useState(userData.user.edge_owner_to_timeline_media.page_info.end_cursor)
    const [isFetching, setIsFetching] = useState(false);
    const [isLoading, setIsLoading] = useState(true);

    console.log(userData)


    const fetchMoreListItems = async () => {
        const response = await fetch(`/get_user_media/${mediaEndCursor}/${userData.user.id}`)
        const mediaData = await response.json()


        setUserMedia(userMedia => [...userMedia, ...mediaData.data.user.edge_owner_to_timeline_media.edges])
        setMediaEndCursor(mediaData.data.user.edge_owner_to_timeline_media.page_info.end_cursor)
    }

    const createPopUp = () => {
        <Modal />
    }


    return (
        <div className='container'>
            <div className="header">
                <div className="container">
                    <div className="row mb-5">
                        <div className="col-3">
                            <img className='rounded-circle' height="100" width="100" src={`https://api.codetabs.com/v1/proxy?quest=${userData.user.profile_pic_url_hd}`}
                                style={userData.story && { border: "5px solid #c034eb" }} />
                        </div>
                        <div className="col-9">
                            <div className="username">
                                <span>{userData.user.username}</span>
                            </div>
                            <div className="follow_and_posts_info">
                                <div className="row">
                                    <div className="col">
                                        <span><b>{userData.user.edge_owner_to_timeline_media.count}</b> gönderi</span>
                                    </div>
                                    <div className="col">

                                        <span><b>{userData.user.edge_followed_by.count}</b> <Button onClick={createPopUp} className='btn btn-light p-0 align-baseline'>takipçi</Button></span>
                                    </div>
                                    <div className="col">
                                        <span><b>{userData.user.edge_follow.count}</b> takip</span>
                                    </div>
                                </div>
                            </div>
                            <div className="bio-external-full_name">
                                <div className="full_name">
                                    <span><b>{userData.user.full_name}</b></span>
                                </div>
                                <div className="bio">
                                    <span>{userData.user.biography}</span>
                                </div>
                                <div className="external">
                                    <span>
                                        <a href={userData.user.external_url_linkshimmed} target="_blank" rel="noopener noreferrer">
                                            {userData.user.external_url}
                                        </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="row mb-4">
                        {
                            userData.highlights.map((e) => {
                                return <div className="col">
                                    <img className='rounded-circle' height="100" width="100" src={`https://api.codetabs.com/v1/proxy?quest=${e.cover_media.cropped_image_version.url}`}
                                        style={{ border: "1px solid #fff", outline: "2px solid #E4E4E4" }} />
                                </div>
                            })
                        }
                    </div>


                    <div className="user_media">
                        <div className="row">
                            {userMedia.map((e) => {
                                return <div className="col-4 mb-3">
                                    <img src={`https://api.codetabs.com/v1/proxy?quest=${e.node.display_url}`} style={{ width: "300px", height: "300px", objectFit: "cover" }} />

                                </div>
                            })}
                        </div>
                    </div>

                    {mediaEndCursor != "" && <div class="d-grid justify-content-center gap-2 col-6 mx-auto">
                        <Button onClick={fetchMoreListItems} className="btn btn-primary">Yükle</Button>
                    </div>}

                </div>

            </div>
        </div>
    )
}

export default UserProfile
