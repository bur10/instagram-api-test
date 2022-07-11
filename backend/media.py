from json import JSONEncoder


class Media:

    def __init__(self, type_name, display_url, caption, liked_count, comment_count):
        self.type_name = type_name
        self.display_url = display_url
        self.caption = caption
        self.liked_count = liked_count
        self.comment_count = comment_count


class IGraphImage(Media):

    def __init__(self, type_name, display_url, caption="", liked_count="", comment_count=""):
        super().__init__(type_name, display_url, caption, liked_count, comment_count)


class IChildrenGraphImage(IGraphImage):

    def __init__(self, type_name, display_url):
        super().__init__(type_name, display_url)


class IGraphVideo(Media):

    def __init__(self, type_name, display_url, video_url, caption="", liked_count="", comment_count=""):
        super().__init__(type_name, display_url, caption, liked_count, comment_count)
        self.video_url = video_url


class IChildrenGraphVideo(IGraphVideo):

    def __init__(self, type_name, display_url, video_url):
        super().__init__(type_name, display_url, video_url)


class IGraphSidecar(Media):

    def __init__(self, type_name, display_url, caption, liked_count,  comment_count, children):
        super().__init__(type_name, display_url, caption, liked_count, comment_count)
        self.children = children


class MediaEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
