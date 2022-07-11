class InstagramUser():

    def __init__(self, id, full_name, username, biography, profile_pic_url, media, media_count, followers_count, following_count, followers_list=[], following_list=[]):
        self.id = id
        self.full_name = full_name
        self.username = username
        self.biography = biography
        self.profile_pic_url = profile_pic_url
        self.media = media
        self.media_count = media_count
        self.followers_count = followers_count
        self.following_count = following_count
        self.followers_list = followers_list
        self.following_list = following_list
